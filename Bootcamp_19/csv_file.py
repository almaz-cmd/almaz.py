import csv

# a = ["значение1", "значение2", "значение3"]
#
# with open("data.csv", "w", newline='', encoding='utf-8') as file:
#     writer = csv.writer(file, delimiter=',')
#     writer.writerow(a)



# import csv
#
# name = [
#     ["Ученик 1", 170],
#     ["Ученик 2", 165],
#     ["Ученик 3", 175],
#     ["Ученик 4", 180],
#     ["Ученик 5", 160]
# ]
#
# with open("data.csv", "w", encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(name)


# with open('data.csv', mode='r') as file:
#     reader = csv.reader(file)






# users_data = [
#     ['user_1', 'address_1'],
#     ['user_2', 'address_2'],
#     ['user_3', 'address_3'],
# ]
#
# for i in users_data:
#     with open('data.csv', "a") as file:
#         writer = csv.writer(file)
#         writer.writerow(i)


# with open("data.csv", "r") as file:
#     reader = csv.reader(file)
#     for i in reader:
#         print(i)


# import csv
#
# def read_csv(filename):
#     data = []
#     try:
#         with open(filename, 'r', newline='') as file:
#             csv_reader = csv.reader(file)
#             for row in csv_reader:
#                 data.append(row)
#     except FileNotFoundError:
#         print(f"Файл {filename} не найден.")
#     return data
#
# def calculate_total(data, column_index):
#     total = 0
#     for row in data[1:]:  # Пропустить заголовок
#         try:
#             amount = float(row[column_index])
#             total += amount
#         except (ValueError, IndexError):
#             print(f"Ошибка при обработке строки: {row}")
#     return total
#
# income_data = read_csv('income.csv')
# expenses_data = read_csv('expenses.csv')
#
# if income_data and expenses_data:
#     total_income = calculate_total(income_data, 1)  # Предполагается, что сумма во втором столбце
#     total_expenses = calculate_total(expenses_data, 1)
#     balance = total_income - total_expenses
#     print(f"Баланс: {balance}")
#
#     report_data = [['Тип', 'Сумма'], ['Доходы', total_income], ['Расходы', total_expenses], ['Баланс', balance]]
#
#     with open('financial_report.csv', 'w', newline='') as file:
#         csv_writer = csv.writer(file)
#         csv_writer.writerows(report_data)

########

# import csv
#
#
# data = [
#     ['Имя', 'Рост'],
#     ['Анна', 165],
#     ['Петр', 178],
#     ['Мария', 162],
#     ['Иван', 175],
#     ['Елена', 170]
# ]
#
# with open("student_heights.csv", "w", newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
#

# def find_tallest_student(filename):
#     tallest_student = None  # Начальное значение для самого высокого ученика
#
#     with open(filename, 'r', newline='') as file:
#         csv_reader = csv.reader(file)
#
#         # Пропустить заголовок, если он есть
#         next(csv_reader, None)
#
#         for row in csv_reader:
#             student_name = row[0]  # Предполагается, что имя находится в первом столбце
#             student_height = float(row[1])  # Предполагается, что рост находится во втором столбце
#
#             if tallest_student is None or student_height > tallest_student['height']:
#                 tallest_student = {'name': student_name, 'height': student_height}
#
#     return tallest_student
#
#
# filename = 'student_heights.csv'  # Замените на имя вашего CSV-файла
# tallest_student = find_tallest_student(filename)
#
# if tallest_student is not None:
#     print(f"Самый высокий ученик: {tallest_student['name']} с ростом {tallest_student['height']} см.")
# else:
#     print("CSV-файл не содержит данных.")

