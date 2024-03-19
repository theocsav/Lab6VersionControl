"""
File: version_control.py
Author: Johan Fortus
Date: 3/19/24
Description: Lab 06 - Version Control
"""

# Main Function
def main():
    user_input = None
    encoded_password = None
    while user_input != '3':
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        user_input = input("Please enter an option: ")

        if user_input == '1':
            user_password = input("Please enter your password to encode: ")
            encoded_password = encode(user_password)
            print("Your password has been encoded and stored!")
            print()
        
        if user_input == '2':
            # print(f"The encoded password is {encoded_password}, and the original password is {}")
            # print()
            pass


# Encode Function
def encode(password):
    encoded_password = ''
    for i in password:
        digit = int(i) + 3
        if digit > 10:
            digit = str(digit)[1:]
        encoded_password += str(digit)
    return encoded_password


if __name__ == "__main__":
    main()
