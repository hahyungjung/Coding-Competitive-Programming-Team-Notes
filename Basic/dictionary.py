dictionary_summary.py

# https://realpython.com/python-dicts/#defining-a-dictionary

# Defining a Dictionary (1)

d = {
    <key>: <value>,
    <key>: <value>,
      .
      .
      .
    <key>: <value>
}

MLB_team = {
     'Colorado' : 'Rockies',
     'Boston'   : 'Red Sox',
     'Minnesota': 'Twins',
     'Milwaukee': 'Brewers',
     'Seattle'  : 'Mariners'
 }

# Defining a Dictionary (2)

d = dict([
    (<key>, <value>),
    (<key>, <value),
      .
      .
      .
    (<key>, <value>)
])

MLB_team = dict([
     ('Colorado', 'Rockies'),
     ('Boston', 'Red Sox'),
     ('Minnesota', 'Twins'),
     ('Milwaukee', 'Brewers'),
     ('Seattle', 'Mariners')
 ])

# Defining a Dictionary (3)

MLB_team = dict(
     Colorado='Rockies',
     Boston='Red Sox',
     Minnesota='Twins',
     Milwaukee='Brewers',
     Seattle='Mariners'
 )


# (1)
d = {'foo': 100, 'bar': 200, 'baz': 300}
# (2)
d = dict(foo=100, bar=200, baz=300)
# (3)
d = {}
d['foo'] = 100
d['bar'] = 200
d['baz'] = 300
# (4)
d = {
     ('foo', 100),
     ('bar', 200),
     ('baz', 300)
}
# Not a valid way to define this dictionary in Python
d = dict([
     ('foo', 100),
     ('bar', 200),
     ('baz', 300)
])
d
# {('foo', 100), ('baz', 300), ('bar', 200)}
type(d)
# <class 'set'>

# ----------------------------------------------------

# Building a Dictionary Incrementally

person = {}
type(person)
# <class 'dict'>

person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}

person
#{'fname': 'Joe', 'lname': 'Fonebone', 'age': 51, 'spouse': 'Edna', 'children': ['Ralph', 'Betty', 'Joey'], 'pets': {'dog': 'Fido', 'cat': 'Sox'}}

# ----------------------------------------------------

# Restrictions on Dictionary Keys

d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
d[(1,1)]
# 'a'
d[(2,1)]
# 'c'

d = {[1, 1]: 'a', [1, 2]: 'b', [2, 1]: 'c', [2, 2]: 'd'}
'''
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d = {[1, 1]: 'a', [1, 2]: 'b', [2, 1]: 'c', [2, 2]: 'd'}
TypeError: unhashable type: 'list'
'''

'''
A dictionary key must be of a type that is immutable. You have already seen examples where several of the immutable types you are familiar with—integer, float, string, and Boolean—have served as dictionary keys.
A tuple can also be a dictionary key, because tuples are immutable.
'''

# ----------------------------------------------------

# Operators and Built-in Functions

MLB_team = {
     'Colorado' : 'Rockies',
     'Boston'   : 'Red Sox',
     'Minnesota': 'Twins',
     'Milwaukee': 'Brewers',
     'Seattle'  : 'Mariners'
 }

'Milwaukee' in MLB_team
# True
'Toronto' in MLB_team
# False
'Toronto' not in MLB_team
# True

MLB_team['Toronto']
'''
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    MLB_team['Toronto']
KeyError: 'Toronto'
'''

'Toronto' in MLB_team and MLB_team['Toronto']
# False




