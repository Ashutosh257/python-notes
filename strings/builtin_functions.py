# python3 builtin_functions.py

#?    Function      Description
#?    chr()	        Converts an integer to a character 
#?    ord()	        Converts a character to an integer
#?    len()	        Returns the length of a string
#?    str()	        Returns a string representation of an object


#+ chr(): returns one character string for an unicode
print(chr(65))
#o/p: A
print(type(chr(65)))
#o/p: <class 'str'>

print('------------------------------------------------------------')

#+ ord(): returns the unicode for a one character string
print(ord('a'))
#o/p: 97
print(type(ord('a')))
#o/p: <class 'int'>


#? We get an error if a string is passed instead of 1 character 
# print(ord('abs'))
#o/p: TypeError: ord() expected a character, but string of length 3 found

print('------------------------------------------------------------')

#+ len(): Returns the length of a string
s = "hello world, apples"
print(len(s))
#o/p: 19

print('------------------------------------------------------------')


#+ str(): converts other types to string type 
# float to str 
float_variable = 43.23
str_float_variable = str(float_variable)
print(str_float_variable)
#o/p: 43.23
print(type(str_float_variable))
#o/p: <class 'str'>


# int to str 
integer_variable = 12
str_integer_variable = str(integer_variable)
print(str_integer_variable)
#o/p: 12
print(type(str_integer_variable))
#o/p: <class 'str'>


# boolean to str 
boolean_variable = True
str_boolean_variable = str(boolean_variable)
print(str_boolean_variable)
#o/p: True
print(type(str_boolean_variable))
#o/p: <class 'str'>