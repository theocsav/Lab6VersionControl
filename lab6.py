"""
Author: Vasco Hinostroza
Date: 03/19/24
Description: Lab 6: Version Control
"""


def main():
    encoded_password = ""
    while True:
        print_menu()
        option = input("Please enter an option: ")
        if option == '3':
            break
        else:
            encoded_password = option_selector(option, encoded_password)


def encode(password):
    encoded_password = ""
    for num in password:
        encoded_password += str(int(num) + 3)
    return encoded_password


def option_selector(option, encoded_password):
    match option:
        case '1':
            while True:
                password = input("Please enter your password to encode: ")
                if password.isnumeric():
                    break
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        case '2':
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.\n")
            pass
        case default:
            print("Error. Incorrect selection.\n")
    return encoded_password


def decode(encoded_password):
    pass


def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")


if __name__ == "__main__":
    main()
