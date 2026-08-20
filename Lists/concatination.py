"""
LIST CONCATENATION USING THE + OPERATOR
========================================
The + operator creates a NEW list by combining two existing lists.
- Original lists remain unchanged
- Returns a new list containing elements from both lists
- Order is preserved: first list's elements, then second list's
"""

list1 = [1,2,3]

list2 = ['Chris','Hallak']

concat_list = list1 + list2

print('concatenation of ',list1 , 'and' , list2,':\n',concat_list)