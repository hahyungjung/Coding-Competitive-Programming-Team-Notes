dictionary_method.py

# https://realpython.com/python-dicts/#defining-a-dictionary

# Built-in Dictionary Methods

# ------------------------------------------------------------
# d.clear()
# Clears a dictionary.

d = {'a': 10, 'b': 20, 'c': 30}
d
# {'a': 10, 'b': 20, 'c': 30}

d.clear()
d
# {}
# ------------------------------------------------------------
# d.get(<key>[, <default>])
# Returns the value for a key if it exists in the dictionary.

d = {'a': 10, 'b': 20, 'c': 30}

print(d.get('b'))
# 20
print(d.get('z'))
# None

# If <key> is not found and the optional <default> argument is specified, that value is returned instead of None:

print(d.get('z', -1))
# -1
# ------------------------------------------------------------
# d.items()
# Returns a list of key-value pairs in a dictionary.

d = {'a': 10, 'b': 20, 'c': 30}

list(d.items())
# [('a', 10), ('b', 20), ('c', 30)]
list(d.items())[1][0]
# 'b'
list(d.items())[1][1]
# 20
# ------------------------------------------------------------
# d.keys()
# Returns a list of keys in a dictionary.

d = {'a': 10, 'b': 20, 'c': 30}

list(d.keys())
# ['a', 'b', 'c']
# ------------------------------------------------------------
# d.values()
# Returns a list of values in a dictionary.

d = {'a': 10, 'b': 20, 'c': 30}

list(d.values())
# [10, 20, 30]

# Any duplicate values in d will be returned as many times as they occur:
d = {'a': 10, 'b': 10, 'c': 10}

list(d.values())
# [10, 10, 10]
# ------------------------------------------------------------
# d.pop(<key>[, <default>])
# Removes a key from a dictionary, if it is present, and returns its value.

d = {'a': 10, 'b': 20, 'c': 30}

d.pop('b')
# 20
d
# {'a': 10, 'c': 30}

# d.pop(<key>) raises a KeyError exception if <key> is not in d:
d = {'a': 10, 'b': 20, 'c': 30}

d.pop('z')
'''
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d.pop('z')
KeyError: 'z'
'''

# If <key> is not in d, and the optional <default> argument is specified, then that value is returned, and no exception is raised:

d = {'a': 10, 'b': 20, 'c': 30}
d.pop('z', -1)
# -1
d
# {'a': 10, 'b': 20, 'c': 30}
# ------------------------------------------------------------
# d.popitem()
# Removes a key-value pair from a dictionary.

d = {'a': 10, 'b': 20, 'c': 30}

d.popitem()
# ('c', 30)
d
# {'a': 10, 'b': 20}

d.popitem()
# ('b', 20)
d
# {'a': 10}

# If d is empty, d.popitem() raises a KeyError exception:
d = {}
d.popitem()
'''
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d.popitem()
KeyError: 'popitem(): dictionary is empty'
'''
# ------------------------------------------------------------
# d.update(<obj>)
# Merges a dictionary with another dictionary or with an iterable of key-value pairs.

'''
If <obj> is a dictionary, d.update(<obj>) merges the entries from <obj> into d. For each key in <obj>:

If the key is not present in d, the key-value pair from <obj> is added to d.
If the key is already present in d, the corresponding value in d for that key is updated to the value from <obj>.
'''

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}

d1.update(d2)
d1
# {'a': 10, 'b': 200, 'c': 30, 'd': 400}

d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update([('b', 200), ('d', 400)])
d1
# {'a': 10, 'b': 200, 'c': 30, 'd': 400}

d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update(b=200, d=400)
d1
# {'a': 10, 'b': 200, 'c': 30, 'd': 400}
# ------------------------------------------------------------

