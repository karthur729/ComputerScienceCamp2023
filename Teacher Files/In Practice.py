names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Isabella", "Jack"]

name = input("Enter a name:  ")

if(name in names):
    print(f'{name} is already in the names list')

else:
    print(f'{name} is not in list. Adding name.')
    names.append(name)


'''

text = "Python is a powerful programming language."

if "programming" in text: 

    print("Substring found!") 

else: 

    print("Substring not found.")
'''
