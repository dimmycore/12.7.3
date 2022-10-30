tickets = int(input('Введите количество билетов: '))
a = 0
b = 0
c = 0
i = 0
while i != tickets:
    person = int(input('Введите возраст покупателя: '))
    i += 1
    if person < 18:
        a = a + 0
    elif 18 <= person < 25:
        b = b + 990
    elif person > 25:
        c = c + 1390
count = a + b + c
if tickets > 3:
    print('Cумма к оплате:', int(count * 0.9))
else:
    print('сумма к оплате:', count)
