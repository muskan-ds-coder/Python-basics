# String is a data type in python.
# String is a sequence of characters enclosed in quotes.
# We can primarily write a string in these three ways.
# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello".
# You can display a string literal with the print() function:
# ExampleGet your own Python Server
print("Hello")
print('Hello')

# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
# Example
print("It's alright")
print("He is called 'Muskan'")
print('He is called "Muskan"')
a = 'Muskan'      # Single quoted string 
b = "Muskan"      # Double quoted string   
c = '''Muskan'''  # Triple quoted string 

# STRING SLICING
# A string in python can be sliced for getting a part of the strings.
# Consider the following string:


name = "Muskan"
nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)
print(nameshort)
character1 = name[1]
print(character1)  # the index in a string starts from 0 to (length - 1) in python. In order to slice a string, we use the following syntax:


#NEGATIVE SLICING 
name = "Muskan"
print(name[0:4])

a = 5
b = 2
c = a + b
d = a - b
print(c)
print(d)
print(c * d)

# String Concatenation
# String concatenation is the operation of joining two or more strings together. In Python, you can concatenate strings using the + operator. When you use the + operator with strings, it combines them into a single string.
# Example
first_name = "Muskan"
last_name = "Kumari"
full_name = first_name + " " + last_name
print(full_name)

# String Repetition
# String repetition is the operation of repeating a string a specified number of times. In Python, you can repeat a string using the * operator. When you use the * operator with a string and an integer, it creates a new string that is the original string repeated the specified number of times.
# Example
word = "Hello"
repeated_word = word * 3
print(repeated_word)

# Example
print("Hello " * 3)

# String Length
print(len("Hello World"))



