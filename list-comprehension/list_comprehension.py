
# python3 list_comprehension.py

#? Syntax
#? [expression for member in iterable]
a = [i**2 for i in range(10)]
print(a)
#o/p: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# list comprehensions are more pythonic!

#? Conditional syntax for comprehension
#? [expression for member in iterable (if conditional)]
a = "hello world to full of shit"
vowels = [v for v in a if v in "aeiou"]
print(vowels)
#o/p: ['e', 'o', 'o', 'o', 'u', 'o', 'i']


#? If want to change the member instead of filtering it out we use the following syntax
#? [expression (if conditional) for member in iterable]
# We wanna change -ve prices to 0 and dont chnage +ve prices

prices = [1.23, -34.3, 10.78, 25.15, -16.78, 5.16]
final_prices = [price if price > 0 else 0 for price in prices]
print(prices)
#o/p: [1.23, -34.3, 10.78, 25.15, -16.78, 5.16]
print(final_prices)
#o/p: [1.23, 0, 10.78, 25.15, 0, 5.16]


#+ We can also perform SET and DICT Comprehensions 

#* SET Comprehension
#? Its similar to list comprehension, it makes sure there are no duplicates
#? we use '{}' curly braces for set comprehension 
#? Unlike lists, sets don’t guarantee that items will be saved in any particular order.
a = "hello world to full of shit"
vowels = {v for v in a if v in "aeiou"}
print(vowels)
# o/p: {'i', 'o', 'u', 'e'}
print(type(vowels))
#o/p: <class 'set'>


#* DICT Comprehension
#? It is similar to list/set comprehension but there is an additional key required
#? {} curly braces are used
a = "hello world to full of shit"
vowels = {i+1:v for i, v in enumerate(a) if v in "aeiou"}
print(vowels)
# o/p: {2: 'e', 5: 'o', 8: 'o', 14: 'o', 17: 'u', 21: 'o', 26: 'i'}
print(type(vowels))
#o/p: <class 'dict'>


#* WALRUS Operator

import random
def get_weather():
    return random.randrange(90, 110)

#! here we need to save the data coming from get_weather and append to the list
#! the following cant be achieved 
# hot_temps = [ for _ in range(20) if (get_weather()) >= 100 ]

#? thats when walrus operator come handy
#? they allow you to run an expression while simultaneously assigning the output value to a variable.   
hot_temps = [ temp  for _ in range(20) if (temp := get_weather()) >= 100 ]
print(hot_temps)
#o/p: [108, 107, 102, 103, 109, 100, 103, 102, 101, 105, 103, 100]
print(len(hot_temps))
#o/p: 12


#* WHEN NOT TO USE COMPREHENSION 
#?  Look out for nested comprehensions
#? Use generators for large datasets












