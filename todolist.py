#---------------------------------------------------#
# Title: To Do List
# Purpose:  Program loads current To Do list
#           from todo.txt into a Python dictionary,
#           display the contents of the list to the
#           user, and then allow the user to perform
#           one of several menue options.
# Dev: Marie Augustine
# Date: April 26, 2019
# ChangeLog:
# MarieAugustine, 4/26/2019, Created script
#---------------------------------------------------#



# Step 1: Read the file
# open file
file = open("todo.txt","r")
# create lstTable for first row
strdata0 = file.readline()
column = strdata0.split(',')
task = str(column[0]).strip()
priority = str(column[1]).strip()
dicRow = {'Task ': task, 'Priority ': priority}
lstTable = [dicRow,]

# read additional rows of data and add them to lstTable
for line in file:
    column = line.split(',')
    task = str(column[0]).strip()
    priority = str(column[1]).strip()
    dicRowNew = {'Task ': task, 'Priority ': priority}
    lstTable.append(dicRowNew)

# loop to display menu and offer options
# display a menu
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line

    # Choice 1: Display the current to-do list
    if strChoice == '1':
        print('Here is your current To-Do list...')
        print('---------------------------------')
        print('TASK',' --- ','PRIORITY\n')
        for item in lstTable:
            print(item["Task "],' --- ',item["Priority "])
        print('---------------------------------\n')

    # Choice 2: Add a new item to lstTable
    elif strChoice == '2':
        addtask = input('Enter your new task: ')
        addpriority = input('Enter priority: ')
        dicRowNewer = {'Task ': addtask, 'Priority ': addpriority}
        lstTable.append(dicRowNewer)

    # Choice 3: Remove an item from to-do list
    elif strChoice == '3':
        strRemove = str(input('Which task would you like to remove? '))
        # for loop to look for and remove strRemove.
        # compare len1 before the loop to after the loop, len2.
        len1 = int(len(lstTable))
        for item in lstTable:
            if item["Task "] == strRemove:
                lstTable.remove(item)
        len2 = int(len(lstTable))
        # if the for loop goes through each list item and len1 == len2, item was not in the list
        if len2 == len1:
            print("\nI'm sorry, but ", strRemove, "was not in your current list.")
            print("Please choose another menu option.")
        # if len1 != len2, it means the remove was successful.
        else:
            print("\n",strRemove," has been removed from your to-do list.")

    # Choice 4: Save Data to File
    elif strChoice == '4':
        # close file in read mode
        file.close()
        # open file in write mode
        file = open("todo.txt","w")
        # write items in same way so that todolist.py can be run again and successfully read the file
        for item in lstTable:
            file.write(str(item["Task "]) + "," + str(item["Priority "]) + "\n")
        print("\nYour To-Do list has been saved!")
        # close file again
        file.close()
        # re-open file in read mode
        file = open("todo.txt","r")

    # Choice 5: Exit Program and let user know program is closed.
    elif strChoice == '5':
        print("Program closed.")
        break
    # If choice other than 1-5, inform user
    else: print("Sorry. ", strChoice, "is not an option.\nPlease choose an item 1-5 from the menu")

# close file
file.close()