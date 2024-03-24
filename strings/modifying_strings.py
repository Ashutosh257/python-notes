# python3 modifying_strings.py

# Strings are immutable
#? If we want to change content of the string we make a copy of it.
#? Changing the string directly will give an error 

a = "hello"
# a[2] = "s"
# print(a)
#o/p: TypeError: 'str' object does not support item assignment

s = "strings"
s = s[:2] + "w" + s[3:]
print(s)
#o/p: stwings

# we can also use the replace() function to replace the string
# eg: .replace(old_value, new_value), it returns a new object with the modified string
name = "John"
new_name = name.replace('h', 'w')
print(new_name)
#o/p: Jown

#+ It didn't modify the original string 
print(name)
#o/p: John

















