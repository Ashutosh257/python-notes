
# python3 list-methods.py  

#? String methods - return a new string object, leaving the original string unchanged.
#? while list methods modify the list itself and dont return a new list although there are some exceptions  


#+ .append(<obj>): adds an object at the end 
a = [1,2,3]
a.append(4)
print(a)
#o/p: [1, 2, 3, 4]

a.append(35.546)
print(a)
#o/p: [1, 2, 3, 4, 35.546]

#? concatenation will add the elements to the end of the list as well but it doesnt modify the OG list, it returns the modified list 
a = [1, 2, 3]
b = a + [4, 5, 6]
print(b)
#o/p: [1, 2, 3, 4, 5, 6]
print(a)
#o/p: [1, 2, 3]

#? append will not return anything 
#? when we append a list, it will add a sublist unlike concatenation; Since .append takes an object as a parameter and considers it as an object instead of individual elements 
a = [1, 2, 3]
a.append([4,5,6])
print(a)
#o/p: [1, 2, 3, [4, 5, 6]]

a = [1, 2, 3]
a.append("asb")
print(a)
#o/p: [[1, 2, 3, 'asb']


#+ .extend(<iterable>): adds elements from the iterable
# works like concatenation
a = [1, 2, 3]
a.extend([4,5,6])
print(a)
#o/p: [1, 2, 3, 4, 5, 6]

a = [1, 2, 3]
a.extend("abc")
print(a)
#o/p: [1, 2, 3, [4, 5, 6]]

a = [1, 2, 3]
a.extend(["abc"])
print(a)
#o/p: [1, 2, 3, 'abc']


#+ .insert(index, object): inserts the object at the given index
 
#+ .remove(object): removes the first occurrence of the object, if not present will raise ValueError
  
#+ .clear(): empty's the list; remove all elements 

#+ .sort([, <key=None> [, <reverse=True>]]): sorts the list
#+ key: to sort by
#+ reverse: true - ascending order, false - descending order  
a = ["spam", "bam", "ham", "scam", "dam", "Cam", "ram", "Fam"]
a.sort()
print(a)
#o/p: ['Cam', 'Fam', 'bam', 'dam', 'ham', 'ram', 'scam', 'spam']; sorts according to ASCII

#? we can add str.upper as a key to uniquely sort; here str is the actual str() and not a variable!
# eg: str.method_name() to sort 
a = ["spam", "bam", "ham", "scam", "dam", "Cam", "ram", "Fam"]
a.sort(key=str.upper)
print(a)
#o/p: ['bam', 'Cam', 'dam', 'Fam', 'ham', 'ram', 'scam', 'spam']

#! We cant sort elements of different data types, it throws TypeError
 
print('------------------------------------------------------------')

#+ .reverse(): flips the list 
a = [31, 22, 73, 4]
a.reverse()
print(a)
#o/p: [4, 73, 22, 31]

a = [31, 22, 73, 4]
print(a[::-1]) # same as .reverse(), but doesnt modify the OG list
#o/p: [4, 73, 22, 31]

a = ["spam", "bam", "ham", "scam", "dam", "Cam", "ram", "Fam"]
a.reverse()
print(a)
#o/p: ['Fam', 'ram', 'Cam', 'dam', 'scam', 'ham', 'bam', 'spam']


#+ .pop(<index=-1>): returns the item that is removed, by default removes the last element.
#+ .index(<obj> [, <start> [, <end>]]): return the index for first occurrence, if not found raises exception
#+ .count(): return number of occurrences










