
# python3 iterables.py

#? Iterables - A general python term for a sequential collection of objects

#+ str.join() 
# lists


a = ["spam", "ram", "cam", "ham", "dam"]
b = '/'.join(a)
print(f"options - {b}")
#o/p: options - spam/ram/cam/ham/dam


# strings
#? Strings are iterables too!
#? here string is considered as a list of characters
a = "SHIELD"
b = '.'.join(a)
print(f"Marvel - {b}")
#o/p: Marvel - S.H.I.E.L.D

#? elements in the list have to be of same datatype - string; If any other data type is found it returns an error 
# error_list = ["sachin", 10, "India"]
# print(' | '.join(error_list))
# #o/p: TypeError: sequence item 1: expected str instance, int found

print('------------------------------------------------------------')

#+ str.split() 
# .spilt() is opposite to .join() method
a = "#goofy#daily#sauce#like"
b = a.split('#')
print(b)
#o/p: ['', 'goofy', 'daily', 'sauce', 'like']

print('#'.join(b))
#o/p: #goofy#daily#sauce#like


print('------------------------------------------------------------')

#? converts the string to list 
b = a.split()
print(b)
#o/p: ['#goofy#daily#sauce#like']

print('------------------------------------------------------------')

#+ str.partition(<separator>): returns a tuple with 3 elements 
#? element 1: string before separator
#? element 2: the separator itself
#? element 3: whole string after separator
a = "#goofy#daily#sauce#like"
print(a.partition('#'))
#o/p: ('', '#', 'goofy#daily#sauce#like')

#? If separator is not found it will return a 3-tuple containing 2 empty strings and 1 OG string
print(a.partition('.'))
#o/p: ('#goofy#daily#sauce#like', '', '')

empty_str = ''
print(empty_str.partition('#'))
#o/p: ('', '', '')

just_separator = '.'
print(just_separator.partition('.'))
#o/p: ('', '.', '')



#+ str.rpartition(<separator>): similar to .partition() except it starts from right 
print(a.rpartition('#'))
#o/p: ('#goofy#daily#sauce', '#', 'like')










