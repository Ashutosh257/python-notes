
# python3 operators.py


#* OPERATORS

#? The + operator, also known as the concatenation operator
s = "spam"
e = "egg"

print(s+e)
#o/p: spamegg

#? The * operator, also known as the replication operator. It will replicate the string 'n' times and concatenate it. 
#eg: "abc" * n, where n should be integer, it cant be any other type
n = 2
print(s*n)
#o/p: spamspam

#! will throw error
# print(s*1.2)
#o/p: TypeError: can't multiply sequence by non-int of type 'float'

#+ What if we try -ve numbers, it will return an empty string. For zero as well
print(s*-3)
#o/p: ""
print(s*0)
#o/p: ""

#* MEMBERSHIP OPERATOR - (in)
#? It’s going to return True if the first operand is present within the second, and it’ll return False if not
print("hero" in "superhero")
#o/p: True

#+ The match should be exact 
print("hero" in "superHero")
#o/p: False

#? We also use the 'not in' operator, which is a negation of 'in'
print("hero" not in "superhero")
#o/p: False

print("hero" not in "superHero")
#o/p: True
