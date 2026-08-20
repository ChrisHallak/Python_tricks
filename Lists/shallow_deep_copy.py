"""
DIFFERENCE BETWEEN SHALLOW AND DEEP COPYING LISTS
=================================================
- Assignment (=)        : Creates a reference (not a copy)
- Shallow copy          : Creates new list, but nested objects are referenced
- Deep copy             : Creates completely independent copy (requires copy module)
"""

# 1. Assignment (=) - Creates a reference, not a copy
print("1. ASSIGNMENT (=) - REFERENCE")
print("-" * 50)
original_list = [1, "Chris", '25']
copy_list = original_list  # This creates a reference, not a copy!

print('original_list before change:', original_list)
print('copy_list before change    :', copy_list)

print('-' * 50)
print('Adding new value to original list')
original_list.append('new value')
print('-' * 50)

print('original_list after change :', original_list)
print('copy_list after change     :', copy_list)  # Both change! (same object)
print("Both lists changed because they reference the SAME object")

print('\n' + '='*60 + '\n')

# 2. Shallow copy - Method 1: list() constructor
print("2. SHALLOW COPY - Method 1: list() constructor")
print("-" * 50)
original_list = [1, "Chris", '25']
copy_list = list(original_list)  # Shallow copy

print('original_list before change:', original_list)
print('copy_list before change    :', copy_list)

print('-' * 50)
print('Adding new value to original list')
original_list.append('new value')
print('-' * 50)

print('original_list after change :', original_list)
print('copy_list after change     :', copy_list)  # Only original changes
print("Only original changed - copy is independent")

print('\n' + '='*60 + '\n')

# 3. Shallow copy - Method 2: .copy() method
print("3. SHALLOW COPY - Method 2: .copy() method")
print("-" * 50)
original_list = [1, "Chris", '25']
copy_list = original_list.copy()  # Shallow copy

print('original_list before change:', original_list)
print('copy_list before change    :', copy_list)

print('-' * 50)
print('Adding new value to original list')
original_list.append('new value')
print('-' * 50)

print('original_list after change :', original_list)
print('copy_list after change     :', copy_list)  # Only original changes
print("Only original changed - copy is independent")

print('\n' + '='*60 + '\n')

# 4. Shallow copy - Method 3: List comprehension
print("4. SHALLOW COPY - Method 3: List comprehension")
print("-" * 50)
original_list = [1, "Chris", '25']
copy_list = [i for i in original_list]  # Shallow copy

print('original_list before change:', original_list)
print('copy_list before change    :', copy_list)

print('-' * 50)
print('Adding new value to original list')
original_list.append('new value')
print('-' * 50)

print('original_list after change :', original_list)
print('copy_list after change     :', copy_list)  # Only original changes
print("Only original changed - copy is independent")

print('\n' + '='*60 + '\n')

# 5. Deep copy - Using copy module
print("5. DEEP COPY - Using copy.deepcopy()")
print("-" * 50)
import copy

original_list = [1, "Chris", '25']
copy_list = copy.deepcopy(original_list)  # Deep copy

print('original_list before change:', original_list)
print('copy_list before change    :', copy_list)

print('-' * 50)
print('Adding new value to original list')
original_list.append('new value')
print('-' * 50)

print('original_list after change :', original_list)
print('copy_list after change     :', copy_list)  # Only original changes
print("Only original changed - deep copy is completely independent")

print('\n' + '='*60)
print("\nSUMMARY:")
print("-" * 50)
print("Assignment (=)     : Creates a REFERENCE (not a copy)")
print("Shallow copy       : Creates new list, but nested objects are shared")
print("Deep copy          : Creates completely independent copy")
print("\nFor nested lists, shallow copy still shares inner objects!")
print("Use copy.deepcopy() for completely independent nested structures")