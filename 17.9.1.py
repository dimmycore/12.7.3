from random import randint
L = [randint(1, 100) for i in range(20)]
print(L)
S = " ".join(map(str, L))
print(S)
print(type(S))
print(' ')


M = [int(i) for i in S.split()]
try:
    number = int(input("введите целое число от 1 до 100: "))
    if 0 < number < 101 and number % 1 == 0:
        M.append(number)
        M.sort()
        print("список после сортировки: ", M)
    else:
        print("неправильное число")
except ValueError:
    print("ошибка ввода данных")


def binary_search(M, number, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if M[middle] == number:
            return middle
        elif number < M[middle]:
            return binary_search(M, number, left, middle - 1)
        else:
            return binary_search(M, number, middle + 1, right)
    except IndexError:
        return 'число не входит в список'


print('индекс введённого числа в списке: ', binary_search(M, number, 0, 20))

