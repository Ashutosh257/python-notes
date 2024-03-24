
# python3 set.py

#?  Sets are unordered. The elements are unique, and duplicate elements are not allowed. 
#? Hashable objects are those which can call the __hash__() method
#? All Immutable objects are hashable but not all hashable objects are immutable
#? Sets can only include hashable objects 
#- Tuples/Strings/Integers/Boolean are all hashable objects
#- Lists/Dicts are not hashable objects


s = "ds"
print(s.__hash__())
#o/p: -3358968529879608100

#? Converting other types to set
l = set([1, 2, 3])
print(l)
#o/p: {1, 2, 3}

#? for dictionaries only keys are taken as sets 
d = set({"hell": "boy", "man": "bat"})
print(d)
#o/p: {'man', 'hell'}

#? for strings it will split the characters and remove the duplicates
s = set("jelly")
print(s)
#o/p: {'l', 'y', 'e', 'j'}


#* BUILT-IN Methods
#+ len() 
s = {'l', 'y', 'e', 'j', (4, 3)}
print(len(s))
#o/p: 5

#- Membership operator 
#+ <elem> in <iterable> | <elem> not in <iterable>
s = {'l', 'y', 'e', 'j', (4, 3)}
print('a' in s)
#o/p: False
print('e' in s)
#o/p: True
print('a' not in s)
#o/p: True
print('e' not in s)
#o/p: False
print(not 'e' in s)
#o/p: False

#! You cant slice/order SETS, since they are not ordered  


#+ set1.union(set2, set3, set4, ...): returns union of all sets
#? corresponding operator is '|';  x1 | x2 [| x3 ...]
a = {1, 2, 3} 
b = {4, 5} 
print(a.union(b))
#o/p: {1, 2, 3, 4, 5}



#+ set1.intersection(set2, set3, set4, ...): returns intersection of all sets
#? corresponding operator is '&';  x1 & x2 [& x3 ...]
a = {1, 2, 3} 
b = {1, 4, 5, 6} 
print(a.intersection(b))
#o/p: {1}


#+ set1.difference(set2, set3, set4, ...): returns the only elements which are present in the first set and not in any other set
#? The operation is evaluated from left to right
#? corresponding operator is '-';  x1 - x2 [- x3 ...]
a = {1, 2, 3} 
b = {1, 4, 5, 6, 7} 
c = {5, 6, 9} 
print(a.difference(b, c))
#o/p: {2, 3}
print(b.difference(a, c))
#o/p: {4, 7}
print(c - a - b)
#o/p: {9}


#+ set1.symmetric_difference(set2): returns the elements which are present in the set and not in any other set, basically complement of intersection
#? a.symmetric_difference(b): can only take 1 argument 
#? for multiple args: use a ^ b ^ c 
a = {1, 2, 3} 
b = {1, 4, 5, 6} 
c = {5, 6, 9} 
print(a.symmetric_difference(b))
#o/p: {2, 3, 4, 5, 6}
print(b ^ a ^ c)
#o/p: {2, 3, 4, 9}
print(c ^ a ^ b)
#o/p: {2, 3, 4, 9}



#+ set1.isdisjoint(set2): checks if the sets have anything in common
#? works with only 1 arg 
a = {1, 2, 3} 
b = {1, 4, 5, 6} 
print(a.isdisjoint(b))
#o/p: {1}


#+ set1.issubset(set2): checks if the set is subset of the other
#? corresponding operator is '<=';  x1 <= x2 [<= x3 ...]
a = {1, 2, 3} 
b = {1, 4, 5, 6} 
print(a.issubset(b))
#o/p: {1}



#* Modify set 
#+ .add(<elem>) elem should be hashable
x = {1, 2, 3}
x.add(4)
print(x)
#o/p: {1, 2, 3, 4}


#+ .remove(<elem>): elem should be present in the set else throws an error
x.remove(3)
print(x)
#o/p: {1, 2, 4}

# x.remove(6)
#o/p: KeyError: 6

#+ .discard(<elem>): removes elem and do nothing if the elem does not exist
x = {1, 2, 3, 4, 9}
x.discard(2)
print(x)
#o/p: {1, 3, 4, 9}

x.discard(11)
print(x)
#o/p: {1, 3, 4, 9}

#+ .pop(): removes and returns a random element from the set and raises error when called on an empty set
#+ .clear(): removes all the elements; no error thrown when called on empty set  











