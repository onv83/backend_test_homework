"""2.
Напишите аннотацию для функции series_sum(). Логика работы функции
описана в docstring.
Подсказка
Для описания сложных типов нужен импорт из typing.
Ожидается, что на вход функции придёт список, состоящий только из строк
и чисел — целых или с плавающей точкой."""
from typing import Union, List


def series_sum(incoming: List[Union[str, float]]) -> str:
    """Принимает на вход список, приводит его элементы к строкам
    и конкатенирует их.
    """
    result = ''
    for i in incoming:
        result += str(i)
    return result


# Список
# <имя_переменной>: List[<тип_значения>]
var_list: List[int] = [1, 2, 3, 4, ]
