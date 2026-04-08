# Python Data Types

# Text Type:	         str
# Numeric Types:	     int, float, complex
# Sequence Types:	     list, tuple, range
# Mapping Type:	         dict
# Set Types:	         set, frozenset
# Boolean Type:	         bool
# Binary Types:	         bytes, bytearray, memoryview
# None Type:	         NoneType

from types import NoneType


x = 5
print(type(x))        #<class 'int'>

a = "Hello, World!"
print(type(a))        #<class 'str'>

b = 3.14
print(type(b))        #<class 'float'>

c = True
print(type(c))        #<class 'bool'>

d = None
print(type(d))        #<class 'NoneType'>  

x = "Hello World"	                            (str)
#display x:
print(x)
#display the data type of x:
print(type(x)) 

x = 20	                                        (int)
#display x:
print(x)
#display the data type of x:
print(type(x)) 

x = 20.5	                                    (float)	

x = 1j	                                        (complex)	
x = ["apple", "banana", "cherry"]	            (list)	
x = ("apple", "banana", "cherry")	            (tuple)
x = range(6)	                                (range)	
x = {"name" : "John", "age" : 36}	            (dict)	
x = {"apple", "banana", "cherry"}	            (set)	
x = frozenset({"apple", "banana", "cherry"})	(frozenset)	
x = True	                                    (bool)	
x = b"Hello"	                                (bytes)	
x = bytearray(5)	                            (bytearray)	
x = memoryview(bytes(5))	                    (memoryview)	
x = None	                                    (NoneType)	
