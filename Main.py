from Grocery import Grocery

#Fields
groceryList = []

#Introduction
print("Unwelcome to your grocery list. Add groceries by typing \"add \" and then the name of your grocery item. Press q to quit like a refrigerated chicken.")

#Print all of the groceries in the grocery list
def printGroceries():
    for g in groceryList:
        print(str(g.name))

#This is to undo the split but minus the first stuff
def fuseString(inputList):
    returnString = ""
    #Add the word and a space to the return string for every word found in the list
    for i in range(len(inputList)):
        returnString = returnString + inputList[i] + " "
    #Trim the last space
    returnString = returnString[0:-1]
    #Return the string
    return returnString

#program loop
while(True):

    #split the input into a list
    iList = input().split()
    #Save the length of the list
    iListLen = len(iList)
    
    #Quit if the input is q
    if iListLen == 1 and (iList[0].upper() == "Q"):
        break
    #List the groceries if the only entry is "list"
    elif iListLen == 1 and iList[0].upper() == "LIST":
        #Print the names of all of the groceries on the list
        printGroceries()
        print("")
        #Insult
        print("Ooooo, looks like my grandma\'s groceries")
    #Add a grocery to the grocery list!
    elif iListLen > 1 and iList[0].upper() == "ADD":
        #Fuse the last bit of the list in case of grocieries like "Chocolate Cake", but removing the first part "add"
        groceryName = fuseString(iList[1:])
        #Create the grocery item
        g = Grocery(groceryName)
        #Add the grocery item to the grocery list
        groceryList.append(g)
        #Insult
        print("Congratulations bannana pie, you added your first grocery. If you actually care, type \"list\" to see your rotten food")
    else:
        #Notification insult
        print("That\'s not a command you bucket head! Try again correctly this time.")

print("Smell you rotten food later.")