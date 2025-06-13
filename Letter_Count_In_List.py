Fruit_List = ["Apple", "Banana", "Strawberry", "Pears", "Grapes"]

counter = 0

for i in Fruit_List:

    counter = counter + len(i)

print("Total letters in the given List = ", counter)

print("Average length of each element in the given list is = ", (counter/len(Fruit_List))  )