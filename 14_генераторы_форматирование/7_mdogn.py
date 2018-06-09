## Взять какой-нибудь файл с достаточно большим текстом, прочитать его, поделить
## на предложения (просто по знакам конца предложения), удалить знаки препинания.
## Затем в зависимости от варианта сделать следующее (обязательно использовать list
## comprehensions и formatting): 
## Для каждого предложения найти слова, которые встретились в предложении больше,
## чем 1 раз, и распечатать табличку с выравниванием по центру, в которой сказано,
## сколько раз они встретились. Например, для предложения
## "А это веселая птица-синица, которая часто ворует пшеницу, которая в темном
## чулане хранится в доме, который построил Джек." распечатать:
##
## которая           2 
##
## в            2



import re

sym = "0123456789.,?!…:;()[]-_|/\"'«»*{}<>@#$%^&№"
pattern = re.compile(r'([А-Я]((т.п.|т.д.|пр.|г.)|[^?!.\(]|\([^\)]*\))*[.?!])')

def sents(filename):
    sents = []
    res = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
        text = text.replace('\n',' ')
        for _,sent in enumerate(pattern.findall(text)):
            sents.append('{}'.format(sent[0]))
        for sent in sents:
            sent_new = re.sub('[0-9]|[\.,\?!…:;—\"\()\/]|( -)','',sent)
            res.append(sent_new)
    return res

def words(res):
    d = {}
    r = {}
    for sent in res:     
        words = sent.lower().split()
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1   
        r = {k:v for k, v in d.items() if v > 1}
        if r:
            print("Предложение: \"" + sent + "\"")
            for key, value in r.items():
                print('{}{:^15}'.format(key,value))
        dict.clear(d)
        dict.clear(r)

def main():
    words(sents('text1.txt'))

if __name__=='__main__':
    main()
        
