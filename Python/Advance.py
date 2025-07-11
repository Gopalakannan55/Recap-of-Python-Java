# Exception Handling
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")

# OOP
#class,obj,method
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

p = Person("Kumar")
p.greet()


#  Inheritance
class A:
    def show(self):
        print("Class A")

class B(A):
    pass

b = B()
b.show()

# List Comprehension

squares = [x**2 for x in range(5)]
print(squares)

from functools import reduce

#py map filter redue
nums = [1, 2, 3]
print(list(map(lambda x: x*2, nums)))      
print(list(filter(lambda x: x % 2 == 0, nums)))  
print(reduce(lambda x, y: x+y, nums))   
