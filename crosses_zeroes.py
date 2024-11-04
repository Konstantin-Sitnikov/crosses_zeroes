#Создаем игровое поле
playinig_field = {(0, 0): "-", (0, 1): "-", (0, 2): "-",
                  (1, 0): "-", (1, 1): "-", (1, 2): "-",
                  (2, 0): "-", (2, 1): "-", (2, 2): "-"}


def dislayning_the_playinig_field(a: dict) -> str:

    """Функция отображения текущего состояния игрового поля
        функция формирует и возвращает игровое проле в виде строки
    """

    field = (f"{" " * 15} X\n"             #Подпись оси Х
             f"{" " * 9} 0     1     2\n"    #Значения координат по оси Х
             f"{" " * 7}{"-" * 19}\n")       #Оформление горизонтальной линии
    for i in range(3):
        new_string = f" Y  {i}" if i == 1 else f"    {i}" # Создаем новую строку с подписью значений координат по оси Y
        for j in range(3):
            new_string += f"  |  {playinig_field[(i, j)]  }"        #Добавляем в новую строку значения столбцов
        new_string += (f"  |\n"
                       f"{" " * 7}{"-" * 19}\n")        #Делаем переход на новую строку с оформлением горизонтальной линии
        field += new_string         #Добавляем новую строку к игровому полю
    return field        #Возвращаем значение текущего игрового поля

print(dislayning_the_playinig_field(playinig_field))

def check_win(a: dict, symbol) -> bool:

    """Функция проверки выигрышных комбинаций

    в функции создается контрольный список "control_list" с проверяемыми символами
    и 4 списка:
     - "diagonal_1", "diagonal_2" - списки, для проверки выигрышных комбинаций по диагонали
     - line - список, для проверки выигрышных комбинаций по строке
     - column - список, для проверки выигрышных комбинаций по столбцу

    если хотябы один из 4-х списков совпадет с контрольным, фунция вернет: "True",
    иначе:  False"""


    control_list = [symbol] * 3 #создаем тестовый список из необходимых символов
    diagonal_1 = []         #списки для проверки комбинации по диагонали
    diagonal_2 = []
    for i in range(3):
        line = []           #список для проверки комбинации по строке
        column = []         #список для проверки комбинации по столбцу
        for j in range(3):
            line.append(playinig_field[(i, j)])             #заполняем список строк
            column.append(playinig_field[(j, i)])           #заполняем список столбцов
            if i == j:
                diagonal_1.append(playinig_field[(j, i)])   #заполняем списки диагоналей
            if i + j == 2:
                diagonal_2.append(playinig_field[(j, i)])

        if (line == control_list or column == control_list or
                diagonal_1 == control_list or diagonal_2 == control_list):      #сравниваем списоки с тестовым
            return True
    return False



def coordinate_check(x:str, y:str) -> bool:

    """ Функция проверки введенных кординат

    Функция принимает на вход значения координат и проверяет:
    - количество введенных символов;
    - что введены именно числа,
    - введеные числа лежат в нужном диапазоне

    Функция возвращает "True" если пользовать верно ввел координаты

    """

    if len(x) == 1 and len(y) == 1:                     #Проверяем длинну введенных чисел
        if x.isdigit() and y.isdigit():                 #Проверяем что введены числа
            if 0 <= int(x) <= 2 and 0 <= int(y) <= 2:   #Проверяем что числа лежат в нужном диапазоне
                return True
    return False


def check_add_symbol(symbol:str) -> any:
    while True:
        print(f"Ход '{symbol}'")
        x = input("Введите x (от 0 до 2): ")
        y = input("Введите y (от 0 до 2): ")
        if coordinate_check(x, y):
            if playinig_field[(int(y), int(x))] == "-":
                playinig_field[(int(y), int(x))] = symbol
                break
            else:
                print("Позиция занята, попробуйте снова")
                continue
        else:
            print("Вы ввели не верные координаты, попробуйте снова")
            continue



def draw_tect(a: dict) -> bool:
    x = True
    for value in a.values():
        if value == "-":
            x = False
    return x



def game(n:int) -> any:
    while True:
        print(dislayning_the_playinig_field(playinig_field))

        if n % 2 != 0:
            symbol = "X"
            check_add_symbol(symbol)
            n = 2
            if check_win(playinig_field, symbol):
                print("-" * 21)
                print(dislayning_the_playinig_field(playinig_field))
                print("-" * 21)
                print("X победил")
                break
            if not(check_win(playinig_field, symbol)) and draw_tect(playinig_field):
                print("Ничья")
                break


        else:
            symbol = "O"
            check_add_symbol(symbol)
            check_win(playinig_field, symbol)
            n = 1
            if check_win(playinig_field, symbol):
                print("-" * 21)
                print(dislayning_the_playinig_field(playinig_field))
                print("-" * 21)
                print("O победил")
                break
            if not (check_win(playinig_field, symbol)) and draw_tect(playinig_field):
                print("Ничья")
                break










# while True:
#     print("-" * 21)
#     print("   Добро подаловать  \n"
#           "       в игру \n"
#           "  'Крестики-Нолики'")
#     print("-" * 21)
#     print("1. Начать новую игру!")
#     print("2. Завершить игру")
#     print("-" * 21)
#     n = 1
#     i = int(input("Выберете действие: "))
#
#     if i == 1:
#         game(n)
#
#     elif i == 2:
#         print("Игра закончена!")
#     elif i == 3:
#         print("Игра закончена!")
#         break