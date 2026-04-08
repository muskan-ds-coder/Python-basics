# A Variable is a container to store data
x = 12
name = "Muskan"

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# You can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))

#String variables can be declared either by using single or double quotes:
x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)

#Variable names are case-sensitive.
a = 4
A = "Sally"
print(a)
print(A)

# Uses of Variable (Store data)
age = 21

# Perform calculations
a = 4
b = 2
print(a+b)

#Store user input
name = input("Enter name: ")

# Reuse values
price = 50
total = price * 2
print(total)

# Many values to Multiple variable
a, b, c, = 1, 2, 3
print(a, b, c)

# Casting
x = str(3)      # x will be '3'
y = int(3)      # y will be '3'
z = float(3)    # z will be '3.0'
print(x)
print(y)
print(z)

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#Illegal variable names:

# 2myvar = "John"
# my-var = "John"
# my var = "John"
#This example will produce an error in the result


