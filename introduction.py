# write a function that takes 2 inputs (2 people), and introduces one to another
# Prompt the user for 2 names
# call your dunction, which should then print and introduvtion
    # introduce one person to the other

def introduction(nameA, nameB):
    print(nameA + " meet " + nameB + ".\nAnd " +nameB + " meet " + nameA + ". ")

nameA = input("Enter your name\n: ")
nameB = input("Enter your name\n: ")
introduction(nameA, nameB)