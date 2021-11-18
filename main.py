import ujson

ujson.dumps([{"key": "value"}, 81, True])
'[{"key":"value"},81,true]'
ujson.loads("""[{"key": "value"}, 81, true]""")
[{'key': 'value'}, 81, True]


import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code
200
r.headers['content-type']
'application/json; charset=utf8'
r.encoding
'utf-8'
r.text
'{"type":"User"...'
r.json()
{'disk_usage': 368627, 'private_gists': 484, ...}


import jmespath

expression = jmespath.compile('foo.bar')
expression.search({'foo': {'bar': 'baz'}})
'baz'
expression.search({'foo': {'bar': 'other'}})
'other'


from Rich import print

print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())


from PIL import Image

background = Image.open("bg.jpg")
background.show()


from emoji import emojize

moj = emojize('Packages are :fire:')
print(moj)
