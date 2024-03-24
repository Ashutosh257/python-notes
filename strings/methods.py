

# python3 methods.py

#? Methods vs Functions: Methods are special type of functions that are called by objects.
#? Method is invoked by an object and has knowledge of its target object during execution
# eg: object.function_name(<args>) -> method while function_name(<args>) -> function


#- Will discuss only commonly used methods
#* CASE CONVERSION METHODS 

#+ string.capitalize(): converts all the chracters to lowercase except the first character of the string
s = "hello WoRLd OFFICE"
a = s.capitalize()
print(f"{s} --capitalize()--> {a}")
#o/p: Hello world office

#? It doesn't affect numbers or special characters
num_and_special = "abc123^*&" 
print(num_and_special.capitalize())
#o/p: Abc123^*&

#+ string.lower(): returns a copy of the OG string that converts all characters to lower case
s = "abcakHAD"
a = s.lower()
print(f"{s} --lower()--> {a}")
#o/p: abcakhad

#+ string.upper(): returns a copy of the OG string that converts all characters to upper case
s = "abcakHAD"
a = s.upper()
print(f"{s} --upper()--> {a}")
#o/p: ABCAKHAD


#+ string.swapcase(): returns a copy of the OG string that converts lower case characters to upper case and vice versa
s = "abcakHAD"
a = s.swapcase()
print(f"{s} --swapcase()--> {a}")
#o/p: ABCAKHAD


#+ string.title(): returns a copy of the OG string that converts every first character of the word to upper case
s = "henLo pArk oF nEw YoRk"
a = s.title()
print(f"{s} --title()--> {a}")
#o/p: Henlo Park Of New York

#? It doesn't work well when the stings get complex like having apostrophe or abbreviations
s = "rabbit's foot in USA"
a = s.title()
print(f"{s} --title()--> {a}")
#o/p: Rabbit'S Foot In Usa


#* FIND AND SEEK METHODS

#? Each method in this group supports optional <start> and <end> arguments. 
#? These are interpreted as for string slicing: the action of the method is restricted to the portion of the target string 
#? starting at character position <start> and proceeding up to but not including character position <end>. 
#? If <start> is specified but <end> is not, then the method applies to the portion of the target string from <start> through the end of the string. 

#+ string.count(): returns the count of occurrence of the substring in the string.
s = "hello WoRLd OFFICE"
print(s.count('o',6,15)) #? It will not count 'O' as it is not same as 'o'
#o/p: 1

print('------------------------------------------------------------')

#+ string.endswith(): returns boolean value if the string ends with the substring specified.
s = "hello bello OFFICE"
print(s.endswith('o',6,11)) #? It ends at o in bello.
#o/p: True 
print(s.endswith('llo',6,11)) #? It ends at o in bello.
#o/p: True 
print(s.endswith('o',6,15)) #? It ends at 
#o/p: False

print('------------------------------------------------------------')

#+ string.startswith(): similar to endswith()
s = "hello bello OFFICE"
print(s.startswith('b',6,11)) #? It ends at o in bello.
#o/p: True 
print(s.startswith('bell',6,11)) #? It ends at o in bello.
#o/p: True 
print(s.startswith('hell',6,15)) #? It ends at 
#o/p: False

print('------------------------------------------------------------')


#+ string.find() will find the substring in the string. 
#+ If found it will return the lowest index where the substring is found else return -1
s = "bam jam rm cam"  
print(s.find('am'))
#o/p: 1
print(s.find('am', 5))
#o/p: 5
print(s.find('am', 9, 17)) #? it doesnt give error if i send the 'end' value greater than the length of the string
#o/p: 12

print('------------------------------------------------------------')

#+ string.rfind() is similar to find() but starts search from the right and returns the highest index when the substring is found else -1.
s = 'spam bacon spam spam egg spam'
print(s.find('spam'))
#o/p: 0
print(s.rfind('spam'))
#o/p: 25

print(s.rfind('spam', 8, 15))
#o/p: 11
print(s.rfind('spam', 8, 10))
#o/p: -1

print('------------------------------------------------------------')


#+ string.index() is similar to .find() the only difference is if the substring is not found then it returns an error instead of -1 unlike .find() 
s = 'spam bacon spam spam egg spam'
print(s.index('spam'))
#o/p: 0

print(s.index('spam', 8, 15))
#o/p: 11
# print(s.index('spam', 8, 10))
#o/p: ValueError: substring not found

print('------------------------------------------------------------')


#+ string.rindex() is similar to rfind() the only difference is if the substring is not found then it returns an error instead of -1 unlike .rfind()
s = 'spam bacon spam spam egg spam'
print(s.rindex('spam'))
#o/p: 25

print(s.rindex('spam', 8, 15))
#o/p: 11
# print(s.rindex('spam', 8, 10))
#o/p: ValueError: substring not found

print('------------------------------------------------------------')




#* CHARACTER CLASSIFICATION

#+ str.isalnum(): returns True if string is non-empty, no special characters and has only alphanumeric characters!

s = "gas89"
print(s.isalnum())
s = ""
print(s.isalnum())
s = "uvg7("
print(s.isalnum())





