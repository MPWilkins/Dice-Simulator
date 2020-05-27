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
    Print("7. D100")
    Print("8. Quit")
    select = int(input("Select a Number: "))
    # First batch will not include modifiers
    if select == 1:
        di_Four()
    elif select == 2:
        di_Six()
    elif select == 3:
        di_Eight()
    elif select == 4:
        di_Ten()
    elif select == 5:
        di_Twelve()
    elif select == 6:
        di_Twenty()
    elif select == 7:
        di_Hundred()
    elif select == 8:
        exit
    else:
        print("Invalid Number. Please select a Valid Number.")
        selectionMenu()
        
def di_Four():
    print(random.randint(1, 4))
    
def di_Six():
    print(random.randint(1, 6))
    
def di_Eight():
    print(random.randint(1, 8))
    
def di_Ten():
    print(random.randint(1, 10))
    
def di_Twelve():
 print(random.randint(1, 12))
    
def di_Twenty():
    print(random.randint(1, 20))
    
def di_Hundred():   
    print(random.randint(1, 100))
        
# run program
selectionMenu