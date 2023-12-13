from unittest.mock import Mock


def example1():
    """Output:

    ```
      File "/usr/lib/python3.9/unittest/mock.py", line 1151, in _execute_mock_call
        raise effect
    Exception
    ```
    """

    mock = Mock(side_effect=Exception)
    mock()


def example2():
    """Output:
    <Mock name='Real Python Mock' id='139678848849376'>

    """
    mock = Mock(name='Real Python Mock')
    print(mock)


def example3():
    """Output:
    True

    """
    mock = Mock(return_value=True)
    print(mock())


def example4():
    """Output:
    <Mock name='Real Python Mock.name' id='139982370330128'>
    Real Python Mock

    """
    mock = Mock(name='Real Python Mock')
    print(mock.name)

    mock = Mock()
    mock.name = 'Real Python Mock'
    print(mock.name)


def example5():
    """Output:
    <Mock id='139931730765280'>
    True
    """
    mock = Mock()
    mock.configure_mock(return_value=True)
    print(mock)
    print(mock())


def example6():
    """Output:
    {'12/25': 'Christmas', '7/4': 'Independece Day'}
    """
    response_mock = Mock()
    response_mock.json.return_value = {
        '12/25': 'Christmas',
        '7/4': 'Independece Day'
    }

    print(response_mock.json())


def example7():
    """Output:
        {'12/25': 'Chrismas', '7/4': 'Independence Day'}

    """
    holidays = {
        '12/25': 'Chrismas',
        '7/4': 'Independence Day'
    }

    response_mock = Mock(**{'json.return_value': holidays})

    print(response_mock.json())


if __name__ == '__main__':
    example7()
