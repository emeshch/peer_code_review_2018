# Вам нужно написать программу, порождающую случайные грамматически правильные, но бессмысленные тексты.  

# Вместо тысячи объяснений прикладываем два образца программ: poem_generator.py порождает стихотворение на русском языке, написанное трехстопным анапестом, sentence_generator.py порождает текст на английском языке. Посмотрев программы, вы поймёте, как такая программа должна быть устроена и какие в ней должны быть функции.  Функции, естественно, не обязательно делать ровно такими же, как в этой программе (и даже желательно сделать их как-нибудь по-своему), но каждая ваша функция должна делать какую-то одну определённую операцию — таким образом, функций у вас в программе должно быть не одна и не две. 

# Для работы вам понадобится функция выбора случайного элемента из массива. Чтобы её использовать, в самом начале программы нужно написать

# Вариант (5) Текст должен быть не короче, чем 5 предложений на русском языке. Предложения должны быть сложносочинёнными и сложноподчинёнными. 


# Инструкция для программы:
# Создайте свои файлы с названиями, которые указаны в этой программе. Затем запишите туда требуемые слова. Только тогда программа будет рабоатть правильно.

import random

pnouns = []
padverbs = []
pnouns2 = []
pokts = []
pnouns3 = []
pnouns4 = []
pverbs1 = []
pverbs2 = []

nouns = []
adverbs = []
nouns2 = []
adjectives = []
soiuzes = []
nouns3 = []
verbs = []
obsts = []
verbs2 = []

# Тип сложного предложения

def Type():
    types = ['СПП', 'ССП']
    if random.choice(types) == 'СПП':
        print()
        print("СЛОЖНОПОДЧИНЁННОЕ ПРЕДЛОЖЕНИЕ")
        print()
        Vid = Pnoun1() + Padv() + Pverb1() + \
              Pnoun2() + ',' + Pokt() + Pnoun3() + Pverb2() + Pnoun4()
    else:
        print()
        print("СЛОЖНОСОЧИНЁННОЕ ПРЕДЛОЖЕНИЕ")
        print()
        Vid = noun() + adverb() + verb1() + adjective() + noun2() + \
              soiuz() + noun3() + verb2() + obst()
    return Vid

# Сложноподчинённое предложение

def Pnoun1():
    with open ("Words1.txt", "r", encoding = "utf-8-sig") as f1:
        for word in f1.read().split("\n"):
            pnouns.append(word)
    return random.choice(pnouns)
 
def Padv():
    with open ("Words2.txt", "r", encoding = "utf-8-sig") as f2:
        for word2 in f2.read().split("\n"):
            padverbs.append(word2)
    return random.choice(padverbs)

def Pnoun2():
    with open ("Words3.txt", "r", encoding = "utf-8-sig") as f3:
        for word3 in f3.read().split("\n"):
            pnouns2.append(word3)
    return random.choice(pnouns2)
 
def Pokt():
    with open ("Words4.txt", "r", encoding = "utf-8-sig") as f4:
        for word4 in f4.read().split("\n"):
            pokts.append(word4)
    return random.choice(pokts)

def Pnoun3():
    with open ("Words5.txt", "r", encoding = "utf-8-sig") as f5:
        for word5 in f5.read().split("\n"):
            pnouns3.append(word5)
    return random.choice(pnouns3)

def Pnoun4():
    with open ("Words6.txt", "r", encoding = "utf-8-sig") as f6:
        for word6 in f6.read().split("\n"):
            pnouns4.append(word6)
    return random.choice(pnouns4)

def Pverb1():
    with open ("Words7.txt", "r", encoding = "utf-8-sig") as f7:
        for word7 in f7.read().split("\n"):
            pverbs1.append(word7)
    return random.choice(pverbs1)

def Pverb2():
    with open ("Words8.txt", "r", encoding = "utf-8-sig") as f8:
        for word8 in f8.read().split("\n"):
            pverbs2.append(word8)
    return random.choice(pverbs2)

# Сложносочинённое предложение

def noun():
    with open ("nouns.txt", "r", encoding = "utf-8-sig") as f1:
        for word in f1.read().split("\n"):
            nouns.append(word)
    return random.choice(nouns)
 
def adverb():
    with open ("adverbs.txt", "r", encoding = "utf-8-sig") as f2:
        for word2 in f2.read().split("\n"):
            adverbs.append(word2)
    return random.choice(adverbs)

def noun2():
    with open ("nouns2.txt", "r", encoding = "utf-8-sig") as f3:
        for word3 in f3.read().split("\n"):
            nouns2.append(word3)
    return random.choice(nouns2)
 
def adjective():
    with open ("adjectives.txt", "r", encoding = "utf-8-sig") as f4:
        for word4 in f4.read().split("\n"):
            adjectives.append(word4)
    return random.choice(adjectives)
 
def soiuz():
    with open ("soiuzes.txt", "r", encoding = "utf-8-sig") as f5:
        for word5 in f5.read().split("\n"):
            soiuzes.append(word5)
    return random.choice(soiuzes)

def noun3():
    with open ("nouns3.txt", "r", encoding = "utf-8-sig") as f6:
        for word6 in f6.read().split("\n"):
            nouns3.append(word6)
    return random.choice(nouns3)

def verb1():
    with open ("verbs.txt", "r", encoding = "utf-8-sig") as f7:
        for word7 in f7.read().split("\n"):
            verbs.append(word7)
    return random.choice(verbs)

def obst():
    with open ("obsts.txt", "r", encoding = "utf-8-sig") as f8:
        for word8 in f8.read().split("\n"):
            obsts.append(word8)
    return random.choice(obsts)
 
def verb2():
    with open ("verbs2.txt", "r", encoding = "utf-8-sig") as f9:
        for word9 in f9.read().split("\n"):
            verbs2.append(word9)
    return random.choice(verbs2)

def main():
    amount = ['5', '6', '7', '8', '9', '10']
    if random.choice(amount) == '5':
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
    elif random.choice(amount) == '6':
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
    elif random.choice(amount) == '7':
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
    elif random.choice(amount) == '8':
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
    elif random.choice(amount) == '9':
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
    else:
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())

if __name__ == '__main__':
    main()

