import statistics

#myModule.welcome(input("Enter Your Name: "))

#from myModule import person1
#print(person1['age'])
#is_hot = False
#is_cold = False
#if is_hot:
   # print("it's a hot day")
    #print("Drink plenty of water ")

"""elif is_cold:
    print("it's a cold day")
    print("Wear warm clothes")
else:
    print("it's a lovely day")
  #  print("Enjoy your day")
"""
"""price = 1000000
has_good_credit = False 
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment = ${down_payment} ")"""

"""high_income = True
good_credit = False
if high_income and good_credit:
   print("Eligible for loan")
else:
    print("not Eligible")"""

""""
name = input("Pet name: ")
if len(name) < 3:
    print("Choose again...Stupid name!! ")
elif len(name) > 50:
    print("name can be a maximum of only 50 characters ")
else:
    print("Name looks good")"""

# Weight converter
""""
weight = input("your weight: ")
Unit = input("(L)bs or (K)g: ")
if Unit.upper() == "L":
    print(round(int(weight) * 0.45))

elif Unit.upper() == "K":
    print(round(int(weight)/0.45))

else:
    print("invalid input")"""
# While loops
""""
i = 1
while i <= 5:
    print(i)
    i += 1
print("Done")
"""
'''i = 1
while i <= 5:
    print("*" * i)
    i += 1'''

# Guess Game
"""
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    Guess = int(input("Guess: "))
    guess_count += 1
    if Guess == secret_number:
        print('You Win!')
        break
    elif Guess != secret_number:
        print("Try Again!")
else:
    print("Sorry you Failed !") """

#Car game
"""
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already Started! ")
        else:
            started = True
            print("car started...")

    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped!")

    elif command == "help":
        print('''
start - to start the car  
stop - to stop the car
quit - to exit
 ''')
    elif command == "quit":
        break

else:
    print("I don't understand that...") 
    """

# For loops

"""for item in range(5, 10, 2):
    print(item)
for item2 in range(5, 10):
    print(item2)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")  """

# Nested loops
"""
for x in range (4):
    for y in range (3):
        print(f'({x},{y})')
"""

# Lists
"""
names = ['James', 'John', 'Beau', 'Greg', 'Cain']
# access a range of items second item to the last item
print(names[1:])
# to get the last item in the list
print(names[-1])
"""
"""
# A program to find the largest number in the list
numbers = [20, 30, 70, 5, 7, 9, 3, 1]
print(max(numbers))
print(min(numbers))

print(statistics.mean(numbers))

# list functions
print(len(numbers))
numbers.pop()
print(numbers)
numbers.clear()
print(numbers) """

# Multi dimensional lists
"""
matrix = [
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
]
my_marks = [44, 57, 57, 65, 57, 65, 80, 80]
print(matrix)
print([7, 8, 9] in matrix)
print(my_marks.count(57))
my_marks.sort()
# sort method arranges the numbers in ascending order
my_marks.reverse()
# reverse method reverses the numbers from ascending to descending
print(my_marks)
numbers2 = my_marks.copy()
print(numbers2)
"""
# A program to remove the duplicates in a
'''
scores = [12, 25, 40, 50, 60, 25, 60, 70]
unique_scores = []
for score in scores:
    if score not in unique_scores:
        unique_scores.append(score)
print(unique_scores)'''

# TUPLES
     # Used to

# Dictionaries
"""
customer = {
    "Name": "James Kariuki",
    "Age": 30,
    "Height": 6,
    "is_verified": True
}
print(customer["Name"])
print(customer.get("Name"))
"""
"""
phone = input("Phone no: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "Three",
    "4": "Four"

}
output = ""
for no in phone:
    output += digits_mapping.get(no, "!") + " "
print(output) """
"""i = 1
while True:
    if i % 3 == 0:
        break
    print(i)

    i += 1
print(i)"""

# Functions

'''

def greet_user(first_name, last_name):
    print(f'Hi{first_name} {last_name} ')
    print("welcome on board")'''


# using positional arguments


'''
print("start")
greet_user(" James", "Wanjiku")
greet_user(" Moreen", "Muthama")
print("finish")

# using keyword arguments
greet_user(last_name=" Wanjiku", first_name=" James")'''

# by default all functions return None
# Square function

'''

def square(number):
    return number ** 2


print(square(3))
print(square(16))
print(square(297))
print(square(139))
'''
# Creating a reusable function
# Emoji Converter

def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": " 😊",
        ":(": " 😒 "
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))







