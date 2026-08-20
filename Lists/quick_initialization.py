"""
LIST INITIALIZATION TECHNIQUES IN PYTHON
========================================
Multiple ways to create and initialize lists with default values.
"""

my_list = [0] * 5

print('my_list :', my_list)

print('-' * 50)
# ------------------------------

empty_list = [] * 5

print('empy list :', empty_list)
print('Length of empty_list: ', len(empty_list))

print('-' * 50)
# ------------------------------

list2 = [0 for i in range(5)]
print('list2 :',list2)
