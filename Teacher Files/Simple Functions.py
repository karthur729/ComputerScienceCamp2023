# Function to print a simple message.
def message():
    print("Hello how are you?")

message()
message()


# Function to give a greeting to a user.
def greeting():
    name = input("What is your name: ")
    print(f'Good morning {name}.')

greeting()
greeting()


name1 = 'John'
name2 = 'David'
# Passing a user name into a funciton
def personal_greeting(name):
    print(f'Have a nice day {name}.')

personal_greeting(name1)
personal_greeting(name2)

