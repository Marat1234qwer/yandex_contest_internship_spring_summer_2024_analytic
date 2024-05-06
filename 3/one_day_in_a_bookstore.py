"""
Считываем данные из таблицы в переменную 'data'.
Если разница между покупками покупателя не превышает 30 мин.,
вносим этого покупателя в список.
Считаем сколько каких покупателей в списке.
Записываем в новую таблцу данных покупателей.
"""
import sqlite3


def read_data():
    connection_logs = sqlite3.connect('logs.db')
    cursor_logs = connection_logs.cursor()
    cursor_logs.execute('SELECT * FROM logs')
    data = cursor_logs.fetchall()
    connection_logs.close()
    return data


def write_output_data(lst_u, lst_c):
    connection_output = sqlite3.connect('output.db')
    cursor_output = connection_output.cursor()
    cursor_output.execute('''
    CREATE TABLE IF NOT EXISTS output (
    user_id TEXT,
    cnt INTEGER
    )
    ''')
    for i in range(len(lst_u)):
        cursor_output.execute('INSERT INTO output (user_id, cnt) VALUES (?, ?)', (lst_u[i], lst_c[i]))
    connection_output.commit()
    connection_output.close()


def action(data):
    lst_out = []  # список покупателей активных периодов
    for i in range(len(data)-1):
        dif = data[i+1][1] - data[i][1]
        if data[i][0] == data[i+1][0] and dif < 30:
            lst_out.append(data[i][0])
    lst_out.sort()
    lst_u = []  # список покупателей
    lst_u.append(lst_out[0])
    j = 0
    for i in range(len(lst_out)-1):
        if lst_u[j] != lst_out[i+1]:
            lst_u.append(lst_out[i+1])
            j += 1
    lst_c = []  # сколко раз попал в список lst_u
    for i in range(len(lst_u)):
        lst_c.append(lst_out.count(lst_u[i]))
    return lst_u, lst_c


def main():
    data = read_data()
    lst_u, lst_c = action(data)
    write_output_data(lst_u, lst_c)


if __name__ == '__main__':
    main()
