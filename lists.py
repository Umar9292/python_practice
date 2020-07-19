# numbers = [23, 4, 90, 4, 67, 77, 100]
# biggest_number = numbers[0]
#
# for num in numbers:
#     if num > biggest_number:
#         biggest_number = num
#
# print(biggest_number)

# Exercise for removing duplicates ina list

numbers = [2, 2, 5, 6, 7, 7, 67, 77, 53]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)
