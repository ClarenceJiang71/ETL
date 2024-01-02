"""
Support the function that convert timestamp to string tools
"""

import time

def ts10_to_date_string(ts, format_string = "%Y-%m-%d %H:%M:%S"):
    """
    Convert a 10 digit timestamp to string form
    """
    return time.strftime(format_string, time.localtime(ts))


def ts13_to_date_string(ts, format_string = "%Y-%m-%d %H:%M:%S"):
    ts10 = int(ts/1000)
    return ts10_to_date_string(ts10, format_string)