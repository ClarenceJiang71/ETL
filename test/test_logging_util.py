from unittest import TestCase
import sys
sys.path.append('/Users/clarencestudy/Desktop/Tech/ETL/ETL')
from util.logging_util import init_logger
from logging import RootLogger

class TestLogginUtil(TestCase):
    def setUp(self) -> None:
        pass

    def test_init_logger(self):
        logger = init_logger()
        res = isinstance(logger, RootLogger)
        self.assertEqual(res, True)
        self.assertIsInstance(logger, RootLogger)

    def tearDown(self) -> None: 
        pass