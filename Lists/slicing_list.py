"""
    This file shows the methods of slicing lists
"""

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('my_list :', my_list)
print('-' * 50)

# Full range (copy of entire list)
print('my_list[0:10]   :', my_list[0:10])
print('my_list[:]      :', my_list[:])  # Shorter way for full copy

# Specific range (from index 2 to 4, stop is exclusive)
print('my_list[2:5]    :', my_list[2:5])

# Omitting stop (from index 2 to the end)
print('my_list[2:]     :', my_list[2:])

# Omitting start (from beginning to index 4, stop is exclusive)
print('my_list[:5]     :', my_list[:5])

# Step slicing (step = 1 is default)
print('my_list[0:10:1] :', my_list[0:10:1])
print('my_list[0:10:2] :', my_list[0:10:2])  # Every second element
print('my_list[::2]    :', my_list[::2])  # Shorter way for step 2

# Negative indexing (counts from the end, -1 is last element)
print('my_list[-5:]    :', my_list[-5:])  # Last 5 elements
print('my_list[:-5]    :', my_list[:-5])  # All except last 5
print('my_list[-5:-2]  :', my_list[-5:-2])  # From index -5 to -3

# Reversing a list using negative step
print('my_list[::-1]   :', my_list[::-1])  # Reverse the entire list
print('my_list[::-2]   :', my_list[::-2])  # Reverse with step 2
