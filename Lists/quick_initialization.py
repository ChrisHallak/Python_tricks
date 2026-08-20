"""
    Multiple ways to create and initialize lists with default values.
"""

# Using repetition operator (*) to create a list with repeated elements
my_list = [0] * 5
print('my_list :', my_list)  # [0, 0, 0, 0, 0]

print('-' * 50)

# Using repetition on empty list (results in empty list)
empty_list = [] * 5
print('empty_list :', empty_list)  # []
print('Length of empty_list:', len(empty_list))  # 0

print('-' * 50)

# Using list comprehension to create a list
list2 = [0 for i in range(5)]
print('list2 :', list2)  # [0, 0, 0, 0, 0]
