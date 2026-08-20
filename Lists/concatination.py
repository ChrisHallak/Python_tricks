"""
LIST CONCATENATION USING THE + OPERATOR
========================================
The + operator creates a NEW list by combining two existing lists.
- Original lists remain unchanged
- Returns a new list containing elements from both lists
- Order is preserved: first list's elements, then second list's
"""

list1 = [1, 2, 3]
list2 = ['Chris', 'Hallak']

# Concatenating two lists using + operator
concat_list = list1 + list2

print('Concatenation of', list1, 'and', list2, ':\n', concat_list)
print('-' * 50)

# Verify original lists remain unchanged
print('Original list1:', list1)
print('Original list2:', list2)
