""" This tutorial is about validating calls"""


from unittest.mock import Mock


json = Mock()

json.loads('{"key": "value"}')

json.loads.assert_called()
json.loads.assert_called_once()
json.loads.assert_called_with('{"key": "value"}')
json.loads.assert_called_once_with('{"key": "value"}')


json.loads('{"key": "value"}')



print(json.loads.call_count)
print(json.loads.call_args)
print(json.loads.call_args_list)
print(json.method_calls)


