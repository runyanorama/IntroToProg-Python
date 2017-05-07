# 1) Create a text file called todo.txt and using some data (tasks, priorities).
# 2) Load each row of data from the ToDo.txt file into a Python dictionary. The data will be stored in a row,
# like a table.
objFile = open("ToDo.txt", "r")
lstTable = [] # assigns a blank list to variable because user will be 'appending' dictionary itmes to the list.

# 3) After you get the data into a Python dictionary, add the new dictionary 'row' into a Python 'list' object (now
# the data will be managed as a table.)
# Reads entire first line of text file while separating into two index items, 'task' and 'priority'.
# Assigns each index item of line to a single variable split into its indices.
# assigns 'items' to a new variable and makes that variable a dictionary item consisting of each index as the key/value.
# Puts dictionary item into lstTable by 'append' method.
for line in objFile:
    items = line.strip().split(",")
    dicNewRow = {items[0]: items[1]}
    lstTable.append(dicNewRow)
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
    # Exits the program.
    if (strChoice == '0'):
        print("Goodbye!")
        break

    # Shows current data table
    elif (strChoice.strip() == '1'):
        print("\nYour current data is:\n")
        for index, item in enumerate(lstTable): # iterates across each item in lstTable by index number.
            print("{} - {}".format(index, item)) # 'format' method allows user to rearange and display lstTable with each index
            # number corresponding to its respective dictionary item. This will allow easy addition and deletion of items in
            # lstTable according to their index numbers.

        print("Please select a user option:")
        continue

    elif (strChoice.strip() == '2'):
        # Ask user for two new user inputs (task, priority).
        strTask = input("Please specify the new task: ")
        strPriority = input("Please specify the priority: ")
        dicNewItem = {strTask:strPriority} # assigns user inputs into a new dictionary item. This MUST be displayed in proper
           # dictionary form (i.e. curly brackets and 'colon') otherwise it will be interpreted as a 'set' and will return an error.

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
            lstTable.append(dicNewItem) #adds new dictionary item to list using 'append' method.
            # 4) Display contents of the list to user.
        print("Your new database is: ", lstTable)
        objFile.close()

    elif (strChoice.strip() == '3'):
        strItemDelete = int(input("Please enter a task to delete: "))
        for index, item in enumerate(lstTable):
            if index == strItemDelete:
                value = item
        lstTable.remove(value)

    elif (strChoice.strip() == '4'):
        objFile = open("ToDo.txt", "w")
        objFile.write(str(lstTable))
        objFile.close()
    print("Thank you! Your data was saved.")
