#  Passwrod Generate

import random

def Gener_Password(length):
    L_case_letters = 'abcdefghijklmnopqrstuvwxyz'
    U_case_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Digit = '0123456789'
    symbols = '!@#$%^&*()_+=-?><,./}{][:;'

    characters = L_case_letters +   U_case_letter + Digit + symbols

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_gener():
    length = int(input("\n\nEnter the length: "))
    
    password = Gener_Password(length)
    print("\nGenerated Password: {}\n\n".format(password))

password_gener()
