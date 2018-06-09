# Программа должна открывать файл с русским текстом в utf-8 и сообщать про него следующую информацию (по вариантам):

# Вариант (5) Какой процент слов имеет длину больше 10 символов;

f = open ("Crow.txt", encoding="utf-8")
text = f.read()
f.close()
c1 = 0
c2 = 0
for line in text.split("\n"):
    for word in line.split(" "):
        word.replace(',','')
        n = len(word)
        if n > 10:
            c1+=1
        else:
            c2+=1
        print(len(word))
        print(word)
res = c1/(c1+c2) * 100
print("Процент слов, имеющих длину больше десяти слов, =",end = " ")
print(res)
