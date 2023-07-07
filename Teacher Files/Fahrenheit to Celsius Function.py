def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temp1 = 50
temp2 = 89

print(f'{temp1} degrees fahrenheit is {fahrenheit_to_celsius(temp1)} in celsius.')
print(f'{temp2} degrees fahrenheit is {fahrenheit_to_celsius(temp2)} in celsius.')


