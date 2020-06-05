#Imports the random library.
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
        
    select = int(input("Select one of the above options: "))
    while True:
        try:
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
        except ValueError:
            print("Invalid Number. Try again. \n")
            continue # This continues the use of the program if there is a value error.
        else:
            if select == 8:
                quit() #Using quit will exit the entire program. Study some more on sys.exit(), seems that is good practice.
        
# Asks the user if another di should be rolled.
# for a multi-select statement with numberous input, use the keyword "in" instead of == and put the answers in a square bracket for the right answer.
def roll_Again():
    select = input("Would you like to roll another Di Y/N: ")
    if select in ['y', 'Y']:
        selectionMenu()
    elif select in ['n', 'N']:
        quit()
    else:
        print("Please use either 'Y' or 'N.' \n")
        roll_Again()
    
# Place the modifier function here.
def modifier():
    while True:
        try:
            num = int(input("Input numerical modidifer (If no modifier, use 0): "))
        except ValueError:
            print ("Invalid Entry. Try Again.")
            continue
        else:
            return num      
        
#Selection of di
def di_Four():
    newNum = modifier()
    randomNum = random.randint(1, 4)
    print("You rolled:", randomNum)
    print("Your Modifier:", newNum)
    totalRoll = randomNum + newNum
    print("Roll with modifier:", totalRoll, '\n')
    
def di_Six():
    newNum = modifier()
    randomNum = random.randint(1, 6)
    print("You rolled:", randomNum)
    print("Your Modifier:", newNum)
    totalRoll = randomNum + newNum
    print("Roll with modifier:", totalRoll, '\n')
    
def di_Eight():
    newNum = modifier()
    randomNum = random.randint(1, 8)
    print("You rolled:", randomNum)
    print("Your Modifier:", newNum)
    totalRoll = randomNum + newNum
    print("Roll with modifier:", totalRoll, '\n')
    
def di_Ten():
    newNum = modifier()
    randomNum = random.randint(1, 10)
    print("You rolled:", randomNum)
    print("Your Modifier:", newNum)
    totalRoll = randomNum + newNum
    print("Roll with modifier:", totalRoll, '\n')
    
def di_Twelve():
    newNum = modifier()
    randomNum = random.randint(1, 12)
    print("You rolled:", randomNum)
    print("Your Modifier:", newNum)
    totalRoll = randomNum + newNum
    print("Roll with modifier:", totalRoll, '\n')
    
def di_Twenty():
    newNum = modifier()
    randomNum = random.randint(1, 20)
    print("You rolled:", randomNum)
    print("Your Modifier:", newNum)
    totalRoll = randomNum + newNum
    print("Roll with modifier:", totalRoll, '\n')
    
def di_Hundred():
    randomNum = random.randint(1, 100)   
    print("You rolled:", randomNum, '\n')
        
# run program
selectionMenu()