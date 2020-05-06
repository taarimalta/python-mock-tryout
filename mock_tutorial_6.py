from unittest.mock import Mock

def example1():

    mock = Mock(side_effect=Exception)
    mock()

def example2():
    mock = Mock(name='Real Python Mock')
    print(mock)


def example3():
    mock = Mock(return_value=True)
    print(mock())

def example4():
    mock = Mock(name='Real Python Mock')
    print(mock.name)

    mock = Mock()
    mock.name='Real Python Mock'
    print(mock.name)

def example5():
    mock = Mock()
    mock.configure_mock(return_value=True)
    print(mock)
    print(mock())


def example6():
    response_mock=Mock()
    response_mock.json.return_value = {
        '12/25': 'Christmas',
        '7/4': 'Independece Day'
    }

    print(response_mock.json())


def example7():
    holidays={
        '12/25': 'Chrismas',
        '7/4':'Independence Day'
    }

    response_mock = Mock(**{'json.return_value':holidays})

    print(response_mock.json())


if __name__=='__main__':
    example7()
