# Вам надо написать на питоне программу, которая спрашивала бы у пользователя три числа (a, b и c), а дальше, в зависимости от номера Вашего варианта, сообщала бы пользователю, обладают или не обладают введённые числа некоторыми свойствами. Вот общий список свойств:
# 1) a и b в сумме дают c
# 2) a умножить на b равно c
# 3) a даёт остаток c при делении на b
# 4) c является решением линейного уравнения ax + b = 0
# 5) a разделить на b равно c
# 6) a в степени b равно c.
# Если у Вас 1-й вариант, программа должна проверять свойства (1) и (4), 2-й -- (2) и (4), 3-й -- (3) и (4), 4-й -- (1) и (5), 5-й -- (2) и (5), 6-й -- (3) и (5), 7-й -- (5) и (6). То есть если у Вас, например, 4-й вариант, то Ваша программа должна проверять, дают ли a и b в сумме число c и получится ли c, если a разделить на b, и сообщать об этом.

# Вариант №5

print ("Введите число А")
a = int(input())
print ("Введите число B")
b = int(input())
print ("Введите число C")
c = int(input())
if a * b == c:
        print("Умножение чисел A и B имеет смысл")
else:
        print("Умножение A и B не имеет смысла")
print()
if a / b == c:
        print("Деление A на B имеет смысл")
else:
        print("Деление A на B не имеет смысла")

