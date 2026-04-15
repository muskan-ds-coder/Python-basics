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