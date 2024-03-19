"""
File: version_control.py
Author: Johan Fortus
Date: 3/19/24
Description: Lab 06 - Version Control
"""

def main():
    pass

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
