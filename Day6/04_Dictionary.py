# Dictionary in Python
# A dictionary is a collection of key-value pairs.
# A dictionary store data in the form:
# key : value
# Like a real life dictionary:
# Word(key) : Meaning(value)

# Example
my_dict = {
    "name": "Sanoj",
    "age": 25,
    "marks": 85
}
print(my_dict["name"])  # Output: Sanoj
print(my_dict["age"])   # Output: 25    
print(my_dict["marks"]) # Output: 85

# Add / Update data
my_dict["age"] = 26  # Update age
my_dict["city"] = "Godda"  # Add new key-value pair
print(my_dict)  # Output: {'name': 'Sanoj', 'age': 26, 'marks': 85, 'city': 'Godda'}

# Remove data
del my_dict["marks"]  # Remove marks key-value pair
print(my_dict)  # Output: {'name': 'Sanoj', 'age': 26, 'city': 'Godda'}

# Create dictionary of numbers and their squares
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4} 

# Find max value in dictionary
max_value = max(squares.values())
print(max_value)  # Output: 25  
