
# This is to append some stuff in an existing file
# employee_file = open('employees.txt', 'a')

# This will override everything in the file and will
# put only the new stuff in. So basically it will remove
# the old stuff and put in the new stuff.
employee_file = open('employees.txt', 'w')

employee_file.write('\nToby - Human Resource')

employee_file.close()
