import math

import ecommerce.shipping

# print("Hello World")
# print("o----")
# print(" ||||")
# print("*" * 10)
# price = 10
# price = 11
# price += 1
# rating = 4.9
# name = "Ian"
# is_published = True
# print(price)
# print(is_published)

# print("Hospital Patient")
# name = "John Smith"
# age = 35
# is_new_patient = True

# name = input("What is your name? ")
# fav_color = input("What is your favourite colour? ")
# print(name + " likes " + fav_color)

# birth_year = input("Birth year: ")
# print(type(birth_year)) # <class 'str'>
# use int(num) to convert the string num to an int
# # age = 2024 - int(birth_year)
# print(type(age)) # <class 'int'>
# print(age)
# # use str(x) to convert the int x to a string
# print(str(age) + " years old!")

# weight_lbs = input("What is your weight in lbs? ")
# weight_kgs = int(weight_lbs) / 2.2
# print(weight_kgs)
# print(str(weight_kgs) + "kgs")

course = '''Hi there Luke,
You are a Jedi.
Deal with it.'''
print(course)

new_course = "Python for Beginners"
#            [0123456789..........]
print(new_course[0])
print(new_course[-1])
print(new_course[-4])
# Will start with first index, and finish BEFORE the second stated index i.e. 0-5
print(new_course[0:6])
print(new_course[5:])  # start at index 5 until the end
print(new_course[:8])  # starts at beginning until before 8th index
print(new_course[:])  # essentially copies the string

first_name = "John"
last_name = "Smith"
message = first_name + " [" + last_name + "] is a coder."
print(message)
# FORMATTED STRINGS
msg = f"{first_name} [{last_name}] is a coder"
print(msg)
course2 = "Python learnings"
print(len(course2))
course3 = course2.upper()
print(course3)
print(course2.find("y"))  # return the index of the first occurance.
# CASE SENSITIVE - will return -1 if not found.
print(course2.find("Y"))
print(course2.find("learnings"))  # returns index of first character
print(course2.replace("learnings", "for everyone!"))  # still case sensitive
print("Python" in course2)  # returns Boolean

print(math.ceil(2.9))
x = 2.9
# test123
# test

print(round(x))
print(abs(-2.9))

print(math.floor(2.9))

# LISTS
names = ["Ian", "Lee", "Ernie", "Charlie"]
print(names)
print(names[2])
print(names[2:])
print(names[1:3])
print(names[:2])
print(names[:])
names[0] = "James"
print(names)

numbersList = [3, 79, 3, 1, 8, 5, 3, 7, 52]
highestNumber = 0
for number in numbersList:
    if number > highestNumber:
        highestNumber = number
print(highestNumber)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)
matrix.append([10, 11, 12])
print(matrix)
matrix.insert(0, [0, 0, 0])
print(matrix)
matrix.insert(3, [0, 0, 0])
print(matrix)
matrix.remove(matrix[3])
print(matrix)
matrix.pop()
print(matrix)
print(matrix.index([0, 0, 0]))
print(50 in matrix)  # will print False
matrix.sort()
print(matrix)
matrix2 = matrix.copy()
matrix2.append([30])
print(matrix)
print(matrix2)

# Tuples
tuplesList = (3, 6, 2, 1, 2, 2)
# tuplesList is immutable!!!
print(tuplesList.count(2))
print(tuplesList.count(1))

coords = (1, 2, 3)
# coords[0] * coords[1] * coords[2]
# x = coords[0]
# y = coords[1]
# z = coords[2]
# x * y * z
# UNPACKING
x, y, z = coords  # same as above.  Can also be done with Lists
print(x)

# Dictionaries
person = {
    "name": "Ian McNicholas",
    "age": 34,
    "is_Verified": True
}
print(person)
print(person["name"])
person["name"] = "Lee P"
print(person)
print(person.get("test"))  # Will print None.  Not using get will cause an error
print(person.get("Town", "London"))  # provide default value if none found

# EMOJIS
# On a Mac, access emojis with - Control + Command + Space
emojis = {
    ":)": "🙂",
    ":(": "😞"
}
print(emojis.get(":)"))


def greet_user(first_name="Jeff", last_name="Bridges"):
    print(f"Hello there, {first_name} {last_name}")


greet_user("Ian McNicholas")
greet_user()
greet_user(last_name="Smith")
greet_user(last_name="Sumner", first_name="Hugo")

ecommerce.shipping.find_cost()
