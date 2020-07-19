class Mammal:
    def walk(self):
        print('Walking')


class Dog(Mammal):
    def bark(self):
        print('Barking')


class Cat(Mammal):
    pass


dog = Dog()
dog.bark()

cat = Cat()
cat.walk()
