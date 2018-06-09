# Программа должна обходить всё дерево папок, начинающееся с той папки, где она находится, и сообщать следующую информацию (далее - по вариантам): 
# Вариант (5) Сколько в этих папках встречается разных названий файлов без учёта расширений; 

import os

def stat(prev1,prev2, amount, start_path):
    for root, dirs, files in os.walk(start_path):
        print()
        print('ГДЕ МЫ СЕЙЧАС:', root)
        print()
        print('ФАЙЛЫ:')
        print()
        for dire in dirs:
            print(dire)
            if dire != prev1:
                amount += 1
            prev1 = dire
        for file in files:
            print(file)
            if file != prev2:
                amount += 1
            prev2 = file
    print(amount)
    return amount

def main():
    stat(None, None, 0, '.')

if __name__ == '__main__':
    main()

