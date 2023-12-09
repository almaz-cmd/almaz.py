# a = {'name': 'Deniz', 'age': 15, 'salary': 55000}
# print(type(a))

# a = {'name': 'Deniz', 'age': 15, 'salary': 55000}
# for i, j in a.items():
#     if j == 15:
#         continue
#     print(i, j)

# a = {'kartoshka': 45, 'alma': 120, 'limon': 60}
# b = 65
# for i,j in a.items():
#     b = b + j
# print(b)


# IK = ['брюки',
#       'очки',
#       'плавки',
#       'ноутбук',
#       'зарядниик',
#       'загар крем',
#       'футболка',
#       'кроссы',
#       'брюки',
#       'очки',
#       'плавки',
#       'загар крем',
#       'футболка',
#       'кроссы',
#       'брюки',
#       ]
#
# # d = set(IK)
# # print(d)
#
#
# d = []
# home = []
# for i in IK:
#     if i in d:
#         home.append(i)
#     else:
#         d.append(i)
# print(d)
# print(f"uydo kaldy {home} ushular")


# a = int(input('num:'))
# b = 1
# for i in range(1, a + 1):
#     b = b * i
#
# print(b)


# x = [1,24,214,21,56667877887,2532,32,67]
# v = [0]
# for i in x:
#     if i > v[-1]:
#         v.pop(-1)
#         v.append(i)
# print(v)

# text = "apple,banana,cherry,orange"
# fruits = text.split('+', maxsplit=2)
# print(fruits)  # ['apple', 'banana', 'cherry,orange']


# text = "apple,banana,cherry"
# fruits = text.split('=')
# print(fruits)  # ['apple', 'banana', 'cherry']
