
# python3 tuple.py

#? Tuples are similar to list except:
#? They are immutable and they have open-closed round brackets instead of square   
t = (1, 2, 3, 4)
print(t)
#o/p: (1, 2, 3, 4)
print(type(t))
#o/p: <class 'tuple'>

#? To create a singleton tuple, we need to write it as
t = (2, ) 
print(t)
#o/p: (2,)
print(type(t))
#o/p: <class 'tuple'>

#? if we just write (2) it will be considered as integer due to operator precedence since it will consider it as normal open close brackets which we use
#? while performing operations and not the tuple brackets
t = (2) 
print(t)
#o/p: 2
print(type(t))
#o/p: <class 'int'>


#* Packing and Unpacking of tuple 
#? It basically maps each element in tuple to a variable; Number of elements in tuple == Number of assignment variables else it throws an error
t = (24, 32, 9)
a, b, c = t
print(a,b,c)
#o/p: 24 32 9



