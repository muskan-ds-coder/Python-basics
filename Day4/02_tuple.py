# Tuple in Python

# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Tuples are defined by enclosing elements in parentheses () and separating them with commas.
# Tuples are one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# Tuples can contain different types of data
mixed_tuple = (1, "Hello", 3.14, True)
print(mixed_tuple)
# Tuples can also contain other tuples (nested tuples)
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple)
# Example
friends = ("Apple", "orange", 5, 344.05, "Muskan", "grapes")
print(friends)
# Tuples are immutable, which means you cannot change the elements of a tuple after it has been created. However, you can perform operations that create new tuples based on existing ones.

# Example
# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)
# Repetition
repeated_tuple = tuple1 * 3
print(repeated_tuple)
# Length of a tuple
print(len(tuple1))



a = () # empty tuple
print(type(a))  # This will print <class 'tuple'>

b = (1, 2, 3, 4, 5)
print(type(b))

c = (1)
print(type(c))  # This will print <class 'int'> because it's not a tuple, it's just an integer.

d = (1,)  # This is a tuple with one element. The comma is necessary to indicate that it's a tuple.
print(type(d)) # This will print <class 'tuple'> because the comma indicates that it's a tuple, even though it has only one element.

e = (1, 23, 45, 445, 5443, False, "Muskan", "Sanoj", 3.14)
print(e)
print(type(e))  # This will print <class 'tuple'> because it's a tuple with multiple elements of different types.
# e[0] = 10  # This will raise a TypeError because tuples are immutable and cannot be changed after they are created.

# Tuples can be indexed and sliced just like lists, but they cannot be modified.

print(friends[0])  # This will print "Apple"