"""
Считываем данные.
Пишем функцию проверки есть ли в списке простое число.
Создаем список в который будем вносить True - если список содержит
простое число и False если нет.
lst_move - список какое число можно дописать за ход.
Делаем проверку: если длинна списка lst_t_f - не четное число,
значит выиграла Алиса. Выводим на печать 'YES'.
"""


def is_prime(lst):
    flag = False
    for i in range(len(lst)):
        # lst[i] = lst[i]
        d = 2
        if lst[i] > 1:
            while lst[i] % d != 0:
                d += 1
        if d == lst[i] or lst[i] == 1:
            flag = True
            break
    return flag


n, k = map(int, input().split())

lst_t_f = []
while True not in lst_t_f:
    lst_move = [0] * k
    for i in range(k):
        lst_move[i] = n+i+1
    lst_t_f.append(is_prime(lst_move))
    n += 1

if len(lst_t_f) % 2 == 1:
    print('YES')
else:
    print('NO')
