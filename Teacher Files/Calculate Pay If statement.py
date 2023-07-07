pay = 15
john = 50

if john < 40:
    total_pay = john * pay
    print(f'John worked {john} hours. His netpay is {total_pay} dollars. He is below the 40 hour work week.')
elif john == 40:
    total_pay = john * pay
    print(f'John worked {john} hours. His netpay is {total_pay} dollars. He worked the standard work week.')
else:
    overtime = john - 40
    total_pay = 40 * pay + (overtime * 15 * 1.5)
    print(f'John worked {john} hours. His netpay is {total_pay} dollars. He worked {overtime} hours of overtime.')

