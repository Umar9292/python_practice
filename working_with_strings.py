# This will ignore the first and the last letter
# name = 'Jennifer'
# print(name[1:-1])

# If we want to write a multi line string we'll user three ''' marks
# e.g

# text = '''
# Hi, Mike
#
#     We are pleased to announce that you are selected.
#
# Regards:
# The support team.
# '''
#
# print(text)

# If we want to write dynamic strings
# firstName = 'Mike'
# lastName = 'Daniels'
# msg = f'{firstName} [{lastName}] is a coder'
# print(msg)

# Other functions
course = 'Python for beginners'
print(len(course))
print(course.upper())
print(course.lower())

# Finds the index of a character
print(course.find('o'))

print(course.replace('beginners', 'Absolute Beginners'))
print('Python' in course)
