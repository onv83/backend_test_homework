"""Псевдонимы типов
Псевдоним типа — это имя, которое можно присвоить типу данных, чтобы
упростить чтение кода:"""
from typing import Dict, List, Union

# Создан псевдоним для сложного типа данных:
CustomDict = Dict[str, List[Union[int, str]]]


# Указание этого типа для переменной (через псевдоним)
def just_return_it(incoming: CustomDict) -> CustomDict:
    return incoming


just_return_it({'forty_two': [1, '2'], 'hundred': [1, 2]})

# var_list: List[int] = [1, 2, 3, 4, ]


# Указание того же типа для переменной (без псевдонима)
def just_return_i(incoming: Dict[str, int]) \
        -> Dict[str, int]:
    return incoming


def print_func(func):
    print(func)


# Словарь
# <имя_переменной>: Dict[<тип_ключа>, <тип_значения>]
# Ключ аннотирован как строка, а значение - как целое число
# var_dict: Dict[str, int] = {'forty_two': 42, 'hundred': 100, }

# Выгода налицо: псевдоним сбережёт время и нервы.

printing_func = just_return_i({'forty_two': 42, 'hundred': 100, })

print_func(printing_func)
