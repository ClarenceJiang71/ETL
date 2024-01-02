import sys
sys.path.append('/Users/clarencestudy/Desktop/Tech/ETL/ETL')
from unittest import TestCase
from util.str_util import check_null, check_str_null_and_transform_to_sql_null


class TestStrUtil(TestCase):
    def setUp(self) -> None: 
        pass 

    def test_check_null(self):
        s = None 
        self.assertTrue(check_null(s))
        s = "None" 
        self.assertTrue(check_null(s))
        s = "NONE" 
        self.assertTrue(check_null(s))
        s = " None " 
        self.assertTrue(check_null(s))
        s = "null" 
        self.assertTrue(check_null(s))
        s = "undefined" 
        self.assertTrue(check_null(s)) 
        s = "" 
        self.assertTrue(check_null(s))
        s = "with a meaning" 
        self.assertFalse(check_null(s))

    def test_check_str_null_and_transform_to_sql_null(self):
        s = None
        result = check_str_null_and_transform_to_sql_null(s)
        self.assertEqual("NULL", result) 

        s = 1 
        result = check_str_null_and_transform_to_sql_null(s)
        # be careful with the detail in the SQL query 
        self.assertEqual("'1'", result) 

        s = "hunan"
        result = check_str_null_and_transform_to_sql_null(s)
        # be careful with the detail in the SQL query 
        self.assertEqual("'hunan'", result) 

        s = "None"
        result = check_str_null_and_transform_to_sql_null(s)
        # be careful with the detail in the SQL query 
        self.assertEqual("NULL", result) 

    def tearDown(self):
        pass 