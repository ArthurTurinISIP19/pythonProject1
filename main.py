import math
"""print('Введите 2х значное число ')
x1 = int(input())
print('Введите число "a"')
a = int(input())
if 99 >= x1 >= 10:
    q = x1 % 10
    w = x1 // 10
    e = q + w
    if e % 3 == 0:
        print(f'сумма цифр числа {x1} кратно 3')
    else:
        print('не кратно 3')
    if e % a == 0:
        print(f'сумма цифр кратна {a}')
    else:
        print(f'сумма цифр не кратна {a}')
else:
    print(f'число {x1} не яв 2х значным')"""

text1 = str("")
while True:
    text = str(input())
    text1 = text1 + " " + text
    if text == "конец":
        break
#print(text1)
text1 = text1.split()
#print(len(text1)            )
for i in range(len(text1)):
    print(text1[i])