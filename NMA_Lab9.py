def encode(password):
    new_pass = ''
    for char in password:
        new_digit = (int(char) + 3) % 10
        new_pass += str(new_digit)
    return new_pass
