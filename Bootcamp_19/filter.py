# a = [1, 3, 5, 6, 8, 10, 22, 240]
# d = []
# for i in a:
#     if i % 2 == 0:
#         d.append(i)
# print(d)


# def func(x):
#     return x % 2 == 0
#
#
#
# a = [1,2, 3, 5, 6, 8, 10, 22, 240]
# b = list(filter(func, a))
# print(b)


# def s(x):
#     return x % 3 == 0 and x % 2 == 0
#
#
# a = [1, 2, 5, 6, 8, 9, 10, 22, 240]
# b = tuple(filter(s, a))
# print(b)

#
# a = 'hello'
# b = ''.join(filter(str.isalpha, map(str.upper, a)))
# print(b)


# def f(x):
#     return x
#
# a = {'Bishkek': +996, 'Moskva': +7, 'Kazakstan': +7, 'Uzbekistan': +998}
# b = list(filter(f, a.values()))
# print(b)


# a = {"bishkek": 996,
#      "moscwa": +7,
#      "ozbekistan": +998,
#      "kazaxstan": +77}
# s = a.items()
# s = set(filter(lambda x: dict, s))
# print(s)

#
# a = ['hello', 12, False, 0, True, 'hi', 'how are you', {1, 2}, [3, 4]]
# b = list(filter(lambda x: isinstance(x, set), a))
# print(b)


# a = ["app",
#      'orange',
#      "banana",
#      'strawberry',
#      "cherry",
#      "paya",
#      "mango",
#      "waterlemon",
#      "lemn",
#      "limon"]
# s = list(filter(lambda z: len(z) >= 5, a))
# print(s)


# a = ['enter your name ', [56, 67], {123}, '456', False, True, 'how do you do']
# b = {x for x in a if type(x) == bool}
# print(b)


# a = ['apple',
#      'aprikot',
#      'banana',
#      'coconut',
#      'kivi',
#      'lemon',
#      'lime',
#      'mango',
#      'orange',
#      ]
#
# b = list(filter(lambda x:len(x)>= 5,a))
# print(b)

# strings = ["apple", "banana", "cherry", "date", "grape"]
# filtered_strings = [s for s in strings if 'a' in s]
# print(filtered_strings)
