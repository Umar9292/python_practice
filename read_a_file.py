

employee_file = open('employees.txt', 'r')

# print(employee_file.readable())
# print(employee_file.read())

# By writing read line twice it will read the first line
# and then will move the cursor to the next line
# So the the next read line function will print the next line
print(employee_file.readline())
print(employee_file.readline())

# This function will give an array(list) of all the lines
# print(employee_file.readlines())
# print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)

employee_file.close()
