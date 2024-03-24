import os


# path = '/'.join([os.getcwd(), 'tmp', 'text.py'])
# print(path)

# with open(path, 'r') as f:
#     print(f.read())


# x = lambda y: y * 2

# print(x([1,2,3]))


# a = "hello world to full of shit"
# vowels = [(i,v) for i, v in enumerate(a) if v in "aeiou"]
# print(vowels)
from copy import copy, deepcopy

a = [["abc"], "xyz", "uvw", ["klm"]]
b = copy(a)
c = deepcopy(a)

c[0][0] = "a"
c[1] = "x"

print(a)
print(b)
print(c)

b[0][0] = "b"

print(a)
print(b)
print(c)