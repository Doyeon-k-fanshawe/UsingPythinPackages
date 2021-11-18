import jmespath

expression = jmespath.compile('foo.bar')
expression.search({'foo': {'bar': 'baz'}})
'baz'
expression.search({'foo': {'bar': 'other'}})
'other'