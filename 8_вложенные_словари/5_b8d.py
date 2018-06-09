# Вам нужно написать программу, которая загадывает слова. Загадав существительное, программа показывает подсказку в виде распространённого словосочетания с этим существительным, в котором существительное заменено многоточием, и ждёт ответа пользователя, после чего сообщает, выиграл он или проиграл. Например, если загадано слово «снег», можно показать подсказку «белый ...». Словосочетание можно подсмотреть в корпусе или довериться интуиции.
# В задании обязательно использовать словарь. Программа должна уметь загадывать как минимум 5 разных слов (с разными подсказками). Кроме того, желательно, чтобы слова и подсказки хранились в отдельном csv-файле, который загружался бы при запуске программы.
# Дополнительные свойства программы по вариантам: 
# Вариант (5) Программа показывает число попыток, которое пользователь уже сделал, чтобы угадать слово;

import random

def neededword():
    return random.choice(spisok)

spisok = ['Снег', 'Автомобиль', 'Дом', 'Солнце', 'Гриб', 'Город', 'Ёлка', 'Программа',
          'Игра', 'Медаль', 'Школа', 'Море', 'Рыба']
attempt = 0

print()
print('Попробуйте отгадать слово!')
print('Подсказка:')
if neededword() == 'Снег':
    print('Белый...')
    answer = input()
    while answer != 'Снег':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)


elif neededword() == 'Автомобиль':
    print('Cпортивный...')
    answer = input()
    while answer != 'Автомобиль':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)


elif neededword() == 'Дом':
    print('Многоэтажный...')
    answer = input()
    while answer != 'Дом':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)
    
elif neededword() == 'Солнце':
    print('Весеннее..')
    answer = input()
    while answer != 'Солнце':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Гриб':
    print('Съедобный...')
    answer = input()
    while answer != 'Гриб':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Город':
    print('Многонаселённый...')
    answer = input()
    while answer != 'Город':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Ёлка':
    print('Новогодняя...')
    answer = input()
    while answer != 'Ёлка':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Программа':
    print('Образовательная...')
    answer = input()
    while answer != 'Программа':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Игра':
    print('Познавательная...')
    answer = input()
    while answer != 'Игра':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Медаль':
    print('Золотая...')
    answer = input()
    while answer != 'Медаль':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Рыба':
    print('Речная...')
    answer = input()
    while answer != 'Рыба':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Школа':
    print('Старшая...')
    answer = input()
    while answer != 'Школа':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

else:
    print('Лазурное...')
    answer = input()
    while answer != 'Море':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

attempt = 0
print()
print('Попробуйте отгадать слово!')
print('Подсказка:')
if neededword() == 'Снег':
    print('Зимний...')
    answer = input()
    while answer != 'Снег':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)


elif neededword() == 'Автомобиль':
    print('Гоночный...')
    answer = input()
    while answer != 'Автомобиль':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)


elif neededword() == 'Дом':
    print('Жилой...')
    answer = input()
    while answer != 'Дом':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)
    
elif neededword() == 'Солнце':
    print('Яркое..')
    answer = input()
    while answer != 'Солнце':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Гриб':
    print('Лесной...')
    answer = input()
    while answer != 'Гриб':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Город':
    print('Опустевший...')
    answer = input()
    while answer != 'Город':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Ёлка':
    print('Зелёная...')
    answer = input()
    while answer != 'Ёлка':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Программа':
    print('Вирусная..')
    answer = input()
    while answer != 'Программа':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Игра':
    print('Настольная...')
    answer = input()
    while answer != 'Игра':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Медаль':
    print('Почётная...')
    answer = input()
    while answer != 'Медаль':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Рыба':
    print('Хищная..')
    answer = input()
    while answer != 'Рыба':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Школа':
    print('Начальная...')
    answer = input()
    while answer != 'Школа':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

else:
    print('Мёртвое...')
    answer = input()
    while answer != 'Море':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

attempt = 0
print()
print('Попробуйте отгадать слово!')
print('Подсказка:')
if neededword() == 'Снег':
    print('Пушистый...')
    answer = input()
    while answer != 'Снег':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)


elif neededword() == 'Автомобиль':
    print('Скоростной...')
    answer = input()
    while answer != 'Автомобиль':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)


elif neededword() == 'Дом':
    print('Деревенский...')
    answer = input()
    while answer != 'Дом':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)
    
elif neededword() == 'Солнце':
    print('Жёлтое...')
    answer = input()
    while answer != 'Солнце':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Гриб':
    print('Ядовитый...')
    answer = input()
    while answer != 'Гриб':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Город':
    print('Родной...')
    answer = input()
    while answer != 'Город':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Ёлка':
    print('Украшенная...')
    answer = input()
    while answer != 'Ёлка':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Программа':
    print('Компьютерная...')
    answer = input()
    while answer != 'Программа':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Игра':
    print('Интересная...')
    answer = input()
    while answer != 'Игра':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Медаль':
    print('Олимпийская...')
    answer = input()
    while answer != 'Медаль':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Рыба':
    print('Морская...')
    answer = input()
    while answer != 'Рыба':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Школа':
    print('Специальная...')
    answer = input()
    while answer != 'Школа':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

else:
    print('Глубокое...')
    answer = input()
    while answer != 'Море':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

attempt = 0
print()
print('Попробуйте отгадать слово!')
print('Подсказка:')
if neededword() == 'Снег':
    print('Холодный...')
    answer = input()
    while answer != 'Снег':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)


elif neededword() == 'Автомобиль':
    print('Тюнингованный...')
    answer = input()
    while answer != 'Автомобиль':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)


elif neededword() == 'Дом':
    print('Строящийся...')
    answer = input()
    while answer != 'Дом':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)
    
elif neededword() == 'Солнце':
    print('Ослепительное...')
    answer = input()
    while answer != 'Солнце':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Гриб':
    print('Вкусный...')
    answer = input()
    while answer != 'Гриб':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Город':
    print('Столичный...')
    answer = input()
    while answer != 'Город':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Ёлка':
    print('Праздничная...')
    answer = input()
    while answer != 'Ёлка':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Программа':
    print('Продвинутая...')
    answer = input()
    while answer != 'Программа':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Игра':
    print('Виртуальная...')
    answer = input()
    while answer != 'Игра':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Медаль':
    print('Бронзовая...')
    answer = input()
    while answer != 'Медаль':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Рыба':
    print('Океаническая...')
    answer = input()
    while answer != 'Рыба':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Школа':
    print('Деревенская...')
    answer = input()
    while answer != 'Школа':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

else:
    print('Загрязнённое...')
    answer = input()
    while answer != 'Море':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

attempt = 0
print()
print('Попробуйте отгадать слово!')
print('Подсказка:')
if neededword() == 'Снег':
    print('Тающий...')
    answer = input()
    while answer != 'Снег':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)


elif neededword() == 'Автомобиль':
    print('Полицейский...')
    answer = input()
    while answer != 'Автомобиль':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)


elif neededword() == 'Дом':
    print('Одноэтажный...')
    answer = input()
    while answer != 'Дом':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)
    
elif neededword() == 'Солнце':
    print('Осеннее...')
    answer = input()
    while answer != 'Солнце':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Гриб':
    print('Маленький...')
    answer = input()
    while answer != 'Гриб':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Город':
    print('Российский...')
    answer = input()
    while answer != 'Город':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Ёлка':
    print('Растущая...')
    answer = input()
    while answer != 'Ёлка':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Программа':
    print('Школьная...')
    answer = input()
    while answer != 'Программа':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Игра':
    print('Весёлая...')
    answer = input()
    while answer != 'Игра':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Медаль':
    print('Серебряная...')
    answer = input()
    while answer != 'Медаль':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Рыба':
    print('Озёрная...')
    answer = input()
    while answer != 'Рыба':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

elif neededword() == 'Школа':
    print('Младшая...')
    answer = input()
    while answer != 'Школа':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)

else:
    print('Лазурное...')
    answer = input()
    while answer != 'Море':
        print('Неправильный ответ')
        attempt +=1
        print('Текущее количество попыток: ', attempt)
        answer = input()

    attempt +=1
    print('Правильно!')
    print('Количество затраченных попыток: ', attempt)
