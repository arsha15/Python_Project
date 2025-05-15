# Function to find factors using while loop
def find_factors(n):
    i = 1  # Start from 1
    print(f"Factors of {n}:")
    while i <= n:
        if n % i == 0:  # Check if 'i' is a factor
            print(i)
        i += 1  # Increment 'i'

# Input from user
num = int(input("Enter an integer: "))
find_factors(num)