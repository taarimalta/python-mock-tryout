"""This tutorial is about Timeout as a sideeffect"""

import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock
import requests


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()

    return None


requests = Mock()


class TestCalendar(unittest.TestCase):

    def test_get_holidays_timeout(self):
        # Test a connection timeout
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            print(get_holidays())


if __name__ == '__main__':
    unittest.main()
