from unittest import TestCase
import sys
sys.path.append('/Users/clarencestudy/Desktop/Tech/ETL/ETL')
from util.mysql_util import MySQLUtil, get_proceed_files
from util.logging_util import init_logger
import config.project_config as config

logger = init_logger()


class TestMySQLUtil(TestCase):
    def setUp(self) -> None:
        self.mysql_util = MySQLUtil() # default connects to metadata
        pass 

    def test_query(self):
        self.mysql_util.select_db("test")

        if not self.mysql_util.check_table_exists("test", "for_unittest"):
            self.mysql_util.create_table(
                'test',
                'for_unittest',
                'id int primary key, name varchar(255)'
            )

        else:
            logger.debug("the table 'for_unittest' already exists")

        self.mysql_util.execute_with_commit(
            "insert into for_unittest values (1, 'xiaoxiao'), (2, 'tiantian')"
        )

        results = self.mysql_util.query(
            "select * from for_unittest order by id"
        )
        self.assertEqual(results, ((1, 'xiaoxiao'), (2, 'tiantian')))

        self.mysql_util.execute_with_commit(
            "drop table for_unittest"
        )

        self.mysql_util.close()
        self.mysql_util.close()

    def test_execute_without_commit(self):
        self.mysql_util.conn.autocommit(True)

        self.mysql_util.select_db("test")

        if not self.mysql_util.check_table_exists("test", "for_unittest"):
            self.mysql_util.create_table(
                'test',
                'for_unittest',
                'id int primary key, name varchar(255)'
            )

        else:
            logger.debug("the table 'for_unittest' already exists")

        self.mysql_util.execute_without_commit(
            "insert into for_unittest values (1, 'xiaoxiao'), (2, 'tiantian')"
        )

        results = self.mysql_util.query(
            "select * from for_unittest order by id"
        )
        logger.debug(results)
        self.assertEqual(results, ((1, 'xiaoxiao')))

        self.mysql_util.execute_without_commit(
            "drop table for_unittest"
        )

        self.mysql_util.close()
        self.mysql_util.close()

    def test_get_processed_files(self):
        self.mysql_util.select_db("test")
        self.mysql_util.execute_with_commit("drop table if exists test_file_monitor")
        results = get_proceed_files(self.mysql_util, 'test', 'test_file_monitor')
        self.assertEqual(results, [])

        if not self.mysql_util.check_table_exists('test', 'test_file_monitor'):
            self.mysql_util.create_table('test',
                                         'test_file_monitor',
                                         config.metadata_file_monitor_table_create_cols
                                         )
        self.mysql_util.execute_with_commit("truncate test_file_monitor")

        self.mysql_util.execute_with_commit(
            "insert into test_file_monitor values (1, 'e:/data.log', 1024, '2000-01-01 10:00:00') "
        )

        results = get_proceed_files(self.mysql_util, 'test', 'test_file_monitor')
        self.assertEqual(results, ['e:/data.log'])


        self.mysql_util.execute_with_commit(
            "insert into test_file_monitor values (2, 'e:/data1.log', 1024, '2000-01-01 10:00:00') "
        )

        results1 = get_proceed_files(self.mysql_util, 'test', 'test_file_monitor')
        results1.sort()
        self.assertEqual(results1, ['e:/data.log', 'e:/data1.log'])

           
    


