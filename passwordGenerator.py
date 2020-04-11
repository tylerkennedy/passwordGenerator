import string
import random

print("Welcome to TK's Password Generator")

def complexity_switcher(): # Function to allow user to choose the complexity of the password
    while True: # User input validation loop
        print("Choose password complexity")
        complexity_menu = { # Dictionary for user menu options
            1 : "1. Lowercase only",
            2 : "2. Upper and lowercase",
            3 : "3. Upper and lowercase and numbers",
            4 : "4. Upper and lowercase and numbers and symbols (most secure)"
        }
        character_set = { # Dictionary for character sets by complexity
            1 : string.ascii_lowercase,
            2 : string.ascii_letters,
            3 : string.ascii_letters + string.digits,
            4 : string.ascii_letters + string.digits + "@!#$&*?-+" 
        }
        for option, output in complexity_menu.items():
            print(output) # Print menu
        try:
            complexity = int(input()) # validate user input
            return character_set[complexity] # return choosen character set
        except:
            print("Not a valid option. Try again") # reprompt user for invalid input
            continue
        else:
            break # exit loop 

def get_password_length(): # Function to allow user to choose the length of the password
    while True: # user input validation loop
        try:
            password_length = int(input("Enter password length: ")) # validate user input
            return password_length
        except:
            print("Not a valid option. Try again") # reprompt user for invalid input
            continue
        else:
            break

def use_dashes():
    while True:
        dashes_options = {"y" : True, "n" : False}
        try:
            dashes = str(input("Segment password with dashes (Ex: 1234-5678-9abc) y/n: "))
            return dashes_options[dashes.lower()]
        except:
            print("Not a valid option. Try again")
        else:
            break
# Include dashes
# Using words from a dictionary
# Replacing characters with symbols

character_choice = complexity_switcher()
password_length = get_password_length()
dashes = use_dashes()

def generatePassword(length, characters):
    password = ""
    while len(password) < length:
        password = password + random.choice(characters)
    print(password)
    return password


generatePassword(password_length, character_choice)


