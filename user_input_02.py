def convert_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds
print("Seconds converter")
counter = 'y'
while(counter.lower() == 'y'):
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))
    total_seconds = convert_to_seconds(hours, minutes, seconds)
    print("Total seconds:", total_seconds)
    counter = input("Do you want another run y/n")
print("End of program")
'''
print()
print("Lastline of the code")
print()
'''