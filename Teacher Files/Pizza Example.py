cost_of_pizza = 7.5
pizza = input("What is your favorite type of pizza?")
pizza_number = input("How many pizzas would you like to order?")
pizza_number = int(pizza_number)
total_cost = cost_of_pizza * pizza_number
print(f'Your favorite pizza is {pizza}. The total cost of your order is ${total_cost}.')
