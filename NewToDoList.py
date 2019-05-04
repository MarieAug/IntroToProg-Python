#---------------------------------------------------#
# Title: New To-Do List
# Purpose:  Program pulls data from ToDo.txt into a
#           list and allows user to display tasks and
#           corresponding priorities, add tasks/priorities,
#           remove tasks and save the data back to ToDo.txt
# Dev: Marie Augustine
# Date: May 3, 2019
# ChangeLog:
# MarieAugustine, 5/3/2019, Created script
#---------------------------------------------------#

# -- Data --#
# Global Variables
objFileName = "ToDo.txt"
lstTable = []

# -- Processing --#
# Create a Class for performing menu jobs
class MenuJobs(object):
    """Collection of functions that perform jobs a user selects from a menu"""

    # Step 1
    # When the program starts, load any data you have
    # in a text file called ToDo.txt into a python list and dictionary
    @staticmethod
    def readfile(objFileName):
        """Reads file and organizes into a dictionary and list"""
        objFile = open(objFileName, "r")
        dicRow = {}
        strData = ""
        for line in objFile:
            strData = line.split(",") # readline() reads a line of the data into 2 elements
            dicRow = {"Task":strData[0].strip(), "Priority":strData[1].strip()}
            lstTable.append(dicRow)
        objFile.close()
        return lstTable

    # Step 2
    # Display a menu of choices to the user (used book p.179 - ask_number() function)
    @staticmethod
    def menu(question, low = 1, high = 6):
        """Displays a menu of choices to the user and asks user to choose from the menu"""
        print(
            """
             Menu of Options
        1) Show current data
        2) Add a new item.
        3) Remove an existing item.
        4) Save Data to File
        5) Exit Program
        """)
        response = None
        while response not in range(low, high):
            response = int(input(question))
        return response

    # Step 3
    # Display all todo items to user
    # Don't need parameters for this function -- no input to pass.
    @staticmethod
    def showList():
        """Shows the current task list"""
        print("\n******* The current items ToDo are: *******")
        for item in lstTable:
            print(item["Task"] + "(" + item["Priority"] + ")")
        print("*******************************************")

    # Step 4
    # Add a new item to the list/Table - keep user input/output out of the function
    @staticmethod
    def addTask(taskq, priorityq):
        """User adds a new task and priority to the To-Do List"""
        task = str(input(taskq)).strip()
        priority = str(input(priorityq)).strip()
        dicRow = {"Task": task, "Priority": priority}
        lstTable.append(dicRow)


    # Step 5
    # Remove an item from the list/Table
    @staticmethod
    def removeTask(removeq):
        """User removes a task from the To-Do List"""
        strRemove = input(removeq).lower()
        blnItemRemoved = False  # Create a boolean Flag to return.
        intRowNumber = 0
        while (intRowNumber < len(lstTable)):
            if strRemove == str(list(dict(lstTable[intRowNumber]).values())[0]).lower(): # the values function creates a list!
                del lstTable[intRowNumber]
                blnItemRemoved = True
            # end if
            intRowNumber += 1
        # end for loop
        return blnItemRemoved

    # Step 6
    # Save tasks to the ToDo.txt file
    @staticmethod
    def savelist(choiceq):
        """User saves current list to text file"""
        # show current list
        MenuJobs.showList()
        # 5b Ask if they want save that data
        choice = str(input(choiceq)).strip().lower()
        if choice == "y":
            objFile = open(objFileName, "w")
            for dicRow in lstTable:
                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objFile.close()
            return choice
        else:
            return choice


# -- Display I/O --#
# Program reads ToDo.txt
MenuJobs.readfile(objFileName)

# While loop based on response from menu() function
while True:
    # User can see a Menu (Step 2)
    response = MenuJobs.menu("Choose a number from the Menu to perform that option: ")

    if response == 1:
        # User can see to do list (Step 3)
        MenuJobs.showList()

    # User can insert tasks (Step 4)
    elif response == 2:
        MenuJobs.addTask("Enter a new task: ","\nEnter priority, [low/high]: ")
        MenuJobs.showList()

    # User can remove tasks (Step 5)
    elif response == 3:
        blnItemRemoved = MenuJobs.removeTask("Please enter the task you wish to remove? ")
        # Display whether or not the task was successfully removed to the user
        if blnItemRemoved == True:
            print("\nThe task was removed.")
        else:
            print("\nI'm sorry, but I could not find that task.")
        MenuJobs.showList()

    # User can save to file (Step 6)
    elif response == 4:
        choice = MenuJobs.savelist("Are you sure you want to save this list to the file? (y/n): ")
        # Display whether or not the list saved to the user
        if choice == 'y':
            print("\nData saved to file!")
        else:
            print("\nNew data was NOT Saved, but previous data still exists!")

    # Step 7
    # User exits program
    elif response == 5:
        print("\nThe program has now been closed")
        break





