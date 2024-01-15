# Использованы следующие парадигмы:
# 1. Структурная (императивная), т.к. нет необходимости использовать GO TO, порядок действие четко определен.
# 2. Декларативная - для создания списка произведений используется list comprehantion.
# 3. Процедурная - для вывода таблицы умножения создана функция multiplicate_table_print
# в целях разгрузки основного кода и возможности использования функции для вывода списков произведений,
# созданных другими методами и с использованием других парадигм.


COUNT_COLUMN = 5

def multiplicate_table_print(table: list[list]):
    start = 0
    end = COUNT_COLUMN
    max_len = len(table[len(table)-1][len(table)-1])
    while end <= len(table):
        for i in range(len(table)):
            for j in range(start, end):
                print(table[i][j] + ' ' * (max_len - len(table[i][j])), end = "  ")
            print("")
        start = end
        end += COUNT_COLUMN
        print("")
            

if __name__ == '__main__':
    num = int(input('Введите число: '))
    mult_list =[[f'{i} * {j} = {i * j}' for i in range(1, num+1)] for j in range(1, num+1)]
    multiplicate_table_print(mult_list)
