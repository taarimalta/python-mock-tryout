import unittest
from mock_tutorial_7.src.code_to_test import get_holidays, requests, is_weekday
from unittest.mock import patch
from datetime import datetime


class TestCalendar(unittest.TestCase):

    @patch('mock_tutorial_7.src.code_to_test.requests')
    def test_get_holidays_timeout(self, mock_requests):
        """Output:
        1
        call('http://localhost/api/holidays')
        [call('http://localhost/api/holidays')]
        [call.get('http://localhost/api/holidays')]

        """
        mock_requests.get.side_effect = requests.exceptions.Timeout

        with self.assertRaises(requests.exceptions.Timeout):
            get_holidays()

        mock_requests.get.assert_called_once()
        print(mock_requests.get.call_count)
        print(mock_requests.get.call_args)
        print(mock_requests.get.call_args_list)
        print(mock_requests.method_calls)

    def test_get_holidays_timeout_alternate(self):
        """Output:
        1
        call('http://localhost/api/holidays')
        [call('http://localhost/api/holidays')]
        [call.get('http://localhost/api/holidays')]

        """
        with patch('mock_tutorial_7.src.code_to_test.requests') as mock_requests:
            mock_requests.get.side_effect = requests.exceptions.Timeout

            with self.assertRaises(requests.exceptions.Timeout):
                get_holidays()

            mock_requests.get.assert_called_once()
            print(mock_requests.get.call_count)
            print(mock_requests.get.call_args)
            print(mock_requests.get.call_args_list)
            print(mock_requests.method_calls)

    @patch.object(requests, 'get', side_effect=requests.exceptions.Timeout)
    def test_get_holidays_timeout_alternate_2(self, mock_get):
        """Output:
        1
        call('http://localhost/api/holidays')
        [call('http://localhost/api/holidays')]
        []"""
        with self.assertRaises(requests.exceptions.Timeout):
            get_holidays()

        mock_get.assert_called_once()
        print(mock_get.call_count)
        print(mock_get.call_args)
        print(mock_get.call_args_list)
        print(mock_get.method_calls)

    @patch('mock_tutorial_7.src.code_to_test.datetime')
    def test_is_weekday_alternate_1(self, mock_datetime):
        tuesday = datetime(year=2019, month=1, day=1)
        wednesday = datetime(year=2019, month=1, day=2)
        saturday = datetime(year=2019, month=1, day=5)

        mock_datetime.today.return_value = tuesday
        assert is_weekday()

        mock_datetime.today.return_value = wednesday
        assert is_weekday()

        mock_datetime.today.return_value = saturday
        assert not is_weekday()


if __name__ == '__main__':
    unittest.main()
