weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'L':
    weight = 0.45 * weight
    print(f'You are {round(weight)} kilograms')
elif unit.upper() == 'K':
    weight = weight / 0.45
    print(f'You are {round(weight)} pounds')
else:
    print('You entered a wrong unit')
