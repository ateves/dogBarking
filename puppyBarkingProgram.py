import random

puppyNamesList = ["Cobbler", "Lambda", "Giant"]

def puppyBarks(puppyNamesList):
    
    minimumWoofs = 5
    
    for x in puppyNamesList:
        currentRandomNumber = random.randint(minimumWoofs,10)
        print("%s barks %s times!" % (x, currentRandomNumber))

puppyBarks(puppyNamesList)

#This program was written by ANTHONY T