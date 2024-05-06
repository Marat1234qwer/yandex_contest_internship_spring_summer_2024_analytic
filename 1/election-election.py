"""
Считываем данные. Находим индекс города с наибольшим количеством голосов.
Присваиваем голоса Борису, удаляем город из списка.
Голоса за Андрея из оставшихся городов приписываем Андрею.
Пока голоса за Андрея больше чем у Бориса,
повторяем действия.
"""


def read_data():
    with open('input.txt', 'r') as input:
        n = int(input.readline())
        lst_vote = []
        for _ in range(n):
            lst_insert = [int(n) for n in input.readline().split(" ")]
            lst_vote.append(lst_insert)
    return lst_vote


def search_index_bigger_sum(lst):
    best = 0
    best_index = 0
    for i in range(len(lst)):
        summa = sum(lst[i])
        if summa > best:
            best = summa
            best_index = i
    return best_index


def couting_a_vote(lst):
    a_vote = 0
    for i in range(len(lst)):
        a_vote += lst[i][0]
    return a_vote


def main():
    lst_vote = read_data()
    
    b_vote = 0
    a_vote = couting_a_vote(lst_vote)
    count = 0
    if a_vote > b_vote:
        while a_vote >= b_vote:
            b_vote += sum(lst_vote[search_index_bigger_sum(lst_vote)])
            lst_vote.pop(search_index_bigger_sum(lst_vote))
            a_vote = couting_a_vote(lst_vote)
            count += 1

    print(count)


if __name__ == '__main__':
    main()
