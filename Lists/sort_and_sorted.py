"""
DIFFERENCE BETWEEN sort() AND sorted()
=======================================
- sort()  : List method, modifies original list, returns None
- sorted(): Built-in function, creates new sorted list, original unchanged
"""

# 1. sort
my_list = [8,3,1]
print('my list before applying sort method : ',my_list)
my_list.sort()
print('my list after applying sort method : ',my_list)

print('-'*50)
# 2.sorted
my_list = [8,3,1]
print('my list before applying sorted function : ',my_list)
sorted(my_list)
print('my list after applying sorted function : ',my_list)

