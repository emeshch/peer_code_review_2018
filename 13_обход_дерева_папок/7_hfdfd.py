## Программа должна обходить всё дерево папок, начинающееся с той папки, где она
## находится, и сообщать следующую информацию (далее - по вариантам): 
## в какой папке лежит больше всего файлов.

import os
import re

def obhod():
    d = {}
    path = '.'
    for root, dirs, files in os.walk(path):
        d[root] = len(files)
    num = max(d.values())
    print('Папка(-и) с наибольшим кол-вом файлов:')
    for root in sorted(d, key = d.get, reverse = True):
        r = re.search('\\\(\w+)$', root)
        if d[root] == num and r:
            string = r.group(1)
            print(string + '(' + str(d[root]) + ')')
        elif root == '.' and d[root] == num:
            print('Начальная папка' + '(' + str(d[root]) + ')')

def main():
    return obhod()

if __name__=='__main__':
    main()
