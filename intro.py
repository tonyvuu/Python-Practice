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

class_peeps = ['Tony', 'Dez', 'John', 'Kenny']

# Print the entire list
# print(class_peeps)

# Print the first person in the list
# print(class_peeps[0])

# Example 1: Print all names in the list
for names in class_peeps:
    print(names)

# Example 2: Change Dez to say instructor, Kenny to ken, Tri to sudent
for name in class_peeps: 
    if name == 'Tony':
        print("Yonny")
    elif name == 'Kenny':
        print('Ken')
    elif name == 'John':
        print("Jackal")
    else:
        print(name)
        
# Example 3: Will print the numbers 0-9
# for num in range(10):
    # print(num)

# Example 4: Print the numbers 5-10
for num in range(5,11):
    print(num)
    
# Print the first letter of Atlanta
city = 'Atlanta'
print(city[0])

#How to delete the last item from a list: 
class_peeps.pop()
print(class_peeps)

