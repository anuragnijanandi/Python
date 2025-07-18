# height_example.py

# Problem Statement:
# If you're taller than 56", you can ride Space Mountain at Disneyland.
# If you're shorter, you cannot.
# Additionally, if you are greater than 150 inches, you are super tall and
# deserve a witty message.

# Get user's height
height = int(input("How tall are you? "))

# Do this if statement first
if height > 150:
    print("Wow, you're tall!")

# Do this one second - so people who are tall get the witty message
# AND get permission to ride the ride
if height >= 56:
    print("OK, you can ride Space Mountain.")
else:
    print("Too short to ride.")