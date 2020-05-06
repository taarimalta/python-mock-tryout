"""This tutorial is about a callback as sideeffect"""

from unittest.mock import Mock
import unittest
import requests
from requests.exceptions import Timeout

def get_holidays():
    r = requests.get('http://localhost/api/holidays')

    if r.status_code == 200:
        return r.json()

    return None


requests = Mock()


class TestCalendar(unittest.TestCase):

    def test_get_holidays_logging(self):

        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day'
        }

        requests.get.side_effect = [Timeout, response_mock]

        # Test that the first request raises a Timeout
        with self.assertRaises(Timeout):
            get_holidays()

        # Now retry, expecting a successful response
        assert get_holidays()['12/25'] == 'Christmas'

        # Finally, assert .get() was called twice
        assert requests.get.call_count == 2


if __name__ == '__main__':
    unittest.main()
