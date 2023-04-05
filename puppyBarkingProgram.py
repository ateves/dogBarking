import random

puppyNamesList = ["Dexter", "Happy", "Cooper"]

def puppyBarks(puppyNamesList):
    
    minimumWoofs = 5
    
    for x in puppyNamesList:
        currentRandomNumber = random.randint(minimumWoofs,10)
        print("%s barks %s times!" % (x, currentRandomNumber))

puppyBarks(puppyNamesList)
