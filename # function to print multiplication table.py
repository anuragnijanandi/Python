# function to print multiplication table

def print_table (n):
    """Prints the multiplication table for the given number n."""
    i=1
    while i<= 10:
        print(f"{n} x {i} = {n*i}")
       
        i += 1

# input from user
n =int (input("Enter the number:   "))

# calling the function
print_table(n)
# end of the code
