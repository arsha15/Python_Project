with open("guests.txt", "w") as guests:
    initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]
    for i in initial_guests:
        guests.write(i + "\n")
