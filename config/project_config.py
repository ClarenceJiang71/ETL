import time

log_root_path = "logs/"
log_filename = f"pyetl-{time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))}.log"
level = 20


### MYSQL CONFIG###
mysql_charset = "utf8"
### METADATA CONFIG###
metadata_host = "localhost"
metadata_port = 3306 
metadata_user = "root"
metadata_password = "dbuserdbuser"
metadata_database = "metadata"
#### For comparison tool #### 
metadata_file_monitor_table_name = "file_monitor"
metadata_file_monitor_table_create_cols = """
    id int primary key auto_increment, 
    file_name varchar(255) unique not null comment 'the name of processed files',
    process_lines int comment 'count of processed data',
    process_time timestamp default current_timestamp comment 'processed time'

"""

#### JSON related path #### 
json_data_root_path = "/Users/clarencestudy/Desktop/Tech/ETL/data/json_data"

#### CSV related path #### 
retail_output_csv_root_path = "/Users/clarencestudy/Desktop/Tech/ETL/data/output/csv/"
retail_orders_output_csv_file_name = f'orders-{time.strftime("%Y%m%d-%H%M%S", time.localtime())}.csv'
retail_orders_detail_output_csv_file_name = f'orders-detail-{time.strftime("%Y%m%d-%H%M%S", time.localtime())}.csv'

#### target retail database related ####
target_host = metadata_host
target_user = metadata_user
target_password = metadata_password
target_port = metadata_port
target_db_name = "retail"

target_orders_table_name = "orders"
target_orders_table_create_cols = \
    f"order_id VARCHAR(255) PRIMARY KEY, " \
    f"store_id INT COMMENT '店铺ID', " \
    f"store_name VARCHAR(30) COMMENT '店铺名称', " \
    f"store_status VARCHAR(10) COMMENT '店铺状态(open,close)', " \
    f"store_own_user_id INT COMMENT '店主id', " \
    f"store_own_user_name VARCHAR(50) COMMENT '店主名称', " \
    f"store_own_user_tel VARCHAR(15) COMMENT '店主手机号', " \
    f"store_category VARCHAR(10) COMMENT '店铺类型(normal,test)', " \
    f"store_address VARCHAR(255) COMMENT '店铺地址', " \
    f"store_shop_no VARCHAR(255) COMMENT '店铺第三方支付id号', " \
    f"store_province VARCHAR(10) COMMENT '店铺所在省', " \
    f"store_city VARCHAR(10) COMMENT '店铺所在市', " \
    f"store_district VARCHAR(10) COMMENT '店铺所在行政区', " \
    f"store_gps_name VARCHAR(255) COMMENT '店铺gps名称', " \
    f"store_gps_address VARCHAR(255) COMMENT '店铺gps地址', " \
    f"store_gps_longitude VARCHAR(255) COMMENT '店铺gps经度', " \
    f"store_gps_latitude VARCHAR(255) COMMENT '店铺gps纬度', " \
    f"is_signed TINYINT COMMENT '是否第三方支付签约(0,1)', " \
    f"operator VARCHAR(10) COMMENT '操作员', " \
    f"operator_name VARCHAR(50) COMMENT '操作员名称', " \
    f"face_id VARCHAR(255) COMMENT '顾客面部识别ID', " \
    f"member_id VARCHAR(255) COMMENT '顾客会员ID', " \
    f"store_create_date_ts TIMESTAMP COMMENT '店铺创建时间', " \
    f"origin VARCHAR(255) COMMENT '原始信息(无用)', " \
    f"day_order_seq INT COMMENT '本订单是当日第几单', " \
    f"discount_rate DECIMAL(10, 5) COMMENT '折扣率', " \
    f"discount_type TINYINT COMMENT '折扣类型', " \
    f"discount DECIMAL(10, 5) COMMENT '折扣金额', " \
    f"money_before_whole_discount DECIMAL(10, 5) COMMENT '折扣前总金额', " \
    f"receivable DECIMAL(10, 5) COMMENT '应收金额', " \
    f"erase DECIMAL(10, 5) COMMENT '抹零金额', " \
    f"small_change DECIMAL(10, 5) COMMENT '找零金额', " \
    f"total_no_discount DECIMAL(10, 5) COMMENT '总价格(无折扣)', " \
    f"pay_total DECIMAL(10, 5) COMMENT '付款金额', " \
    f"pay_type VARCHAR(10) COMMENT '付款类型', " \
    f"payment_channel TINYINT COMMENT '付款通道', " \
    f"payment_scenarios VARCHAR(15) COMMENT '付款描述(无用)', " \
    f"product_count INT COMMENT '本单卖出多少商品', " \
    f"date_ts TIMESTAMP COMMENT '订单时间', " \
    f"INDEX (receivable), INDEX (date_ts)"

target_orders_detail_table_name = "orders_detail"
target_orders_detail_table_create_cols = \
    f"order_id varchar(255), " \
    f"barcode varchar(255), " \
    f"name varchar(255), " \
    f"count int comment 'how many products in this order', "\
    f"price_per decimal(10,5), " \
    f"retail_price decimal(10,5), " \
    f"trade_price decimal(10,5), " \
    f"category_id int, " \
    f"unit_id int, " \
    f"primary key (order_id, barcode)"
    
# 数据源库配置
source_host = 'localhost'
source_user = 'root'
source_password = 'dbuserdbuser'
source_port = 3306
source_database = 'source_data'
# 数据源表名称
source_barcode_table_name = 'sys_barcode'

# 目标数据表与数据表结构
target_barcode_table_name = 'sys_barcode'
target_barcode_table_create_cols = """
    `code` varchar(50) PRIMARY KEY COMMENT '商品条码',
    `name` varchar(200) DEFAULT '' COMMENT '商品名称',
    `spec` varchar(200) DEFAULT '' COMMENT '商品规格',
    `trademark` varchar(100) DEFAULT '' COMMENT '商品商标',
    `addr` varchar(200) DEFAULT '' COMMENT '商品产地',
    `units` varchar(50) DEFAULT '' COMMENT '商品单位(个、杯、箱、等)',
    `factory_name` varchar(200) DEFAULT '' COMMENT '生产厂家',
    `trade_price` DECIMAL(50, 5) DEFAULT 0.0 COMMENT '贸易价格(指导进价)',
    `retail_price` DECIMAL(50, 5) DEFAULT 0.0 COMMENT '零售价格(建议卖价)',
    `update_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    `wholeunit` varchar(50) DEFAULT NULL COMMENT '大包装单位',
    `wholenum` int(11) DEFAULT NULL COMMENT '大包装内装数量',
    `img` varchar(500) DEFAULT NULL COMMENT '商品图片',
    `src` varchar(20) DEFAULT NULL COMMENT '源信息', 
    INDEX (update_at)
"""

# 商品数据写出 csv 根路径
barcode_output_csv_root_path = "/Users/clarencestudy/Desktop/Tech/ETL/data/output/barcode/"
# 商品数据写出 csv 文件名
barcode_orders_output_csv_file_name = f'barcode-{time.strftime("%Y-%m-%d-%H_%M", time.localtime())}.csv'

metadata_barcode_table_name = 'barcode_monitor'
# barcode业务：update_at字段的监控表的建表语句的列信息
metadata_barcode_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT COMMENT '自增ID', " \
                                     "time_record TIMESTAMP NOT NULL COMMENT '本次采集记录的最大时间', " \
                                     "gather_line_count INT NULL COMMENT '本次采集条数'"