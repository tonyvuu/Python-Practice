#1 SLEEP_IN: The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

# print(sleep_in(True, False))

#2 diff21: Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

def diff21(n):
  if n <= 21: #if the int is equal to or less than 21 then proceed with the code
    return 21 - n # return the difference between 21 and n 
  else:
    return (n - 21) * 2 # if it doesnt follow the if statement, then return the difference of n and 21 then multiply it by two to get the absolute difference.

# print(diff21(22))

#3 near-hundred: Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

print(near_hundred(110))


#4 SUM-DOUBLE: Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
  sum = a + b   # store the sum in a local variable
  
  if a == b:    # if parameter 1 and parameter 2 are the same, then
    sum = sum * 2   # double it by multiplying by two
    return sum

# print(sum_double(3,2))

# MAKES10: Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
def makes10(a, b):
  return (a == 10 or b == 10 or a + b == 10)

# print(makes10(2,5))

# Not_string: Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.




# FRONT_3: Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

