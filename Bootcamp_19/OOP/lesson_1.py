# class Person:
#     name = 'Diana'
#     age = 25
#     position = 'Teacher'
#     salary = 40000
#
#     def say(self):
#         return f"hello {self.name}"
#
# d = Person()
# # print(d.position)
# print(d.say())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return f"hello {self.name}"

class Animals(Person):
    def say_2(self):
        return f"hello {self.name}"


p = Person('Diana', 25)
print(p.say())

d = Animals('recs', 3)
print(d.say_2())

