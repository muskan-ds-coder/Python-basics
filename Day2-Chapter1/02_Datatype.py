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

e = "Hello World" #(str)
#display e:
print(e)
#display the data type of e:
print(type(e)) 

f = 20	#(int)
print(f)
print(type(f)) 

g = 20.5  #(float)
print(g)
print(type(g))  

h = 1j	 #(complex)	
print(h)
print(type(h)) 

i = ["apple", "banana", "cherry"]  #(list)
print(i)
print(type(i)) 
# Empty list
my_list = []
# List with items
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]
# Modifying list, Lists are mutable, so you can change them:
fruits.append("orange")  # Add to end
fruits.insert(1, "grape")  # Insert at index
fruits.remove("banana")  # Remove by value
fruits.pop(0)  # Remove by index

j = ("apple", "banana", "cherry")  #(tuple)
print(j)
print(type(j)) 

k = range(6)  #(range)
print(k)
print(type(k)) 

l = {"name" : "John", "age" : 36}	#(dict)
print(l)
print(type(l)) 

m = {"apple", "banana", "cherry"}	#(set)
print(m)
print(type(m)) 

n = frozenset({"apple", "banana", "cherry"})  #(frozenset)	
print(n)
print(type(n)) 

o = True  #(bool)
print(o)
print(type(o)) 

p = b"Hello"  #(bytes)
print(p)
print(type(p)) 

q = bytearray(5) #(bytearray)
print(q)
print(type(q)) 

r = memoryview(bytes(5))  #(memoryview)
print(r)
print(type(r)) 

s = None  #(NoneType)
print(s)
print(type(s)) 	

