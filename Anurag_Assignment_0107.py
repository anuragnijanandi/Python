# author: Anurag Nijanandi
# aicte id: 1-3239824826
# date: 2024-01-07
# assignment: 0107

# Q1: Find the greatest of 3 numbers

# This program finds the greatest of three numbers entered by the user.

print("Enter three numbers to find the greatest among them.")

# Get input from user
a = int(input("Enter first number: "))          # a is the first number
b = int(input("Enter second number: "))         # b is the second number
c = int(input("Enter third number: "))          # c is the third number

# Compare the numbers and find the greatest
# Check if a is greatest
if a >= b and a >= c:
    print("The greatest number is:", a) 
# Check if b is greatest
elif b >= a and b >= c:
    print("The greatest number is:", b)
# if a and b are not greatest, then c is the greatest
else:
    print("The greatest number is:", c)


# Q2: Check whether the number is even or odd

# This program checks whether a number entered by the user is even or odd.

print("Enter a number to check if it is even or odd.")

# Get input from user

num = int(input("Enter a number: "))  # number should be an integer

# Check if the number is even or odd
# If the number is divisible by 2, it is even; otherwise, it is odd
if num % 2 == 0:
    print(num, "is an even number.")    # display if the number is even
else:
    print(num, "is an odd number.")     # display if the number is odd


# Q3: Check whether a year is a leap year or not

# This program checks whether a year entered by the user is a leap year or not.
print("Enter a year to check if it is a leap year.")

# Get input from user
year = int(input("Enter a year: "))
# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")          # display if the year is a leap year
else:
    print(year, "is not a leap year.")      # display if the year is not a leap year


# Q4: Check-simulate traffic signal

# This program simulates a traffic signal based on user input.

print("Enter the traffic signal colour (red, yellow, green) to check the action.")

# Get input from user (any colour: red, yellow, green)
signal = input("Enter the traffic signal colour (red, yellow, green): ").lower() # convert input to lowercase for consistency

# Check the traffic signal colour
if signal == "red":
    print("STOP!")              # display if the signal is red
elif signal == "yellow":
    print("PAUSE!")             # display if the signal is yellow
elif signal == "green":
    print("GO!")                # display if the signal is green    


# Q5: Write a program for grading using logical operators

# This program assigns a grade based on the marks entered by the user.

print("Enter your marks to get the grade.")

# Get input-marks from user

marks = int(input("Enter your marks: ")) # convert input marks to integer

# Check the marks and assign a grade

if marks >= 90: 
    print("Grade: A")                   # display if marks are 90 or above
elif marks >= 80:
    print("Grade: B")                   # display if marks are 80 or above
elif marks >= 70:
    print("Grade: C")                   # display if marks are 70 or above
elif marks >= 60:
    print("Grade: D")                   # display if marks are 60 or above
elif marks >= 50:
    print("Grade: E")                   # display if marks are 50 or above
else:       
    print("Grade: Fail")                # display if marks are below 50