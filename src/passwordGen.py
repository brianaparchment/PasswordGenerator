#Password Generator
import string
import random

def passGen():
    charUpper = string.ascii_uppercase #str w/ the uppercase alphabet
    uppercase = [] #list of uppercase letters
    for elem in charUpper:
        uppercase.append(elem)

    charLower = string.ascii_lowercase #str w/ lowercase alphabet
    lowercase = [] #list of lower case letters
    for elem in charLower:
        lowercase.append(elem)

    #list of symbols
    symbols = ["~","!","@","$","%","^","&","*","(",")","_","-","+","=","<",">",".","/","?",",",":",";"]
    #list of numbers
    numbers = [0,1,2,3,4,5,6,7,8,9]

    letters = []
    #selects 4 random str from each list
    for elem in range(4):
        letters.append(random.choice(lowercase))
        letters.append(random.choice(uppercase))
    specialChar = []
    #selects 2 random str from each list
    for elem in range(2):
        specialChar.append(random.choice(numbers))
        specialChar.append(random.choice(symbols))
    
    #combine lists  
    passList = letters + specialChar
    #shuffle list
    random.shuffle(passList)

    #convert list to str
    password = ''.join(map(str,passList))


    welcome = "Welcome to the Password Generator"
    print(welcome)

    user_input = input("Press Enter to Get a New Password\n")
    print("Password: ",password)
passGen()