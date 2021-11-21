"""Аннотации коллекций
Для типизации коллекций (множеств, словарей, списков и кортежей) есть
специальный синтаксис.
Инструменты для типизации коллекций импортируются из того же модуля typing."""
from typing import Sequence, Dict, List, Tuple, Set, Union


# Это множество может принять только целые числа
var_set: Set[int] = {1, 2, 3, 4, 5, 6, }

# Словарь
# <имя_переменной>: Dict[<тип_ключа>, <тип_значения>]
# Ключ аннотирован как строка, а значение - как целое число
var_dict: Dict[str, int] = {'forty_two': 42, 'hundred': 100, }

# Список
# <имя_переменной>: List[<тип_значения>]
var_list: List[int] = [1, 2, 3, 4, ]

# Кортеж с определённой длиной (перечисляются типы всех элементов)
# <имя_переменной>: Tuple[<тип_элемента_1>, <тип_элемента_2>,
# <тип_последнего элемента>]
var_tuple: Tuple[int, int, str, float] = (1, 2, 'привет', 1.618,)

# Кортеж с переменной длиной
# <имя_переменной>: Tuple[<тип_всех_элементов>, ...]
# Многоточие (Ellipsis) - это указание для Python, что длина
# кортежа не определена
var_tuple1: Tuple[float, ...] = (1, 2, 3.4,)

# Универсальный тип Sequence (Последовательность),
# подойдёт для аннотирования списка или множества

# <имя_переменной>: Sequence[<тип_всех_элементов>]
# принимает список
var_sequence: Sequence[float] = [1.2, 2, 3, ]
# и принимает множество
var_sequence1: Sequence[float] = {1.2, 2, 3, }
var_sequence2: Set[Union[float, int]] = {1.2, 2, 3, }

"""Синтаксис коллекций предполагает, что коллекция содержит 
однотипные элементы.
Однако типом значений коллекции могут быть Any, Union или Optional, 
и тогда можно аннотировать типы как угодно гибко:
from typing import Tuple, Union"""

var_tuple2: Tuple[Union[str, int, bool], ...] = (True, 13, 'наш кортеж',)
print(var_tuple2)