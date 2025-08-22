print("Hello World")
for i in range(5):
    print("Printing iteration number ",i)# This is a comment


def greetings(name):
    print("Hello " + name)

   
greetings("Arvind")
greetings("Yuvraj")


import calendar
year = 1977
month = 2
print(calendar.month(year,month))

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return f"{hours} hours, {minutes} minutes, {remaining_seconds} seconds"

# Example usage:
seconds = 3672

print(convert_seconds(seconds))
