def encode(password):
    new_pass = ''
    for char in password:
        new_digit = (int(char) + 3) % 10
        new_pass += str(new_digit)
    return new_pass

def decode(password):
    decoded_pass = ''
    for char in password:
        new_digit = (int(char) - 3) % 10
        decoded_pass += str(new_digit)
    return decoded_pass

if __name__ == '__main__':
    stored_pass = None

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter the password to encode: ")
            stored_pass = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == "2":
            if stored_pass:
                decoded_password = decode(stored_pass)
                print(f"The encoded password is {stored_pass}, and the original password is {decoded_password}.\n")
        elif option == "3":
            break
