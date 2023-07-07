while True:
    user_input = input("Enter a whole number greater than zero: ")

    if user_input.isdigit():
        number = int(user_input)
        if number > 0:
            print("Valid input! You entered:", number)
            break
        else:
            print("Please enter a number greater than zero.")

    else:
        print("invalid input. Please enter a valid whole number.")
