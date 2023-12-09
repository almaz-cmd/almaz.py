# List comprehension
# from datetime import datetime
#
# now = datetime.now()
# a = []
# for i in range(1,30):
#     if i % 2 == 0:
#         a.append(i)
# print(a)
# d = datetime.now()
# s = d - now
#
#
# n = datetime.now()
# a = [i for i in range(1, 30) if i % 2 == 0]
# print(a)
# f = datetime.now()
#
# g = f - n
#
# result = s - g
# print(result)


# a = [i**2 for i in range(1, 30)]
# print(a)
#
# a = []
# for i in range(1,30):
#     a.append(i**2)
# print(a)

# d = [{i, j} for i in range(1, 20) for j in range(21, 40)]
# print(d)


# s = ['black', 'blue', 'orange', 'pink']
#
# d = [i.upper() for i in s]
# print(d)

# rows = 3
# cols = 4
# matrix = [[0 for _ in range(cols)] for _ in range(rows)]
# print(matrix)

# table = [[i * j for j in range(1, 11)] for i in range(1, 11)]
# result = table[2][3]  # 2, потому что индексы начинаются с 0
# print(result)

#
# n,m =int(input()),int(input())
# a = []
# for i in range(n):
#     a.append([0] * m)
#
# for i in range(n):
#     for j in range(m):
#         print(a[i][j], end=' ')
#     print(' ')
