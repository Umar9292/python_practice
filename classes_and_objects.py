from Student import Student

student1 = Student('Mike', 'OS', 2.9, True)
student2 = Student('John', 'OS', 3.9, True)

# print(student1.name + '\n', student1.major)

print(student1.on_honour_roll())
print(student2.on_honour_roll())
