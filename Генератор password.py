import string as s 
from random import *

print('\nДОБРО ПОЖАЛОВАТЬ В ГЕНЕТАРОР ПАРОЛЕЙ!\n')

#! Цикл будет идти пока человек не напишет в конце starwith('н', 'n')
while True: 
    # ! Создание пароля Режим номер 2
    def pasword(big, lower, digit, simv, length):        
        pasw = []
        if any([big, lower, digit, simv]):      #! Проверяем если пользователь выбрал всё нет то выводим else
            if big:
                pasw.append(s.ascii_uppercase)
            if lower:
                pasw.append(s.ascii_lowercase)
            if digit:
                pasw.append(s.digits)
            if simv:
                pasw.append(s.punctuation)
            if length.isdigit():
                length = int(length)
            else:
                length = 10
        else:
            return '\nНичего не выбрал???))) гуд бай)\n'
        parol = ''
        
        while length != 0:
            parol += choice(choice(pasw))
            length -= 1

        return '\n' + parol

    #! Режим 1
    def menu_1():        
        print('\nДля начала узнаем что вы хотите включить в пароль:\n')
        big_a = input('\nВключать большие буквы?(По умолчанию да)\n')[0].lower() in ['н', 'n']
        lower_a = input('\nВключать маленькие буквы?(По умолчанию да)\n')[0].lower() in ['н', 'n']
        digit = input('\nВключать ли цифры?(По умолчанию да)\n')[0].lower() in ['н', 'n']
        simvol = input('\nВключать ли символы?(По умолчанию да)\n')[0].lower() in ['н', 'n']
        len_pasw = input('\nКакую длину строки?(По умолчанию 10)\n')
        print(pasword(not(big_a), not(lower_a), not(digit), not(simvol), len_pasw))

    #! Режим 2
    def menu_2():    
        while True:
            txt = input('\nВведите все символы из которых хотите сделать пароль\n')
            x =  input('\nВведите длину строки:\n(По умолчанию стоит 10)\n') 
            len_txt = int(x) if x.isdigit() else 10
            if len(txt) > len_txt:
                parol = ''
                while len_txt != 0:
                    parol += choice(txt)
                    len_txt -= 1
                print(f'\n\nВаш сгенерированый пароль: {parol}\n\n')
                break
            else:
                print('\nДлина символов должна быть больше либо равна длине пароля!', end='')

    #! Выбор Режима Пароля
    def menu():    
        if input('\nДля начала выберете режим\nРежим 1: Программа спрашивает у вас данные например делать ли большие буквы или нет\nРежим 2: Вы сами пишите текст из которого хотите сделать пароль и пишите длину\n(По умолчанию 1)\n') == '2':
            menu_2()
        else:
            menu_1()
        
    menu()
    
    #! Проверяем хочет ли пользователь продолжить или же нет
    if input('\nХотите продолжить?(По умолчанию нет)\n')[0].lower() in ['д', 'y']: 
        continue
    else:
        break