per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму для вклада'))
print(per_cent.items())
print(per_cent.keys())
a = money/100*per_cent.get('ТКБ')
b = money/100*per_cent.get('СКБ')
c = money/100*per_cent.get('ВТБ')
d = money/100*per_cent.get('СБЕР')
deposit = []
deposit.extend([a, b, c, d])
print('накопленные средства за год вклада в каждом из банков', deposit)
deposit.sort()
print('максимальная сумма, которую вы можете заработать:', deposit[-1])
