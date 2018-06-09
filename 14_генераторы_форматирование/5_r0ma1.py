# Взять какой-нибудь файл с достаточно большим текстом, прочитать его, поделить на предложения (просто по знакам конца предложения), удалить знаки препинания. Затем в зависимости от варианта сделать следующее (обязательно использовать list comprehensions и formatting): 
# Вариант (5) Преобразовать предложения так, чтобы каждая буква в каждом слове повторялась столько раз, сколько она встречается в этом слове (например, "Мама вымыла раму" превращается в "Маамаа выымыыла раму"). 

from collections import Counter
import string

def main():
    ''' '''
    file = ''.join(open('file.txt', 'r', encoding='utf-8-sig')).rstrip(
        string.punctuation)
    wordes = file.lower().split()
    words = [word.lower() for word in wordes]
    out_sentence = ""
    for word in words:
        for letter in word:
            for _ in range(word.count(letter)):
                out_sentence += letter
        out_sentence += " "
    print(out_sentence)

if __name__ == '__main__':
    main()
