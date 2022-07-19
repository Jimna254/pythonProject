"""
def welcome(name):
    print(f"Hello {name} Welcome to analytics Academy")


person1 = {
  "name": "James",
  "age": 20,
  "country": "Kenya"
  "education”: “BSC Software Engineering"

}
welcome(person1["name"])
"""
# Exceptions and Error Handling
"""
try:
    age = int(input('Age: '))
    income = 30000
    risk = income / age
    print(age)
    print(risk)
except ValueError:
    print("Invalid value! ")
except ZeroDivisionError:
    print("Age Can't be zero")
"""
# Classes in Python

'''
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point()
point1.draw()
'''
# using dictionaries
'''
phone = input("Phone: ")
digits_mapping = {
    "1": "one",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
   output += digits_mapping.get(ch, "!") + " "
print(output)
'''
#Return statements
def square(number):
    return number ** 2
print(square(3))



