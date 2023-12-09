import datetime

x = {'pin': '1709', 'balance': 100000}


def check_pin(pin):
    return pin.isdigit()


def change_pin(account):
    new_pin = input('Введите новый пинкод!')
    if new_pin.isdigit() and len(new_pin) == 4:
        account['pin'] = new_pin
        print('Пин-код изменен!')
    else:
        print('Пин код должен состоять из 4 цифр!')


pin_attempts = 0
while pin_attempts < 3:
    pin = input('Введите пин код / Enter PIN: ')
    if check_pin(pin) and pin == x['pin']:
        break
    else:
        print('Пин код введен не правильно! / Invalid PIN')
        pin_attempts += 1
    if pin_attempts == 3:
        print('Обратитесь в Тех.Поддержку!:0777224880')
        exit()
while True:
    print('Выберите язык. Slect language:')
    print('1.Кыргызча')
    print('2.Русский')
    print('3.English')
    lang_choice = input()
    if lang_choice == '1':
        language = 'Кыргызча'
        break
    elif lang_choice == '2':
        language = 'Русский'
        break
    elif lang_choice == '3':
        language = 'English'
        break

balance = x['balance']

while True:
    print(f'Здраствуйте!')
    print('1.Пооверка баланса:')
    print('2.Снятие наличных:')
    print('3.Выход:')
    print('4.Изменить пинкод:')
    choice = input('Введите номер действия:')

    if choice == "1":
        print(f'Баланс: {balance}')
    elif choice == "2":
        a = 500, 1000, 2000, 5000
        print(f'Выдача {a} сумма:')
        b = int(input('Введите сумму выдачи:'))
        if b >= 200 and b <= balance and b % 100 == 0 and b % 100 != 100 and b % 100 != 300:
            balance -= b
            print(f'Сумма {b} выведен!.')
            c = input('Чек?')
            if c == 'да':

                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("\nЧек:")
                print("Банкомат Bakai Bank")
                print(f"Сумма: {b} сом.")
                print(f"Остататок:{balance}")
                print(f"Дата и Время: {timestamp}")
                print("----------------------------------------\n")
        else:
            print('Неправильная сумма!')
    elif choice == "3":
        print('Спасибо за выбор нашего банкомата!')
        break
    elif choice == "4":
        change_pin(x)
    else:
        print('Неправильный ввод повторите!')

    continue_choice = input('Продолжить?(да/нет): ')
    if continue_choice.lower() == 'жок':
        print('Спасиобо за выбор нашего банкомата!')
        break