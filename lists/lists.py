
# python3 lists.py

import math


#* INTRO
# lists are declared using []
my_list = [1,2,3,4,5,6]

#? [1,2,3] is not eqvivalent to [2,3,1]. to equate lists order is important
print([1,2,3] == [2,3,1])
#o/p: False
print([1,2,3] == [1,2,3])
#o/p: True


def foo():
    print("foo")

#? everything in python is an object
# we can have diff data types in single list including functions, classes and modules too!
different_types_list = [1, 3.24, "abc", foo, math]
#o/p: [1, 3.24, 'abc', <function foo at 0x104b527a0>, <module 'math' from '/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload/math.cpython-310-darwin.so'>]

print(different_types_list)

print('------------------------------------------------------------')


#* INDEXING 
# index in python lists starts from 0. 
# they are mutable meaning values of elements in the list can be added or changed.
 
#? We access elements in list using indexes
#eg: my_list[m] where m is an index that can be an integer.
print(my_list[0])
#o/p: 1
print(my_list[4])
#o/p: 5
print(my_list[len(my_list)-1])
#o/p: 6

# If we give an index greater than the length of the list, it will return an error
# print(my_list[9])
#o/p: IndexError: list index out of range

print('------------------------------------------------------------')

#? we can also use negative indexes. negative index points to the last element and traveses in reverse order as we decrese the integer i.e tends towards -x
print(my_list[-1])
#o/p: 6
print(my_list[-4])
#o/p: 5
print(my_list[-len(my_list)])
#o/p: 6

# Again if we provide an index bigger than the length it will return an error. 
# print(my_list[-9])
#o/p: IndexError: list index out of range


#* SLICING
#? we can provide a sublist of the actual list using slicing  
#eg: my_list[m:n] -- starts from position 'm' and ends at position 'n-1'. It doesn't include my_list[n] in the sublist {m,n} are integers
print(my_list[2:5])

print(my_list[-5:-2])

#? We can also omit the index while slicing. 
#eg: my_list[:n], omiting m - starts the slice at the beginning of the list : (0 to n-1 element)
#eg: my_list[m:], omitting n - extends the slice till the end of the list : (m to last index element)
#eg: my_list[:], omitting both m,n - makes a copy of the list : (all elements)
  

#? basically omitting any index makes the slice "greedy in nature" and it will try to take max amount of elements in the list.        
print(my_list[:4])
#o/p: [1, 2, 3, 4]

print(my_list[4:])
#o/p: [5, 6]

print(my_list[:])
#o/p: [1, 2, 3, 4, 5, 6]
#? Unlike strings its a copy, and not a reference to the same object


#? strings copy reference not values
# todo: you can uncomment and try 
# a = "snd"
# b = a
# print(f"a : {a}, b: {b} ")
# print(f"id(a): {id(a)}")  
# print(f"id(b): {id(b)}")

#? id() function is used to fetch the memory address of the object
new_list = my_list[:]
print(f"id(my_list): {id(my_list)}")
print(f"id(new_list): {id(new_list)}")


#+ There is an additional index called as step/stride
#+ my_list[a:b:c] - c is like a step parameter. So, in a sublist of range a to b-1, the value of 'c' signifies by which it will increment to the next index. 
print(my_list[1:6:2])
#o/p: [2,4,6]

#? step can be negative as well 
print(my_list[6:1:-2])
#o/p: [6,4]

#? reverses the list 
print(my_list[::-1])

