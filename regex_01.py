log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

index = log.index("[")

print("The square bracket is located at index number", index)

print("The extracted process id is", log[index+1:index+6])