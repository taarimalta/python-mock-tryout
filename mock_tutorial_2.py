""" This tutorial is about setting return value for methods
"""

from datetime import datetime


def is_weekday():
    today = datetime.today()

    return (0 <= today.weekday() < 5)

"""
Output depends on weekday
True
"""
print(is_weekday())

from unittest.mock import Mock


tuesday = datetime(year=2019, month=1, day =1)
saturday = datetime(year=2019, month=1, day = 5)


datetime=Mock()
datetime.today.return_value = tuesday

assert is_weekday()

datetime.today.return_value = saturday

assert not is_weekday()


