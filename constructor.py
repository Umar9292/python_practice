class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'I am {self.name}')


john = Person('John Smith')
john.talk()

bob = Person('Bob Smith')
bob.talk()
