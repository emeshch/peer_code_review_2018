#Она должна открывать заранее сохранённый html-файл со статьёй из русской википедии
#на определённую тему с определённой карточкой (в зависимости от варианта) и доставать оттуда кое-какую информацию
#(тоже в зависимости от варианта).
#Извлеченную информацию она должна записать в текстовый файл.
#4. статьи об учёных (напр., Эйнштейн, Альберт) — научная сфера;

import re


def f():
    print('Введите полное имя файла')
    filename = input()
    with open(filename, 'r', encoding='utf-8') as a:
        b = a.read()
    return b


def finder(b):
    found = re.findall('Научная\sсфера</th><td>\n<p><span.*title="([А-Яа-я\s]*)', b)
    with open("answer.txt", "w", encoding="utf-8") as f:
        f.write(str(found))


def main():
    b = f()
    finder(b)


if __name__ == "__main__":
    main()
