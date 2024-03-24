
# python3 update_methods.py


#+ set1.update(set2, set3, ...): adds elements which dont exist in first set. Basically, Union with no duplication
#+ corresponding operator: x1 |= x2[ |= x3 ...]

#+ set1.intersection_update(set2, set3, ...): retains elements found in both sets
#+ corresponding operator: x1 &= x2[ &= x3 ...]


#+ set1.difference_update(set2, set3, ...): keeps elements that are in first set and not any other set
#+ corresponding operator: x1 -= x2[ | x3 ...]
#? The '|' operator takes union of all other sets apart from x1 and then performs a difference_update on the union of those sets
a = {1, 2, 3}
b = {2}
c = {3}
a -= b | c 
#? first (b U c) happens -> {2, 3} and then difference_update is done by a with (b U c): a -= {2, 3} --> {1}
print(a)


#+ set1.symmetric_difference_update(set2): keeps elements that are in single set and not any other set
#+ corresponding operator: x1 ^= x2[ ^ x3 ...] and this will mutate x1 to include all elements found in either any of the sets, but not in multiple sets.




















