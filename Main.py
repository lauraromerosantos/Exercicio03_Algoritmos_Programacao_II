from List import List

list = List()
list.add(43)
list.add(10)
list.add(24)
print("List in order: " + str(list.size))
list.printListOrdered()
list.printReverseOrder()

value = input("Enter a value: ")
list.add(value)
print("\n -----------------\n")
list.printListOrdered()
list.printReverseOrder()
