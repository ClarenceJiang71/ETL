"""
Collect json files and the files from MySQL database 
extract the files that have not been processed and not in the database
"""
from util.logging_util import init_logger
from util.file_util import get_dir_files_list, get_new_by_compare_lists
from util.mysql_util import MySQLUtil, get_proceed_files
import config.project_config as config
from model.retail_orders_model import OrderModel, OrderDetailModel

logger = init_logger()

def build_db_util():
    db_util = MySQLUtil()
    target_util = MySQLUtil(
        host = config.target_host, 
        port = config.target_port,
        user = config.target_user,
        password = config.target_password,
        database = config.target_db_name
    )
    return db_util,target_util


def get_process_files():
    # 1. read json files 
    files = get_dir_files_list(path = config.json_data_root_path, recursive=False)
    logger.info(f"find these json files {files}")

    # 2. extract those json file names that are already processed in the db
    processed_files = get_proceed_files(db_util)
    logger.info(f"We find these files: {processed_files} are already processed")

    # 3. compare and process json file names 
    need_to_process_files = get_new_by_compare_lists(files, processed_files)
    logger.info(f"we find these files {need_to_process_files} need to be processed")

    return need_to_process_files


def build_model_list(file_name):
    # how many lines in the original json file 
    file_processed_lines_count = 0
    order_model_list = []
    order_detail_model_list = []
    for line in open(file_name, "r", encoding="UTF-8"):
        file_processed_lines_count += 1

        order_model = OrderModel(line)
        order_detail_model = OrderDetailModel(line)
        order_model_list.append(order_model)
        order_detail_model_list.append(order_detail_model)
    return order_model_list,order_detail_model_list, file_processed_lines_count


def filter_except_data(order_model_list):
    reserved_models = []
    for model in order_model_list:
        if model.receivable <= 10000: 
            reserved_models.append(model)
    return reserved_models

def get_order_csv_file():
    order_csv_write_f = open(
            file = config.retail_output_csv_root_path + config.retail_orders_output_csv_file_name,
            mode = "a",
            encoding="UTF-8"
        )

    order_detail_csv_write_f = open(
            file = config.retail_output_csv_root_path+config.retail_orders_detail_output_csv_file_name,
            mode = 'a', 
            encoding="UTF-8"
        )
    
    return order_csv_write_f,order_detail_csv_write_f

def write_model_data_to_csv(order_detail_model_list, reserved_models, order_csv_write_f, order_detail_csv_write_f):
    for model in reserved_models:
        line = model.to_csv()
        order_csv_write_f.write(line)
        order_csv_write_f.write('\n')
    order_csv_write_f.close()

    for model in order_detail_model_list:
        line = model.to_csv()
        order_detail_csv_write_f.write(line)
            # # No need for further write line cuz it is included in the to_csv function 
            # order_detail_csv_write_f.write('\n')
    order_detail_csv_write_f.close()

def create_order_tables(target_util):
    if not target_util.check_table_exists(config.target_db_name, config.target_orders_table_name):
        target_util.create_table(
                config.target_db_name,
                config.target_orders_table_name,
                config.target_orders_table_create_cols
            )
        
    if not target_util.check_table_exists(config.target_db_name, config.target_orders_detail_table_name):
        target_util.create_table(
                config.target_db_name,
                config.target_orders_detail_table_name,
                config.target_orders_detail_table_create_cols
            )

def write_model_data_to_mysql(target_util, reserved_models):
    for i, model in enumerate(reserved_models):
        sql = model.generate_insert_sql()
        target_util.select_db(config.target_db_name)
        target_util.execute_without_commit(sql)
            # be careful memory might not be enough, so set up auto submit per 1000s
        if (i+1) % 1000 == 0:
            target_util.conn.commit()
        # careful about those that are left over
    target_util.conn.commit()

def write_to_csv(order_detail_model_list, reserved_models):
    order_csv_write_f, order_detail_csv_write_f = get_order_csv_file()

    write_model_data_to_csv(order_detail_model_list, reserved_models, order_csv_write_f, order_detail_csv_write_f)

def write_to_mysql(target_util, order_detail_model_list, reserved_models):
    create_order_tables(target_util)

    write_model_data_to_mysql(target_util, reserved_models)
    write_model_data_to_mysql(target_util, order_detail_model_list)

def write_metadata_to_metadatabase(db_util, processed_files_record_dict):
    for file_name, processed_lines in processed_files_record_dict.items():
        insert_sql = f"insert into {config.metadata_file_monitor_table_name} (file_name, process_lines) " \
                        f"values ('{file_name}', {processed_lines})"
        db_util.select_db("metadata")
        db_util.execute_with_commit(insert_sql)

if __name__ == '__main__':

   
    logger.info("start program")

     # construct the mysql util object
    db_util, target_util = build_db_util()

    need_to_process_files = get_process_files()

    # 4. process the files, after this step, csv has been generated
    processed_files_record_dict = {} # collect how many lines in each raw json file

    for file_name in need_to_process_files:
    
        order_model_list, order_detail_model_list, file_processed_lines_count = build_model_list(file_name)

        reserved_models = filter_except_data(order_model_list)
        
        write_to_csv(order_detail_model_list, reserved_models)

        processed_files_record_dict[file_name] = file_processed_lines_count

        logger.info(f"The output of order and order details are finished, it was written to {config.retail_output_csv_root_path}")
        
        # 5. write the data from model lists into mysql
       
        ## 5.1 check if the tables already exists 
        write_to_mysql(target_util, order_detail_model_list, reserved_models)
            
    global_count = sum(processed_files_record_dict.values())

    logger.info(f"finish all the mysql insertion, processed a total of {global_count} lines")


    write_metadata_to_metadatabase(db_util, processed_files_record_dict)
    
    target_util.close()
    db_util.close()
