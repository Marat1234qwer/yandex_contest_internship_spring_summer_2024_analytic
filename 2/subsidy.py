'''
Вводим данные.
Создаем список сколько денег должны отдать и
список сколько денег получают.
Считаем количество субсидий:
если житель должен больше чем он получит,
увеличиваем субсидию на эту сумму.
'''

n = int(input())
lst_debt = []
for i in range(n):
    lst_input = list(map(int, input().split()))
    lst_debt.append(lst_input)

lst_get = [0] * n  # сколько денег получают
for i in range(n):
    get_to = lst_debt[i][0]
    how_mach = lst_debt[i][1]
    lst_get[get_to-1] += how_mach

subsidy = 0
for i in range(n):
    if lst_debt[i][1] > lst_get[i]:
        subsidy += lst_debt[i][1] - lst_get[i]

print(subsidy)
