def print_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "X" * (2 * i - 1))

# Set the height of the pyramid
height = int(input("Enter the height of the pyramid: "))
print_pyramid(height)