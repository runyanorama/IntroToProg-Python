# ------ Exception Handling Demonstration ------#
try: # Gets user inputs, stores them as tuple data, and establishes a 'try-except' block to test validity of inputs
    int_customer_ID = int(input("Please enter customer ID: "))
    str_customer_name = input("Please enter customer name: ")
    str_customer_email = input("Please enter customer email address: ")
    tpl_data = (int_customer_ID, str_customer_name, str_customer_email),
    print("Your current database is: ", str(tpl_data) + "\n")

    str_user_input = input("Enter 'exit' to quit, or press any key to continue and enter new items.")
    if str_user_input.lower() == 'exit':
        exit()

# I anticipated the user entering a string character rather than an integer for 'customer ID',
# so I created a 'ValueError' exception message.
# Because the 'e' built-in function stores the error message in memory, I used it to display
# the actual message rather than simply inform the user that an error had occurred.
except ValueError as e:
    print("The following error was detected:"'\n')
    print(e)
    print("Please choose an integer value for 'Customer ID'!")


# This serves as a general 'catch-all' for any errors that I did not anticipate while continuing
# to display the actual content of the error message itself.
except Exception as e:
    print("The following error was detected:")
    print(e)


# I have used the same 'try-except' block as above, continuing to use both specific and general error exceptions.
# This was necessary because my program gets a new set of inputs (i.e. updated inputs) from the user, this time
# scripted within a 'while' loop, thus requiring a second 'try-except' block.
try:
    while True:
        updated_ID = int(input("Please enter new customer ID: "))
        updated_name = input("Please enter new customer name: ")
        updated_email = input("Please enter new customer email address: ")
        updated_tpl_data = (updated_ID, updated_name, updated_email),
        tpl_data += (updated_tpl_data)


        print("Your updated database is: ", str(tpl_data) + "\n")

        str_user_input = input("Enter 'exit' to quit, or press any key to continue.")
        if str_user_input.lower() == 'exit':
            break
        else:
            continue

except ValueError as e:
    print("The following error was detected:")
    print(e)
    print("Please choose an integer value for 'Customer ID'!")

except SyntaxError as e:
    print("The following error was detected:")
    print(e)

except Exception as e:
    print("The following error was detected: ")
    print(e)





# ------ Working with Binary Files ------ #
import pickle

# Gets user inputs-- these will be the 'values' in our dictionaries.
int_customer_ID = int(input("Please enter customer ID: "))
str_customer_name = input("Please enter customer name: ")
str_customer_email = input("Please enter customer email address: ")

# Create dictionaries using the inputs as 'values' and their respective terms as 'keys.'
dict_ID = {'ID': int_customer_ID}
dict_name = {'Name':str_customer_name}
dict_email = {'Email': str_customer_email}
lst_data = [ ] # Start with a blank list and append dictionary data to it.

# Dictionary data is appended to the list. I'm sure there is a smarter way to do this--- but I'm not smart.
# Once the list is compiled, it will be 'pickled.'
lst_data.append(dict_ID)
lst_data.append(dict_name)
lst_data.append(dict_email)

# Verifies that the list compiled correctly
print("Here is your data: ", str(lst_data) + "\n")
str_user_input = input("Press 'enter' to continue and save, or enter 'exit' to quit."'\n')

if str_user_input.lower() == 'exit':
    exit()
else:
    # Stores the data with the pickle.dump method

    objFile = open("C:\\_PythonClass\\customers.dat", "wb")
    pickle.dump(lst_data, objFile)
    objFile.close()

    # Reads the data back with the same pickle.load method
    objFile = open("C:\\_PythonClass\\Customers.dat", "rb")
    objFileData = pickle.load(objFile)
    objFile.close()

    print("Thank you! The following data was saved:")

    print(objFileData)