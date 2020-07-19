house_price = 1000000
good_credit = True

if good_credit:
    # this will give us the 10% of the house price
    down_payment = 0.1 * house_price
else:
    # this will give us the 20% of the house price
    down_payment = 0.2 * house_price

print(f'Down Payment will be: ${round(down_payment)}')
