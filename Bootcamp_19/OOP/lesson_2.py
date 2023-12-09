# class Person:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def say_hello(self):
#         return f"hello {self.name}"
#
# my_class = Person('Asan', 23, 40000)
# print(my_class.age)
# print(my_class.say_hello())
# my_class.age = 24
# print(my_class.age)



# class Person:
#     def __init__(self, name, age, salary):
#         self._name = name
#         self._age = age
#         self._salary = salary
#
#     def say_hello(self):
#         return f"hello {self._name}"
#
# my_class = Person('Asan', 23, 40000)
# print(my_class._age)
# print(my_class.say_hello())
# my_class._age = 24
# print(my_class._age)



# class Person:
#     def __init__(self, name, age, salary):
#         self.__name = name
#         self.__age = age
#         self.__salary = salary
#
#     def getter(self):
#         return self.__name
#
#     def setter(self):
#         self.__age = 24
#         return self.__age
#
# my_class = Person('Asan', 23, 40000)
# print(my_class.getter())
# print(my_class.setter())



# class Adam():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, new_name):
#         self.new_name = new_name
#         return self.new_name
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, new_age):
#         self.new_age = new_age
#         return self.new_age
#
#
# adam = Adam('Sanjar', 19)
#
# # adam.set_age(20)
# print(adam.set_age(20))
# print(adam.set_name('Almaz'))





# class Adam():
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, new_name):
#         self._name = new_name
#
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, new_age):
#         self._age = new_age
#
#
#
#
# adam = Adam('Rustam', 16)
# print(adam.name, adam.age)


class MBank:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.__cash = 0
        self.__gold = False

    def verifications(self):
        self.__gold = True

    def get_cash(self):
        return f'Balance {self.__cash} som'

    def set_cash(self, x):
        self.__cash = self.__cash + x

    def info(self):
        return f'Name {self.name}\nSurname {self.surname}'


mb = MBank('Sedep', 'Almazova')
print(mb.info())
# print(mb.get_cash())
mb.set_cash(10000)
print(mb.get_cash())















