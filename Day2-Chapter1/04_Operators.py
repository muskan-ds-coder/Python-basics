# Python Operators

# Arithmetic Operators: +, -, *, /, %, **, //
# Assignment Operators: =, +=, -=, *=, /=, %=, **=, //=
# Comparison Operators: ==, !=, >, <, >=, <=    
# Logical Operators: and, or, not
# Bitwise Operators: &, |, ^, ~, <<, >>
# Identity Operators: is, is not
# Membership Operators: in, not in

# Arithmetic Operators
x = 10
y = 5
z = x + y  # Addition
a = x - y  # Subtraction
b = x * y  # Multiplication
c = x / y  # Division
d = x % y  # Modulus
e = x ** y  # Exponentiation
f = x // y  # Floor Division    
print("Addition:", z)
print("Subtraction:", a)
print("Multiplication:", b)
print("Division:", c)
print("Modulus:", d)
print("Exponentiation:", e)
print("Floor Division:", f)

# Assignment Operators
x = 10  # Assignment
x += 5  # Equivalent to x = x + 5   
print("After += 5:", x)
x -= 3  # Equivalent to x = x - 3
print("After -= 3:", x)
x *= 2  # Equivalent to x = x * 2
print("After *= 2:", x)
x /= 4  # Equivalent to x = x / 4
print("After /= 4:", x)
x %= 3  # Equivalent to x = x % 3
print("After %= 3:", x)
x **= 2  # Equivalent to x = x ** 2
print("After **= 2:", x)
x //= 2  # Equivalent to x = x // 2
print("After //= 2:", x)

# Comparison Operators
a = 10
b = 20
print("a == b:", a == b)  # Equal to
print("a != b:", a != b)  # Not equal to
print("a > b:", a > b)    # Greater than
print("a < b:", a < b)    # Less than
print("a >= b:", a >= b)  # Greater than or equal to
print("a <= b:", a <= b)  # Less than or equal to

# Logical Operators
x = True
y = False
print("x and y:", x and y)  # Logical AND
print("x or y:", x or y)    # Logical OR
print("not x:", not x)      # Logical NOT

# Bitwise Operators:
a = 5  # In binary: 0101
b = 3  # In binary: 0011 
print("a & b:", a & b)  # Bitwise AND
print("a | b:", a | b)  # Bitwise OR
print("a ^ b:", a ^ b)  # Bitwise XOR
print("~a:", ~a)        # Bitwise NOT
print("a << 1:", a << 1)  # Left shift
print("a >> 1:", a >> 1)  # Right shift

# Identity Operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print("x is y:", x is y)      
print("x is z:", x is z)      
print("x is not y:", x is not y)  

# Membership Operators
x = "Hello, World!"
print(" 'Hello' in x:", 'Hello' in x)      
print(" 'World' not in x:", 'World' not in x)  
y = [1, 2, 3, 4, 5]
print(" 3 in y:", 3 in y)      
print(" 6 not in y:", 6 not in y)  
fruits = ["apple", "banana"]
print("apple" in fruits)      
print("grape" not in fruits)  




