# Tuple in Python
# A tuple is a collection of items that is: 
# 1. Ordered: The items have a defined order, and that order will not change.
# 2. Immutable: Once a tuple is created, you cannot change its content (add, remove, or modify items).
# 3. Allows duplicate values: Since tuples are indexed, they can have items with the same value.
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# Accessing tuple items
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3

# Slicing a tuple
print(my_tuple[1:4])  # Output: (2, 3, 4)

# Tuple with different data types
mixed_tuple = (1, "Hello", 3.14, [1, 2, 3])
print(mixed_tuple)  # Output: (1, 'Hello', 3.14, [1, 2, 3])

# Tuple unpacking
a, b, c, d = mixed_tuple    
print(a)  # Output: 1
print(b)  # Output: Hello
print(c)  # Output: 3.14
print(d)  # Output: [1, 2, 3]

# Tuple methods
# count() - Returns the number of times a specified value appears in the tuple
print(my_tuple.count(2))  # Output: 1
# index() - Searches the tuple for a specified value and returns the position of where it was found
print(my_tuple.index(3))  # Output: 2

# Note: Since tuples are immutable, they do not have methods like append(), remove(), or clear() that lists have.

