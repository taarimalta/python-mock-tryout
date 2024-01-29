""" This tutorial is about validating calls
"""


from unittest.mock import Mock


json = Mock()

json.loads('{"key": "value"}')

json.loads.assert_called()
json.loads.assert_called_once()
json.loads.assert_called_with('{"key": "value"}')
json.loads.assert_called_once_with('{"key": "value"}')


json.loads('{"key": "value"}')


"""
Output:
2
"""
print(json.loads.call_count)

"""
Output:
call('{"key": "value"}')
"""
print(json.loads.call_args)

"""
Output:
[call('{"key": "value"}'), call('{"key": "value"}')]
"""
print(json.loads.call_args_list)


"""
Output:
[call.loads('{"key": "value"}'), call.loads('{"key": "value"}')]
"""
print(json.method_calls)


