class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print('Недопустимый возраст')

    def display(self):
        print('my name is %s' % self.__name, 'my age is %d' % self.__age)


p1 = Person('Igor')

p1.age = -62
print(p1.display())



