import string as s 

print('\nДобро пожаломать в Шифровку слова!\n')

# TODO Шифр Цезаря
def code_cause(txt): 
    alaphent = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    for i in txt:
        if i.lower() in alaphent:
            sum_a = alaphent.index(i.lower()) + 3
            if sum_a >= 26:
                y = sum_a - 26
                if i.islower():
                    s += chr(97 + y )
                else:
                    s += chr(65 + y )
            else:
                if i.islower():
                    s += alaphent[sum_a]
                else:
                    s += alaphent[sum_a].upper()
        else:
            s += i
    return s

# TODO Шифр Бинарным
def code_bine(txt): 
    s = []
    for i in txt:
        s.append(format(ord(i), 'b'))
    return ' '.join(s)

# TODO Шифр Наоборот
def code_couple(txt): 
    return txt[::-1]

#Todo Шифр Морзе
def code_morse(txt):    
    morse_alphabet = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    ' ': '  ',
    '1': '.-',
    '2': '-...',
    '3': '-.-.',
    '4': '-..',
    '5': '.',
    '6': '..-',
    '7': '--.',
    '8': '....',
    '9': '.-.',
    '0': '.-'}   
    l = []
    for i in txt:
        if i.lower() in morse_alphabet:
            l.append(morse_alphabet[i.lower()])
        else:
            l.append(i)
    return ''.join(l)

#! Узнаём у пользователя что он хочет и выбираем какой шифр и выводим его 
def menu(): 
    code = input('\nДавай выберем шифровку текста\nУ нас есть вот такие типы шифровки\n\nШифр Цезаря(номер 1)\n\nШифр Бинарный(номер 2)\n\nШирф Наоборот(номер 3)\n\nШифр Морзе(номер 4)\nВыбирете номер(По умолчанию стоит номер 2): ')
    text = input('\nОчень хорошо теперь напиши текст который хотите зашивровать(На английском языке): ')
    func = {'1': code_cause, '2': code_bine, '3': code_couple, '4': code_morse}
    p_func = {'1': 'Шифр Цезаря', '2': 'Бинарный Шифр', '3': 'Шифр Парами', '4': 'Шифр Морзе'}

        
    if len(code) == 1 and code in '1234':
        True
    else:
        code = '2'
    print(f'\nВаш текст:\n{text}\n\n{p_func[code]}:\n{func[code](text)}\n')

    
menu()