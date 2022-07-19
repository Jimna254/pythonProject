# Weight converter
'''
try:

     weight = input("your weight: ")
     Unit = input("(L)bs or (K)g: ")

     if Unit.upper() == "L":
          print(round(int(weight) * 0.45))

     elif Unit == "K":
          print(round(int(weight)/0.45))

     else:
      print("invalid input")

except ValueError:
     print("Invalid Inputs")'''
"""
#Classes => Use the keyword class
class Point:
     def move(self):
          print("move")
     

     def draw(self):
          print("draw")


point1 = Point()
point1.move()"""
# We use Classes to define new types 

# Using Constructors
'''
class Point:
     def __init__(self, x, y):
         self.x=x
         self.y=y

     def move(self):
          print("move")

     def draw(self):
          print("draw")

point = Point(10, 20)
print(point.x, point.y)'''

# A Class Person it should have a name attributre as well as a talk method
'''
class Person:
     def __init__(self, name):
           self.name = name
     def talk(self):
          print(f"Hi ! I am{self.name}")


john = Person(" John Smith")
james = Person(" James Kariuki")
john.talk()
james.talk()
'''
# Inheritance
class Mammal:
     def walk(self):
          print("Walk")


class Dog(Mammal):
     pass

class Cat(Mammal):
     def playfull(self):
          print("Meow")

cat1 = Cat()
cat1.playfull()
cat1.walk()
  
     

          



           


