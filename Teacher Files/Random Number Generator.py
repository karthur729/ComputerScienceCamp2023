import random

random_number = random.randint(1, 100)
print("The random number is: ", random_number)

for x in range(30):
    print(random.randint(1, 100))

fruits = ['apple', 'banana', 'orange', 'kiwi']
random_fruit = random.choice(fruits)
print(random_fruit)

