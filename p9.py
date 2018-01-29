''' 9. To demonstrate use of Dictionary & related functions '''

# The dictionary is Python’s built-in mapping type. Dictionaries map keys to values and these key-value
# pairs provide a useful way to store data in Python. 
# Typically used to hold data that are related, such as the information contained in an ID 
# or a user profile, dictionaries are constructed with curly braces on either side { }.

# Dictionary looks like this: 

unesco = {'username': 'unesco.org', 'online': True, 'followers': 454323}

# In addition to the curly braces, there are also colons (:) throughout the dictionary.
# The words on the left side are the Keys, which are of immutable data type,
# the keys in above example are:
# username, online and followers

# The words on the right of the colon are Values, which can be on any data types, here we have
# unersco.org -> string
# online -> Boolean
# followers -> interger

''' x ------------------ x -------------------- x '''

# Accessing dictionary elements

print(unesco['username'])       # output: unesco.org
print(unesco['online'])         # output: True
print(unesco['followers'])      # output: 454323

''' x ------------------ x -------------------- x '''

# using functions to access elements

dict.keys()                # isolates keys
dict.values()              # isolates values
dict.items()               # returns items in a list format of (key, value) tuple pairs

print(unesco.keys())       # prints all the keys in unesco dictionary

''' x ------------------ x -------------------- x '''

# Modifying Dictionaries

# Adding elements to dictionary

fruit = {'mango': 'yellow', 'apple': 'red'}

fruit['grapes'] = 'green'       # adds grapes as a key and green as a value to fruit dictionary
print(fruit)                    # 'mango': 'yellow', 'apple': 'red', 'grapes': 'green'


# Deleting dictionary elements

del fruit['apple']      # delete apple element

fruit.clear()           # clear all the elements of dictionary

del fruit               # delete entire fruit dictionary
