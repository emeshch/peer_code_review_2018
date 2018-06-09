# В этом домашнем задании программа должна открывать файл с русским текстом в кодировке UTF-8 и распечатывать из него по одному разу все встретившиеся в нём (в зависимости от варианта): 
# Вариант (5) формы глагола «съесть»

import re

d = ''
with open('Text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        d = d + ' ' + line.replace('\n', ' ')

#d = set(open('Text.txt', 'r', encoding='utf-8'))

result1 = re.findall(r'съе+\w+', d)
result2 = re.findall(r'Съе+\w+', d)
result3 = re.findall(r'несъе+\w+', d)
result4 = re.findall(r'Несъе+\w+', d)
print("СЛОВА, НАЧИНАЮЩИЕСЯ СО СТРОЧНОЙ БУКВЫ:")
print()
for word in result1:
    if word[:4] == 'съез' or word[:4] != 'съеб' or word[:4] != 'съеж' or word[:4] != 'съех': # на случай, если в тексте будут матерные слова
        print(word)
print()
print("СЛОВА, НАЧИНАЮЩИЕСЯ С ЗАГЛАВНОЙ БУКВЫ:")
print()
for word in result2:
    if word[:4] != 'Съез' or word[:4] != 'Съеб' or word[:4] != 'Съеж' or word[:4] != 'Съех': # на случай, если в тексте будут матерные слова
        print(word)
        if word == word:
            del(word)
print()
print("СЛОВА С ПРИСТАВКОЙ, НАЧИНАЮЩИЕСЯ СО СТРОЧНОЙ БУКВЫ:")
print()
for word in result3:
    if word[:4] != 'несъез' or word[:4] != 'несъеб' or word[:4] != 'несъеж' or word[:4] != 'несъех': # на случай, если в тексте будут матерные слова
        if word[0] != word[1]:
            print(word)
print()
print("СЛОВА С ПРИСТАВКОЙ, НАЧИНАЮЩИЕСЯ С ЗАГЛАВНОЙ БУКВЫ:")
print()
for word in result4:
    if word[:4] != 'Несъез' or word[:4] != 'Несъеб' or word[:4] != 'Несъеж' or word[:4] != 'Несъех': # на случай, если в тексте будут матерные слова
        print(word)
