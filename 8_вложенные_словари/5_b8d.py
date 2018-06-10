# Вам нужно написать программу, которая загадывает слова. Загадав существительное, программа показывает подсказку в виде распространённого словосочетания с этим существительным, в котором существительное заменено многоточием, и ждёт ответа пользователя, после чего сообщает, выиграл он или проиграл. Например, если загадано слово «снег», можно показать подсказку «белый ...». Словосочетание можно подсмотреть в корпусе или довериться интуиции.
# В задании обязательно использовать словарь. Программа должна уметь загадывать как минимум 5 разных слов (с разными подсказками). Кроме того, желательно, чтобы слова и подсказки хранились в отдельном csv-файле, который загружался бы при запуске программы.
# Дополнительные свойства программы по вариантам:
# Вариант (5) Программа показывает число попыток, которое пользователь уже сделал, чтобы угадать слово;

import random

dictionary = {}


def neededword():
    word = random.choice(list(dictionary.keys()))
    return word


def dictionary_maker():
    with open('words1.csv', 'r', encoding='utf-8') as f:
        for line in f:
            sp = line.strip().split(';')
            if len(sp) != 2:
                continue
            if(sp[0] not in dictionary):
                dictionary[sp[0]]=[]
            dictionary[sp[0]].append(sp[1])
    return


def word_guesser(word):
    attempt = 0
    print('Попробуйте отгадать слово!')
    for i in dictionary[word]:
        print('Подсказка:', i )
        guess = input().lower()
        attempt += 1
        if guess == word:
            print('Ура, вы отгадали с ', attempt, ' попытки')
            return
        else:
            print('Увы. Текущее количество попыток:', attempt)
    print('Увы, подсказки кончились. Количество использованных попыток:', attempt)
    return


def main():
    dictionary
    dictionary_maker()
    for i in range(5):
        word = neededword()
        word_guesser(word)


if __name__ == "__main__":
    main()
