__author__ = 'Evan Wolting'

GRADE_A = 'Your Grade is a A\nYour amazing!'
GRADE_B = 'Your Grade is a B\nYour doing fine!'
GRADE_C = 'Your Grade is a C\nYour Average!'
GRADE_D = 'Your Grade is a D\nYour below Average, you need to Improve.'
GRADE_F = 'Your Grade is a F\nYour Failing! You better improve to pass.'

NUM1 = 90
NUM2 = 80
NUM3 = 70
NUM4 = 60

score = float(input('Enter_Score:'))
if score >= NUM1:
    print(GRADE_A)
elif score >= NUM2:
    print(GRADE_B)
elif score >= NUM3:
    print(GRADE_C)
elif score >= NUM4:
    print(GRADE_D)
else:
    print(GRADE_F)



