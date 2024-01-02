from unittest import TestCase
from util.time_util import ts10_to_date_string, ts13_to_date_string

class TestTimeUtil(TestCase):
    def setUp(self) -> None:
        pass

    def test_ts10_to_date_str(self):
        ts = 1703795802
        result = ts10_to_date_string(ts, "%Y-%m-%d %H:%M:%S")
        self.assertEqual(result, "2023-12-28 15:36:42")

    def test_ts13_to_date_str(self):
        ts = 1703795802806
        result = ts13_to_date_string(ts, "%Y-%m-%d %H:%M:%S")
        self.assertEqual(result, "2023-12-28 15:36:42")


    def tearDown(self) -> None:
        pass