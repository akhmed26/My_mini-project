import random as r

print('\n\n\t       Добро пожаловать в числовую угадайку!\n')

#* Игра будет идти до того пока пользователь не угадает загаданное число или после того как он угадает число напишет input() != да
while True: 
    
    #! Проверяем на ОТ и ДО 
    def is_ot_do():
        while True:
            otd = digit('от')
            dot = digit('до')
            if otd < dot:
                return otd, dot
            else:
                print('Число "ОТ" должно быть МЕНЬШЕ числа "ДО"')
                
    #! Проверяет являеться то что ввел полльзователь число (от или до)
    def digit(z): 
        x = input(f'\nВведите цифру {z} : ')
        while True:
            if x[0] == '-':
                if x.replace('.', '', 1).replace('-', '', 1).isdigit():
                    return int(x)
                else:
                    print('А может быть все-таки введем целое число')
                    x = input(f'\nВведите цифру {z} : ')
            else:
                if x.replace('.', '', 1).isdigit():
                    return int(x)
                else:
                    print('А может быть все-таки введем целое число')
                    x = input(f'\nВведите цифру {z} : ')
            
    
    #! Проверяеться являеться ли число которое ввёл пользователь от или до(чила которого ввёл)
    def dig(ot=1, do=100): 
        x = input('Введите цифру: ')
        while True:
            if len(x) >= 1:
                if x[0] == '-':
                    if x.replace('.', '', 1).replace('-', '', 1).isdigit() and int(ot) <= int(x) <= int(do) + 1:
                        return int(x)
                    else:
                        print(f'А может быть все-таки введем целое число от {ot} до {do}?')
                        x = input('Введите цифру: ')
                else:
                    if x.replace('.', '', 1).isdigit() and int(ot) <= int(x) <= int(do) + 1:
                        return int(x)
                    else:
                        print(f'А может быть все-таки введем целое число от {ot} до {do}?\n')
                    x = input('Введите цифру: ')
            else:
                x = input('Введите цифру: ')
                    
     #! Гемплей и режим игры
    def gameplay():
        if input('\n\tДля начал игры выберете режим с которого хотите играть\n\nРежим 1: Сами выбираете от какого до какого числа загадывать\n\nРежим 2: Угадайка сама выбирает от 1 до 100\n\nВаш выбор: ') != '1':
            total = 0
            rand = r.randint(1, 101)
            while True:
                s = dig()
                if s == rand:
                    print(f'Ураа вы выйграли Поздравялем!\nУ вас ушло {total} попыток!')
                    break
                elif s < rand:
                    print('Больше...\n')
                    total += 1
                else:
                    print('Меньше...\n')
                    total += 1
        else:
            numbers = is_ot_do()
            total = 0
            otd = numbers[0]
            dot = numbers[1]
            print('\nПрограмма загадала число\n')
            rand = r.randrange(otd, dot + 1)
            while True:
                s = dig(otd, dot)
                if s == rand:
                    print(f'\nУраа вы выйграли Поздравялем!\nУ вас ушло {total + 1} попыток!\n')
                    break
                elif s < rand:
                    print('\nВаше число меньше задуманного\n')
                    total += 1
                else:
                    print('\nВаше число больше задуманного\n')
                    total += 1
    
    gameplay()
    
    #! Хочет ли пользователь сыграть снова
    flag_game = input('\nХотети сыграть ещё раз?\n').lower()
    if flag_game == 'нет' or flag_game == 'no': 
        print('\nСпасибо за игру жду тебя скоро')
        break
    else:
        gameplay()