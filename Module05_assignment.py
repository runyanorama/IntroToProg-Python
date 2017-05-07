# 1) Create a text file called todo.txt and using some data (tasks, priorities).
objFile = open("ToDo.txt", "r")
lstTable = [] # defines the lstTable variable as a blank list because user will be 'appending' dictionary items to it.
for line in objFile:
    items = line.strip().split(",") # Reads entire first line of text file while splitting the line into two items.
# 2) Load each row of data from the ToDo.txt file into a Python dictionary. The data will be stored in a row,
# like a table.
    dicNewRow = {items[0]: items[1]} # Assigns each index item of line to a dictionary row.
# 3) After you get the data into a Python dictionary, add the new dictionary 'row' into a Python 'list' object (now
    # the data will be managed as a table.)
    lstTable.append(dicNewRow) # Puts dictionary item into lstTable using 'append' method.
# 4) Display contents of the list to user.
print("Your current database is: ", lstTable)
objFile.close()

# 5) Allow the user to add or remove tasks from the list using numbered choices.
strChoice = None
while (strChoice != 0):
    print("""
    Menu of Options
    0) Exit Program 
    1) Show current data 
    2) Add a new item. 
    3) Remove an existing item.
    4) Save data to a file.
    """)
    strChoice = str(input("Which option would you like to perform? [0 - 4] - "))
    print()
# 6) Allows user to save upon exiting the program.
    if (strChoice.strip() == '0'):
        objFile = open("ToDo.txt", "w")
        objFile.write(str(lstTable))
        objFile.close()
    print("Your data was saved. Goodbye!")
    break

    # Shows current data table
    if (strChoice.strip() == '1'):
        print("\nYour current data is:\n")
        for index, item in enumerate(lstTable):
            print("{} - {}".format(index, item))

            print("Please select a user option:")
            continue

    if (strChoice.strip() == '2'):
        # Ask user for two new user inputs (task, priority).
        strTask = input("Please specify the new task: ")
        strPriority = input("Please specify the priority: ")
        dicNewItem = {strTask:strPriority}

        # writes that data to object file
        objFile = open("ToDo.txt", "a")
        items = line.strip().split(",")
        for key, value in dicNewItem.items():
            objFile.write("\n{},{}".format(key, value))
        print("Your new input data was saved.")
        objFile.close()
        # Reads the 'dicNewItem' inputs and converts them into dictionary format.
        objFile = open("ToDo.txt", "r")
        for line in objFile:
            strData = line
            dicNewItem = {(strData.split(",")[0]).strip(), (strData.split(",")[1]).strip()}
            lstTable.append(dicNewItem)
            # 4) Display contents of the list to user.
        print("Your new database is: ", lstTable)
        objFile.close()

    if (strChoice.strip() == '3'):
        strItemDelete = int(input("Please enter a task to delete: "))
        for index, item in enumerate(lstTable):
            if index == strItemDelete:
                value = item
        lstTable.remove(value)

    # 6) Saves data in the ToDO.txt file
    if (strChoice.strip() == '4'):
        objFile = open("ToDo.txt", "w")
        objFile.write(str(lstTable))
        objFile.close()
    print("Thank you! Your data was saved.")
