# Sets in Python

'''
# A set is a collection of unique(no duplicates), unordered, unchangeable*, and unindexed elements.
# Sets are written with curly brackets {}.
# A set can contain different types of data, but it cannot contain mutable data types like lists or dictionaries.
# Sets are one of 4 built-in data types in Python used to store collections of data

'''
numbers = {1, 2, 3, 4, 5}
print(numbers)

# Duplicates 
my_set = {1, 2, 2, 3, 4, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

a = {1, 2, 3}
b = {3, 4, 5}
# Union
union_set = a.union(b)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_set = a.intersection(b)
print(intersection_set)  # Output: {3}

# Difference
difference_set = a.difference(b)
print(difference_set)  # Output: {1, 2}
difference_set_ba = b.difference(a)
print(difference_set_ba)  # Output: {4, 5}

# Symmetric Difference
sym_diff_set = a.symmetric_difference(b)    
print(sym_diff_set)  # Output: {1, 2, 4, 5}


