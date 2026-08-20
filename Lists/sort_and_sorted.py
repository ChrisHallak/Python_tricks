"""
DIFFERENCE BETWEEN sort() AND sorted()
=======================================
- sort()  : List method, modifies original list, returns None
- sorted(): Built-in function, creates new sorted list, original unchanged
"""

# 1. sort() method - modifies the original list
my_list = [8, 3, 1]
print('my_list before sort()    :', my_list)
my_list.sort()
print('my_list after sort()     :', my_list)  # Original list is modified

print('-' * 50)

# 2. sorted() function - returns a new sorted list, original unchanged
my_list = [8, 3, 1]
print('my_list before sorted()  :', my_list)
new_list = sorted(my_list)  # Store the returned sorted list
print('my_list after sorted()   :', my_list)  # Original remains unchanged
print('new_list (sorted copy)   :', new_list)  # New sorted list
