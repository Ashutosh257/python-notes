
# python3 functional_programming.py

#! Are Lambdas Pythonic or Not?
#! PEP 8, which is the style guide for Python code, reads:
    #! Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier.
#! This strongly discourages using lambda bound to an identifier, mainly where functions should be used and have more benefits. 
#! PEP 8 does not mention other usages of lambda. As you have seen in the previous sections, lambda functions may certainly have good uses, although they are limited.
#! A possible way to answer the question is that lambda functions are perfectly Pythonic if there is nothing more Pythonic available. 
#! I’m staying away from defining what “Pythonic” means, leaving you with the definition that best suits your mindset, as well as your personal or your team’s coding style. 

#* LAMBDA 

# Syntax
#? lambda <parameter_list>: <expression> 
v = lambda x: x**2
print(v(2))
#o/p: 4

#? It’s not necessary to assign a variable to a lambda expression before calling it. You can also call the function defined by a lambda expression directly 
print((lambda s: s[::-1])("I am a string"))
#o/p: gnirts a ma I

#? A lambda expression can’t contain statements like assignment or return, nor can it contain control structures such as for, while, if, else, or def. 

#? if you find a need to include a lambda expression in a formatted string literal (f-string), then you’ll need to enclose it in explicit parentheses
print(f"--- {(lambda s: s[::-1])} ---")
#o/p: --- <function <lambda> at 0x10037a830> ---



#* MAP
"+".join(map(str, [1, 2, 3, 4, 5]))
#o/p: 1+2+3+4+5

#? Although map() accomplishes the desired effect in the above example, 
#? it would be more Pythonic to use a list comprehension to replace the explicit loop in a case like this.
print('+'.join([str(i) for i in [1,2,3,4,5]]))
#o/p: 1+2+3+4+5

#? There’s another form of map() that takes more than one iterable argument:
#? map(<f>, <iterable1>, <iterable2>, ..., <iterablen>) applies <f> to the elements in each <iterablei> in parallel and returns an iterator that yields the results.
#? The number of <iterablei> arguments specified to map() must match the number of arguments that <f> expects. 
#? <f> acts on the first item of each <iterablei>, and that result becomes the first item that the return iterator yields. 
#? Then <f> acts on the second item in each <iterablei>, and that becomes the second yielded item, and so on.  
# eg shown below:
def f(a, b, c):
    return a + b + c

ans = list(map(f, [1, 2, 3], [10, 20, 30], [100, 200, 300]))
print(ans)
#o/p: [111, 222, 333]



#* FILTER
 
#? filter(<f>, <iterable>) applies function <f> to each element of <iterable> and returns an iterator that yields all items for which <f> is truthy. 
#? Conversely, it filters out all items for which <f> is falsy.
# here we filter out elements greater than 100
print(list(filter(lambda x: x > 100, [1, 111, 2, 222, 3, 333])))
#o/p: [111, 222, 333]

# here we filter out elements that are even
print(list(filter(lambda x: x % 2 == 0, [1, 111, 2, 222, 3, 333])))
#o/p: [2, 222]

print(list(filter(lambda x: x.isupper(), ["cat", "Cat", "CAT", "dog", "Dog", "DOG", "emu", "Emu", "EMU"])))
#o/p: ['CAT', 'DOG', 'EMU']



