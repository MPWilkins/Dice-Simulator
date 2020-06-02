#This should allow me to find a random int in a set range.
import random

def selectionMenu():
    print ("Which kind of D&D Di are you wanting to roll?")
    print("1. D4")
    print("2. D6")
    print("3. D8")
    print("4. D10")
    print("5. D12")
    print("6. D20")
    print("7. D100")
    print("8. Quit")
        
    select = int(input("Select a Di to Roll: "))
    
    # First batch will not include modifiers
    if select == 1:
        di_Four()
        roll_Again()
    elif select == 2:
        di_Six()
        roll_Again()
    elif select == 3:
        di_Eight()
        roll_Again()
    elif select == 4:
        di_Ten()
        roll_Again()
    elif select == 5:
        di_Twelve()
        roll_Again()
    elif select == 6:
        di_Twenty()
        roll_Again()
    elif select == 7:
        di_Hundred()
        roll_Again()
    elif select == 8:
        exit
    else:
        print("Invalid Number. Please select a Valid Number. \n")
        selectionMenu() # runs program again if outside of parameters
        
# Asks the user if another di should be rolled.
# for a multi=select statement with numberous input, use the keyword "in" instead of == and put the answers in a square bracket for the right answer.
def roll_Again():
    select = input("Would you like to roll another Di Y/N: ")
    if select in ['y', 'Y']:
        selectionMenu()
    elif select in ['n', 'N']:
        exit
    else:
        print("Please use either 'Y' or 'N.' \n")
        roll_Again()
    
# Place the modifier function here.
        
        
def di_Four():
    print(random.randint(1, 4), '\n')
    
def di_Six():
    print(random.randint(1, 6), '\n')
    
def di_Eight():
    print(random.randint(1, 8), '\n')
    
def di_Ten():
    print(random.randint(1, 10), '\n')
    
def di_Twelve():
 print(random.randint(1, 12), '\n')
    
def di_Twenty():
    print(random.randint(1, 20), '\n')
    
def di_Hundred():   
    print(random.randint(1, 100), '\n')
        
# run program
selectionMenu()