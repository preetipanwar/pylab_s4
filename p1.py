'''1. Demonstrate the working of ‘id’ and ‘type’ functions'''

''' a)  id function ->
        The id() function is used rarely used, it tells about the unique identifier of an object
'''

number1 = 12
print("id of a: ")
print(id(number1))       # print the id

string1 = "hello"
print("\nid of b: ")
print(id(string1))       # print the id

''' b)  type function -> 
        The type() function is used
'''

print("\n")              # \n is used for new line
print('number1 is of type: ')
print(type(number1))

print("\n")              # \n is used for new line
print('string1 is of type: ')
print(type(string1))

''' Notice how we had to write 3 lines to print a value which can be written in one line.
    Lets bring them all on one line.
'''
# str() function converts our value in type to string so that it can be added to the string value
print("\n string1 is of type: " + str(type(string1)))
print("\n number1 is of type: " + str(type(number1)))
