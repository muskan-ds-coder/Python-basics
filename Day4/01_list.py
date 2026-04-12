# List in Python

# Lists are used to store multiple items in a single variable. 
# Lists are one of the most versatile data structures in Python and can contain elements of different types, including other lists. 
# Lists are ordered, changeable, and allow duplicate values.
# Lists are defined by enclosing elements in square brackets [] and separating them with commas.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets: []
# Example
my_list = [1, 2, 3, 4, 5]
print(my_list)  

# Lists can contain different types of data
mixed_list = [1, "Hello", 3.14, True]
print(mixed_list)

# Lists can also contain other lists (nested lists)
nested_list = [1, 2, 3, [4, 5], 6]
print(nested_list[3][0])


# Example
friends = [ "Apple", "orange", 5, 344.05, "Muskan", "grapes"]
print(friends)

friends.append("banana")  # Adding an element to the end of the list
print(friends)

friends.insert(2, "kiwi")  # Adding an element at a specific index
print(friends)

friends.remove("kiwi")  # Removing an element from the list 
print(friends)

friends.reverse()  # Reversing the order of the list
print(friends)

print(friends.pop(2))  # Removing and returning an element at a specific index
value = friends.pop(2)
print(value)  
friends.pop(2)  # Removing an element at a specific index
print(friends)
friends.pop()  # Removing the last element from the list    
print(friends)

# 11 = [1, 23, 45, 2, 8, 5]
# 11.sort()  # Sorting the list in ascending order
# print(11)



