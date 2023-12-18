# Intro to Python

# Integers - whole numbers

age = 30
# print(age)

# Float - not a whole number

pi = 3.14159
# print(pi)

# Boolean - True or False - T and F must be capitalized

is_raining = True 

# print(is_raining)

# Strings - a combination of alphanumeric values

name = 'Tony'
team = 'Lakers'
birthday = " February 23, 1997"

# Print out mutiple lines with spaces
months = '''
Jan, 
Feb,
March
'''

# print(months)

# Lists - sequence of values. These values can be integers, floats, strings, etc. 

scores = [100, 65, 78, 88]
names = ['Tony', 'Hien ', 'John']

# print(names[2])

# Dictionaries - this is a sequence of labeled values

BoysUsername = {"Tony": "Yonny", "Hien": "Heinous", "John": "Sniper"}

# print(BoysUsername["Hien"])

# Special Characters:
# \b - backspace
# \n - new line
# \t - horizontal tab
# \v - vertical tab
# \r - carriage return

# username = input("type in your username: ")
# password = input("type in your password: ")

# print(username, password)

# print("Welcome %s" % username) 

myAge = 26

print("My age is %s" % myAge)

# Using a float, you will use %f. 
print("pi = %f" % pi)
print("pi to the third decimal = %.3f" % pi)


# print(id_number)

# Division

result = 4/2
print('Result:', result)

# Absolute Value
positive_integer = abs(-40)
print(positive_integer)

# Exponents and Rounding
exponents = pow(2, 2)
rounding = round(pi)
exp = 2**2 

print(exponents, rounding, exp)

current_temp = 40
freezing_temp = 32 

if current_temp < freezing_temp:
    print('It is too cold')
elif current_temp > freezing_temp:
    print("Not too cold")
elif current_temp == freezing_temp:
    print("It is right at the freezing point! oh my!")
else:
    print("Error")
    
is_sunny = False

# AND - meaning both conditions on either side of the and must be true

if current_temp < freezing_temp and is_raining == True:
    print("It is freezing and raining.")
elif current_temp > freezing_temp and is_raining == False:
    print(" what a lovely day!")
else: 
    print("It is not a lovely day")   

# OR - only one condition needs to be true

if current_temp < freezing_temp or is_raining == True:
    print("it is freezing or it is raining, either way, stay inside!")
elif current_temp > freezing_temp or is_raining == False: 
    print(' It is a clear day today!')

if is_sunny != True: 
    print("It is not sunny")
    
    
# Lists 

# class_peeps = ['Tony', 'Dez', 'John', 'Kenny']

# Print the entire list
# print(class_peeps)

# Print the first person in the list
# print(class_peeps[0])

# Example 1: Print all names in the list
# for names in class_peeps:
#     print(names)

# Example 2: Change Dez to say instructor, Kenny to ken, Tri to sudent
# for name in class_peeps: 
#     if name == 'Tony':
#         print("Yonny")
#     elif name == 'Kenny':
#         print('Ken')
#     elif name == 'John':
#         print("Jackal")
#     else:
#         print(name)
        
# Example 3: Will print the numbers 0-9
# for num in range(10):
    # print(num)

# Example 4: Print the numbers 5-10
# for num in range(5,11):
#     print(num)
    
# Print the first letter of Atlanta
# city = 'Atlanta'
# print(city[0])

#How to delete the last item from a list: 
# class_peeps.pop()
# print(class_peeps)

# Homework


id = -100

if id < 100:
    print("1st")
elif id in range (100, 249.99):
    print("2nd")
elif id > 250: 
    print("All reservations are taken")
else:
    print("error")
    

# Reversing a list

sample_text = 'Hello World'
sample_list = [1,2,3,4,5]
reversed_list = []

# Example 1, using a while loop
ints = len(sample_list) - 1
while ints >= 0:
    reversed_list.append(sample_list[ints])
    ints = ints - 1
print(sample_list, reversed_list)

# Example: reverse using a slice
print(sample_list[::-1])

# Write a short program that prints each number from 1 to 100 on a new line.
# For each multiple of 3, print "Fizz" instead of the number.
# For each multiple of 5, print "Buzz" instead of the number.
# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

# for num in range(1,101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("fizz")
#     elif num % 5 == 0:
#         print("buzz")
#     else:
#         print(num)
    
# What is a function? A function is a reusable block of code that can be called any time. In orde to call a function in python, we need to start with def. def just stands for definition. The user will need to pass in a parameter. See example below:

# The parameter is a variable that a function takes in. Below is a parameter user_name.

# def say_howdy(user_name):
    # print('Howdy', user_name)

# Any time you write a function, you must call it and pass an argument. 
# name = input('What is your name?')

# say_howdy(name)

# first_name = input("what is your first name?")
# last_name = input('what is your last name?')

# def second_function(parameter1, parameter2):
# this method uses string concatenation
# print ("hey there", parameter1 + ' ' + parameter2)
    # print("hey there", parameter1, parameter2)
    
# second_function(first_name,last_name)


# Calculate the area of a rectangle using a function and a variable
# Function where we define what we expect to be passed in as parameter:
def area(length: int, width: int) -> int:
    return length * width
area_of_rectangle = area(5,6)

print(area_of_rectangle)

# How to get the area of a circle:
def area_of_circle(radius):
    PI = 3.14
    return PI * radius**2 

def wear_sweater():
    try:
        temp = int(input("What is the temperature? "))
        humidity = int(input("What is the humidity? "))
        wind_speed = int(input("What is the wind speed? "))
        
        if temp < 55:
            return True
        elif temp >= 55 and temp < 65 and humidity < 30:
            return True
        elif temp < 60 and wind_speed > 10:
            return True
        else:
            return False
    except ValueError: 
        return "Enter a valid whole integer."

print(wear_sweater())
