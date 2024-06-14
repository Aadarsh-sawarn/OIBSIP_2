# Creating the RANDOM PASSWORD GENERATOR 


# 'random': For generating random choices.
import random

# 'string' : For accesing sets of characters (e.g.,letters,digits,punctuation)
import string

#create function generate_password
def generate_password(min_length, numbers=True, speical_characters=True):

    # variable s1 for letters
    s1 = string.ascii_letters

    #variable s2 for numbers
    s2 = string.digits

    #variable s3 for symbols
    s3 = string.punctuation

    characters = s1
    if numbers:
        characters +=s2
    if speical_characters:
        characters += s3

    
    password = ""
    meets_criteria = False
    has_number = False
    has_speical = False


    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in s2:
            has_number = True
        elif new_char in s3:
            has_speical = True

        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if speical_characters:
            meets_criteria = meets_criteria and has_speical
    
    return password

# Getting input from user

min_length = int(input("Please enter length of the password: "))
has_number = input("Do you want to add numbers in your password (yes/no)?").lower()=="yes"
has_speical = input ("Do you want to add some speical characters in your password (yes/no)?").lower() =="yes"
password = generate_password(min_length,has_number,has_speical)
print("Your password is: " , password)
