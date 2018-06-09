# Программа с помощью отдельной функции принимает от пользователя название файла с английским текстом, читает этот файл и сообщает:
# Вариант (5) Сколько в тексте прилагательных с суффиксом -ous, и какая средняя длина такого прилагательного.

def main():
    ''' '''
    wordlist = []
    length = []
    name = input("Введите имя файла (с расширением): ")
    amount = 0
    dlina = 0
    try:
        with open(name, encoding='utf-8') as f:
            text = f.read()
            text = text.replace('-', '')
            text = text.replace(',', '').replace('.', '')
            words = text.split()
            for word in words:
                if word[-3:] == "ous":
                    amount += 1
                    wordlist.append(word)
                    length.append(len(word))
            print("Общее количество слов: ", amount)
            print("Средняя частота: ", round(float(sum(length) / amount)))
    except FileNotFoundError as err_msg:
        print("Файла {} не существует.".format(name))
        print(err_msg)

if __name__ == '__main__':
    main()
