print("Hello, World!")

# Variables and Data Types
a = 10        
b = 5.5       
name = "Ram"  
flag = True   

# Input and Output
name = input("Enter your name: ")
age=int(input("Enter your age:"))
print("Hello", name,"you age is ",age)

# Type Conversion
x = int("10")     # str to int 
y = str(100)      #int to str

# Operators and Control Flow
a = 5
b = 10
print(a + b)
print(a - b)
print(a *b)
print(a > b and a != b)

#  Conditional Statements
# if
x=10
if x ==10:
    print("10")

#if-else
x=20
if x > 10:
    print("Big")
else:
    print("Small")

#if-else-lader
x = 20
if x > 10:
    print("Big")
elif x == 10:
    print("Equal")
else:
    print("Small")


#  Loops
# for 
for i in range(5):
    print(i)

# while 
x = 0
while x < 3:
    print(x)
    x += 1

# Data Structures
# list
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[1])       
fruits.append("kiwi")  

#tuble
t = (10, 20, 30)
print(t)
print(t[0])

#sets
s = {1, 2, 2, 3}
print(s)

#dict
person = {"name": "Ram", "age": 25}
print(person["name"])
print(person)

# str
text = " Hello World "
print(text)
print(text.strip())
print(text.lower())