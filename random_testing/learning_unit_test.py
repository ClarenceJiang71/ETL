from unittest import TestCase
# from random_testing import test2
from test2 import add

# import sys
# sys.path.append('/Users/clarencestudy/Desktop/Tech/ETL/ETL')
# from random_testing.test2 import add

class MyTest(TestCase):
    def setUp(self) -> None:
        """
        the steps that should be run before testing 
        Things like connection and setup 
        similar to init
        """
      
        pass 

    def test_add(self):
        res = add(1, 2)
        self.assertEqual(res, 3)
        

    def tearDown(self) -> None:
        """
        Things to do after testing, like end connection
        """

        pass