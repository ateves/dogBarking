'''this is the random math package'''
import random

'''this is our list that has three puppy's names inside of it'''
puppyNamesList = ["Cobbler", "Lambda", "Giant"]

'''this is method for making the puppy's bark a number of times'''
def puppyBarks(puppyNamesList):
    
    '''number can change but this is the minimum number of barks/woofs'''
    minimumWoofs = 5
    
    '''for loop we will use to allow the puppies in puppyNamesList to bark a number of times'''
    for x in puppyNamesList:

        '''this line of code determines a 
        random number between the minimum 
        and the maximum (10)'''
        currentRandomNumber = random.randint(minimumWoofs,10)
        
        '''This prints the puppy's name as well as the 
        number of times that puppy has barked'''
        print("%s barks %s times!" % (x, currentRandomNumber))

'''call for our puppy's barks'''
puppyBarks(puppyNamesList)

'''This program was written by ANTHONY T'''