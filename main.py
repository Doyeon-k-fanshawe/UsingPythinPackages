from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *
now = parse("Sat Oct 11 17:13:46 UTC 2003")
today = now.date()
year = rrule(YEARLY,dtstart=now,bymonth=8,bymonthday=13,byweekday=FR)[0].year
rdelta = relativedelta(easter(year), today)
print("Today is: %s" % today)
Today is: 2003-10-11
print("Year with next Aug 13th on a Friday is: %s" % year)
Year with next Aug 13th on a Friday is: 2004
print("How far is the Easter of that year: %s" % rdelta)
How far is the Easter of that year: relativedelta(months=+6)
print("And the Easter of that year is: %s" % (today+rdelta))
And the Easter of that year is: 2004-04-11

 
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

