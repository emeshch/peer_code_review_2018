##файлы с каким расширением чаще всего встречаются в этих папках
##(если таких много, можно печатать только одно)


import os
import collections

#Получаем список расширений всех файлов

def ext():
    types = []
    for root, dirs, files in os.walk('.'):
        for fl in files:
            filename, file_extension = os.path.splitext(fl)
            types.append(file_extension)
    return types

#Делаем из них частотный словарь

def freq(d):
    counter = collections.Counter(d)
    counter = collections.Counter(counter).most_common(1)[0][0]
    return counter


def main():
    print('Самое частое разрешение: ', freq(ext()))

    
if __name__ == "__main__":
    main()
