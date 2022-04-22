remove_duplicates_from_list.py

# Source -- https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/

# Method 1 : Naive method

# Python 3 code to demonstrate 
# removing duplicated from list 
# using naive methods 
  
# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(test_list))

# using naive method
# to remove duplicated 
# from list 
res = []
for i in test_list:
    if i not in res:
        res.append(i)

# printing list after removal 
print ("The list after removing duplicates : " + str(res))

"""
Output
The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
The list after removing duplicates : [1, 3, 5, 6]
"""

# Method 2 : Using list comprehension

# Python 3 code to demonstrate 
# removing duplicated from list 
# using list comprehension
  
# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(test_list))
  
# using list comprehension
# to remove duplicated 
# from list 
res = []
[res.append(x) for x in test_list if x not in res]
  
# printing list after removal 
print ("The list after removing duplicates : " + str(res))

"""
output
The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
The list after removing duplicates : [1, 3, 5, 6]
"""

# Method 3 : Using set()

# Python 3 code to demonstrate 
# removing duplicated from list 
# using set()
  
# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(test_list))
  
# using set()
# to remove duplicated 
# from list 
test_list = list(set(test_list))
  
# printing list after removal 
# distorted ordering
print ("The list after removing duplicates : " + str(test_list))

"""
Output
The original list is : [1, 5, 3, 6, 3, 5, 6, 1]
The list after removing duplicates : [1, 3, 5, 6]
"""

# Method 4 : Using list comprehension + enumerate()

# Python 3 code to demonstrate 
# removing duplicated from list 
# using list comprehension + enumerate()
  
# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(test_list))
  
# using list comprehension + enumerate()
# to remove duplicated 
# from list 
res = [i for n, i in enumerate(test_list) if i not in test_list[:n]]
  
# printing list after removal 
print ("The list after removing duplicates : " + str(res))

"""
Output
The original list is : [1, 5, 3, 6, 3, 5, 6, 1]
The list after removing duplicates : [1, 5, 3, 6]
"""

# Method 5 : Using collections.OrderedDict.fromkeys()

# Python 3 code to demonstrate 
# removing duplicated from list 
# using collections.OrderedDict.fromkeys()
from collections import OrderedDict
  
# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(test_list))
  
# using collections.OrderedDict.fromkeys()
# to remove duplicated 
# from list 
res = list(OrderedDict.fromkeys(test_list))
  
# printing list after removal 
print ("The list after removing duplicates : " + str(res))

"""
Output
The original list is : [1, 5, 3, 6, 3, 5, 6, 1]
The list after removing duplicates : [1, 5, 3, 6]
"""

