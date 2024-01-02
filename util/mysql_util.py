import pymysql
from util.logging_util import init_logger
import config.project_config as config
logger = init_logger()

class MySQLUtil: 
    def __init__(self, 
                host = config.metadata_host, 
                port = config.metadata_port, 
                user = config.metadata_user,
                password = config.metadata_password, 
                charset = config.mysql_charset,
                database = config.metadata_database
                ) -> None:
        """
        connect MySQL
        """
        self.conn = pymysql.connect(
            host = host, 
            port = port, 
            user = user,
            password = password, 
            charset = charset,
            database = database,
            autocommit = False
        )
        if self.conn: 
            logger.info('connection successful')
        

    def close(self):
        # defensive that avoids multiple running of the same function
        if self.conn:
            self.conn.close()
            self.conn = None 
        

    def query(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        logger.info(res)
        return res  

    def select_db(self, db):
        """
        Switch database given a database name 
        """
        self.conn.select_db(db)
        logger.debug(f"switch to the db {db}")


    def execute_with_commit(self, sql):
        """
        Make sure the query is commited      
        """
        cursor = self.conn.cursor()
        cursor.execute(sql)

        logger.debug(f"One line of SQL gets executed: {sql}")

        # make sure it gets submitted 
        if not self.conn.get_autocommit():
            self.conn.commit()

        cursor.close() 

    def execute_without_commit(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        logger.debug("One line of SQL exeucted without checking commit: {sql}")
        cursor.close()

    def check_table_exists(self, db_name, table_name):
        self.select_db(db_name)
        res = self.query("show tables")

        return (table_name, ) in res


    def create_table(self, db_name, table_name, create_cols):
        # if not self.check_table_exists(db_name, table_name):
        sql = f"create table {table_name} ({create_cols})"
        self.select_db(db_name)
        self.execute_with_commit(sql)
        logger.info(f"just created {table_name} table in the {db_name} database")

        # else: 
        #     logger.info(f"the db {db_name} has table {table_name} already existed")


def get_proceed_files(db_util, 
                      db_name=config.metadata_database, 
                      table_name=config.metadata_file_monitor_table_name, 
                      create_cols = config.metadata_file_monitor_table_create_cols):
    """
    process the files that are already processed 
    """

    db_util.select_db(db_name)
    
    if not db_util.check_table_exists(db_name, table_name):
        db_util.create_table(db_name, table_name, create_cols)
    else: 
        logger.debug("The table already exists")


    results = db_util.query(f"select file_name from {table_name}")
    file_names = []
    for result in results: 
        file_names.append(result[0])
    return file_names

if __name__ == "__main__":
    mysql_util = MySQLUtil()
    # mysql_util.query("select * from test;")
    mysql_util.select_db('retail')
    mysql_util.query("select database();")

    # mysql_util.close()
    if not mysql_util.check_table_exists("metadata", "test2"):
        mysql_util.create_table("metadata", "test2", "name varchar(255), age int")


    mysql_util.close()



