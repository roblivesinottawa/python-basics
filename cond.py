# is_hot = False
# is_cold = True
#
# if is_hot:
#     print("it's a hot day")
#     print('Drink lots of water')
# elif is_cold:
#     print('it is cold')
#     print('wear warm clothes')
# else:
#     print('it is a nice day')

# house = 1000000
# good_credit = False
#
# if good_credit:
#     down_payment = 0.1 * house
#     print('You need to put down 10%')
# else:
#     down_payment = 0.2 * house
#     print('You need to put down 20%')
# print(f"Down payment: ${down_payment}")

# has_high_income = False
# has_good_credit = True
#
# if has_high_income or not has_good_credit:
#     print('You are eligible for a loan')

# temperature = 34
#
# if temperature > 30:
#     print("it's a hot day")
# else:
#     print("it's not a hot day")

# name = input('what is your name? ')
#
# if len(name) < 3:
#     print('name must be at least 3 characters long')
# elif len(name) > 50:
#     print('name must be a max of 50 characters')
# else:
#     print('name looks good')


weight = int(input('weight: '))
measure = input('(L)bs or (K)g: ')

if measure.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")



