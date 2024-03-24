
# python3 mutable.py

#+ Python Lists: 
#+ Lists are mutable. They can be modified, after creation as well, order of elements can be changed, etc
#+ Elements can be added/deleted as well

#? In strings, you can make a change and reassign to the same object but it will throw error if we try to assign or change any value 
s = "asdkd"
print(s + "-asd")
#o/p: asdkd-asd
# s[2] = "f"
# print(s)
#o/p: TypeError: 'str' object does not support item assignment

#? In lists, you can make changes and reassign as well 
a = ["spam", "ram", "cam", "ham", "dam"]
# print(a + "ds")
#o/p: TypeError: can only concatenate list (not "str") to list
print(a + ["ds"])
#o/p: ['spam', 'ram', 'cam', 'ham', 'dam', 'ds']

a[3] = "fam" 
print(a)
#o/p: ['spam', 'ram', 'cam', 'fam', 'dam']; a[3]:ham -> a[3]:fam

print('------------------------------------------------------------')

#! IMPORTANT 
#?  If you wanted to change several contiguous elements in a list all at one time, instead of just index assignment, you could do it with slice assignment. 
#? Here you’ll put in m being your first index, and n being again going up to but not including. 
# eg: a[m:b] = <iterable>

a = ["spam", "ram", "cam", "ham", "dam"]
a[2:5] = [1.2, 3, True]
print(a)
#o/p: ['spam', 'ram', 1.2, 3, True]

#? when 1 list element is assigned to a sliced list then all contiguous elements under the slice are replaced by that single list element 
a = ["spam", "ram", "cam", "ham", "dam"] # len - 5
a[3:6] = ["hello"]
print(a)
#o/p: ['spam', 'ram', 'cam', 'hello'] ; len - 4

#- we can also assign more than 1 element to a slice index 
a = ["spam", "ram", "cam", "ham", "dam"] # len - 5
a[1:2] = ['a', 'b', 'c', 'd']
print(a)
#o/p: ['spam', 'a', 'b', 'c', 'd', 'cam', 'ham', 'dam']

#? If we dont use slice, then the list will be assigned as a sublist
a = ["spam", "ram", "cam", "ham", "dam"] # len - 5
a[1] = [22, 33, 44]
print(a)
#o/p: ['spam', [22, 33, 44], 'cam', 'ham', 'dam']

# If we want the above list to be added as simple list
a = ["spam", "ram", "cam", "ham", "dam"] # len - 5
a[1:1] = [22, 33, 44]
print(a)
#o/p: ['spam', 22, 33, 44, 'ram', 'cam', 'ham', 'dam']
# to remove/delete it: assign it to empty list 
a[1:4] = []
print(a)
#o/p: ['spam', 'ram', 'cam', 'ham', 'dam']

print('------------------------------------------------------------')

#* Adding items to list 
a = ["spam", "ram", "cam", "ham", "dam"] # len - 5
# append: add to end
a += ["fam", "bam", "scam"]
print(a)
#o/p: ['spam', 'ram', 'cam', 'ham', 'dam', 'fam', 'bam', 'scam']
# prepend: add to the start
a = [10,20] + a
print(a)
#o/p: [10, 20, 'spam', 'ram', 'cam', 'ham', 'dam', 'fam', 'bam', 'scam']

#? What if we add integers/float, it throws an error: object not iterable 
# a += 12
# print(a)
#o/p: TypeError: 'int' object is not iterable

#? string is an iterable, lets try adding string; 
#? for string it breaks the string and add as individual characters 
a = ["xyz", "ijk", "lmn"]
a += "abc"
print(a)
#o/p: ['xyz', 'ijk', 'lmn', 'a', 'b', 'c']
# we need to add it as a list 
a += ["abc"]
print(a)
#o/p: ['xyz', 'ijk', 'lmn', 'abc']



