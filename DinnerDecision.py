#---------------------------------------------------#
# Title: Dinner Decision
# Purpose:  Writes binary data to dinner.dat.
#           Generates a dinner menu by randomly
#           selecting a listed food item from each
#           category.
# Dev: Marie Augustine
# Date: May 12, 2019 (Mother's Day)
# ChangeLog:
# MarieAugustine, 5/12/2019, Created script
#---------------------------------------------------#


import pickle
import random

# object file variable
file = open("dinner.dat","wb")

# create food categories and items within each category
protein = ["beans", "eggs", "turkey", "chicken"]
grain = ["rice", "farro", "toast", "pasta", "tortilla", "pizza crust"]
vegetable = ["broccoli", "carrots", "peas", "salad", "asparagus"]
yummy = ["avocado", "cheese", "olives", "sauce", "fruit"]

# dump each category to the dinner.dat file
pickle.dump(protein,file)
pickle.dump(grain,file)
pickle.dump(vegetable,file)
pickle.dump(yummy,file)
file.close()

def Menu(satisfiedq):
    """Unpickles the file, then generates random menu by choosing one item from each category list at random"""
    # open the file
    file = open("dinner.dat","rb")

    # load each category from the dinner.dat file
    protein = pickle.load(file)
    grain = pickle.load(file)
    vegetable = pickle.load(file)
    yummy = pickle.load(file)

    # create a variable to use for index to identify selected item/food in each category
    pchoice = random.randint(0,(len(protein)-1))
    gchoice = random.randint(0,(len(grain)-1))
    vchoice = random.randint(0,(len(vegetable)-1))
    ychoice = random.randint(0,(len(yummy)-1))

    # display the selected menu
    print("\nTonight's menu will be:\n")
    print(protein[pchoice].title(), " and ", vegetable[vchoice].title(), " on ", grain[gchoice].title(), " with ", yummy[ychoice].title(), end=".")

    # user input variable that will determine if the program repeats or ends depending on satisfaction with the menu
    satisfied = input(satisfiedq).lower()

    # close file
    file.close()

    # return the value of the user input value
    return satisfied

satisfied = []

print("Don't feel like deciding on dinner tonight?\tNo Problem!")

# loop to allow program to keep generating menus until user is satisfied
try:
    while satisfied != "y":
        satisfied = Menu("\n\nAre you satisfied with your Menu? [y/n]")
    else:
        print("\nEnjoy your dinner!")

# displays any errors
except Exception as e:
     print("\nThere is an error! The error is ", e)
     # closes the file if it's still open
     if(file != None):
        file.close()
        print("\nThe program has ended")