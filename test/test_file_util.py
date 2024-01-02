import os
from unittest import TestCase
import sys
sys.path.append('/Users/clarencestudy/Desktop/Tech/ETL/ETL')
from util.file_util import get_dir_files_list, get_new_by_compare_lists

class TestFileUtil(TestCase):
    def setUp(self) -> None:
        # 确定test folder path
        self.project_root_path = os.path.dirname(os.getcwd())


    def test_get_dir_files_list(self):
      
        res1 = get_dir_files_list(self.project_root_path + "/ETL/" + 'test_dir', 
                           recursive=False)
        predicted_result = ['1', '2']
        result = []
        for p in predicted_result:
            result.append(self.project_root_path + "/ETL/" +"test_dir" + "/" + p)
        self.assertEqual(res1, result)

        res2 = get_dir_files_list(self.project_root_path + "/ETL/" + 'test_dir', 
                           recursive=True)
        print(res2)

        """
        when assertequal the recursive result, make sure the order is 
        taken care 
        """


    def test_get_new_compare_lists(self):
        b_list = ['e:/a.txt', 'e:/b.txt']
        a_list = ['e:/a.txt', 'e:/b.txt', 'e:/c.txt', 'e:/d.txt']
        # 测试get_new_by_compare_lists,并获取返回的数据差
        result = get_new_by_compare_lists(a_list, b_list)
        result.sort()
        # 使用断言判断返回数据的值是否正确
        self.assertListEqual(result, ['e:/c.txt', 'e:/d.txt'])   


    def tearDown(self) -> None:
        pass