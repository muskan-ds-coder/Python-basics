# Data types in Python

# 
# Data types tell the computer what kind of data a variable is stroing.
# Python has several built-in data types, including:
a = 10          # a is an integer (int)
b = 3.14        # b is a floating-point number (float)
c = "Hello"     # c is a string (str)
d = True        # d is a boolean (bool)
e = None        # e is a NoneType (NoneType)
f = 1 + 2j      # f is a complex number (complex)
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>
print(type(e))  # <class 'NoneType'>
print(type(f))  # <class 'complex'>

# Number
x = 5           # integer
y = 3.14        # float
z = 1 + 2j      # complex
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

# Casting
x = int(3)      # x will be 3
y = float(3)    # y will be 3.0
z = str(3)      # z will be '3'
print(x)        # 3
print(y)        # 3.0
print(z)        # '3'

# Python Strings
#You can use double or single quotes:
print("Hello")
print('Hello')

# Slicing Strings
b = "Hello, World!"
print(b[2:5])

# Modify Strings
# Upper Case
# ExampleGet your own Python Server
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
# Lower Case
# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
# Remove Whitespace
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())
# Replace String
# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
# Split String
# The split() method splits a string into a list:
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

# String Concatenation
#To add a space between them, add a " ":
c = "Hello"
d = "World"
e = c + " " + d
print(e)
#Merge variable a with variable b into variable c:
e = "Hello"
f = "World"
g = e + f
print(g)

# Format - Strings
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# age = 36
# #This will produce an error:
# txt = "My name is Muskan, I am " + age
# print(txt)
# But we can combine strings and numbers by using the format() method!
age = 36
txt = "My name is Muskan, I am {}"
print(txt.format(age))

# F-Strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
age = 36
txt = f"My name is Muskan, I am {age}"
print(txt)

# Placeholders and Modifiers
# A placeholder can contain variables, operations, functions, and modifiers to format the value.
# For example, you can use the format specifier :.2f to format a floating-point number with 2 decimal places:
price = 49.99
txt = f"The price is ${price:.2f}"
print(txt)
# You can also use the format specifier :>10 to right-align a string within a field of 10 characters:
name = "Muskan"
txt = f"Hello, {name:>10}!"
print(txt) 
# Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)
txt = f"The price is {20 * 59} dollars" #A placeholder can contain Python code, like math operations:
print(txt)

# Python - Escape Characters
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
#You will get an error if you use double quotes inside a string that is surrounded by double quotes:
#txt = "We are the so-called "Vikings" from the north."
# To fix this problem, use the escape character \":
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Other escape characters used in Python:
# \'	Single Quote
# \\	Backslash   
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \ooo    Octal value
# \xhh    Hex value

# String Methods
# Python has a set of built-in methods that you can use on strings.
# Note: All string methods return new values. They do not change the original string.
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

'''capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning'''

# Booleans
# Booleans represent one of two values: True or False.


