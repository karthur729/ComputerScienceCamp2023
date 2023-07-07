while True:
    password = input("Enter a secure password: ")

    # Password criteria: at least 8 characters, with at least one uppercase letter and one digit
    if len(password) >= 8:
        has_uppercase = False
        has_digit = False

        for char in password:
            if char.isupper():
                has_uppercase = True
            if char.isdigit():
                has_digit = True

        if has_uppercase and has_digit:
            print("Password is secure. Access granted!")
            break
        else:
            print("Password is not secure. Make sure it has at least one uppercase letter and one digit.")
    else:
        print("Password is not secure. Make sure it has at least 8 characters.")
