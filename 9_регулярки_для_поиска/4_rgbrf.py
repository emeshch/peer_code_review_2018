##В этом домашнем задании программа должна открывать файл с русским текстом в кодировке UTF-8 и распечатывать из него по одному разу все встретившиеся в нём (в зависимости от варианта): 
##формы глагола «выпить»

import re


def words(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
        text = text.lower()                     # ищет формы, начинающиеся с заглавной буквы
        text = re.sub(r'[^а-я ]', ' ', text)    # знаки препинания не мешаются
        words = text.split()
    return words


def forms():
    print('введите название файла') # название файла, в котором искать теперь может ввести пользователь
    filename = input()
    w = words(filename)
    verb_forms = []
    for word in w:
        r = re.search('вып(и(в(ш(ая|и(й|х|м(и)?)?))?[^а-я]|т(а(я)?|ы(й|х|м(и)?))?)|ь(ю(т)?|(е(шь|м|т(е)?)))(ся)?|ей(те)?(сь)?)', word) # не ищет формы прошедшего времени и падежных форм причастий
        if r:
            verb = r.group()                    # только форма, нет лишней информации
            verb_forms.append(verb)
        r = re.search('выпил[аои]*', word)      #  ищет формы прошедшего времени
        if r:
            verb = r.group()
            verb_forms.append(verb)
        r = re.search('выпивш[а-р,т-я]{2,3}', word)  # ищет формы действительных причастий
        if r:
            verb = r.group()
            verb_forms.append(verb)
        r = re.search('выпит[а-ы,э-я]{0,3}', word)  # ищет формы страдательных причастий
        if r:
            verb = r.group()
            verb_forms.append(verb)

    print(set(verb_forms))                      # нет повторений


def main():
    forms()


if __name__ == '__main__':
    main()
