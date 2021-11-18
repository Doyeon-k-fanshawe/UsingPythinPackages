import ujson

ujson.dumps([{"key": "value"}, 81, True])
'[{"key":"value"},81,true]'
ujson.loads("""[{"key": "value"}, 81, true]""")
[{'key': 'value'}, 81, True]
