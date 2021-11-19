"""Optional
Компоновщик Optional аннотирует типы данных для переменных, которые
могут принять два типа данных: данные определённого типа и тип None;
например — str и None, bool и None.
Тип None не указывается в компоновщике Optional в явном виде:"""
from typing import Optional

# Переменная text ожидает данные типа str или None
text: Optional[str]

# Эксперимент: в переменную с типом "строка"...
var: str
# ...передадим None:
var = None
# Анализатор кода сообщит об ошибке:
# Incompatible types in assignment
# (expression has type "None", variable has type "str")

# А переменная text аннотирована через Optional, и если передать в неё None...
text = None
# ...проблем не будет.

"""Union
Если переменная должна принимать данные нескольких разных типов — применяют 
аннотацию Union. Разрешённые типы перечисляют через запятую, в 
квадратных скобках:"""

from typing import Union


# Аргумент x может принимать целое число или строку
def hundreds(x: Union[int, str]) -> str:
    return str(x * 100)


hundreds(100)
hundreds('сто')
"""Кстати, аннотация Optional[<тип_данных>] 
эквивалентна Union[<тип_данных>, None]."""

"""Any
Иногда не нужно ограничивать возможные типы переменной, но по каким-то 
причинам всё равно требуется её типизировать. В этом случае применяют 
аннотацию Any («любой»):"""

from typing import Any

x: Any
x = 12210

x: Any
x = 'Строка'
x = True
x = None

# Можно всё! Переменная x примет любой тип данных.

"""Аннотации коллекций
Для типизации коллекций (множеств, словарей, списков и кортежей) 
есть специальный синтаксис.
Инструменты для типизации коллекций импортируются из того же модуля typing."""
from typing import Sequence, Dict, List, Tuple, Set


# Это множество может принять только целые числа
var_set: Set[int] = {1, 2, 3, 4, 5, 6,}    

# Словарь
# <имя_переменной>: Dict[<тип_ключа>, <тип_значения>]
# Ключ аннотирован как строка, а значение - как целое число
var_dict: Dict[str, int] = {'forty_two': 42, 'hundred': 100,}        
var_dict1 = {'forty_two': 42, 'hundred': 100,}
# Список
# <имя_переменной>: List[<тип_значения>]
var_list: List[int] = [1, 2, 3, 4,]  

# Кортеж с определённой длиной (перечисляются типы всех элементов)
# <имя_переменной>: Tuple[<тип_элемента_1>, <тип_элемента_2>, <тип_последнего элемента>]
var_tuple: Tuple[int, int, str, float] = (1, 2, 'привет', 1.618,) 

# Кортеж с переменной длиной 
# <имя_переменной>: Tuple[<тип_всех_элементов>, ...]
# Многоточие (Ellipsis) - это указание для Python, что длина кортежа не определена
var_tuple1: Tuple[float, ...] = (1, 2, 3.4,)

# Универсальный тип Sequence (Последовательность), 
# подойдёт для аннотирования списка или множества

# <имя_переменной>: Sequence[<тип_всех_элементов>]
# принимает список
var_sequence: Sequence[float] = [1.2, 2, 3,]
# и принимает множество
# var_sequence1: Sequence[float] = {1.2, 2, 3,}
# и принимает множество
var_sequence3: Set[Union[float, int]] = {1.2, 2, 3}
"""Синтаксис коллекций предполагает, что коллекция содержит 
однотипные элементы.
Однако типом значений коллекции могут быть Any, Union или Optional, 
и тогда можно аннотировать типы как угодно гибко:"""

from typing import Tuple, Union

var_tuple2: Tuple[Union[str, int, bool], ...] = (True, 13, 'наш кортеж',)

"""Псевдонимы типов
Псевдоним типа — это имя, которое можно присвоить типу данных, 
чтобы упростить чтение кода:"""

from typing import Dict, List, Union

# Создан псевдоним для сложного типа данных:
CustomDict = Dict[str, List[Union[int, str]]]


# Указание этого типа для переменной (через псевдоним)
def just_return_it(incoming: CustomDict) -> CustomDict:
    return incoming


# Указание того же типа для переменной (без псевдонима)
def just_return_it1(incoming: Dict[str, List[Union[int, str]]])\
        -> Dict[str, List[Union[int, str]]]:
    return incoming

# Выгода налицо: псевдоним сбережёт время и нервы.

"""Callable
Если функция передаётся в качестве аргумента в другую функцию или 
в метод и там вызывается — такому аргументу присваивается тип Callable.
from typing import Callable"""

# Callable[[<тип аргумента 1>, <тип аргумента 2>,...], <возвращаемый тип>]

def printer() -> None:
    print("Вызови меня!")


def returner(word: str) -> str:
    return word


def app(printed_inside: Callable[[], None],
        returned_inside: Callable[[str], str]) -> None:
    printed_inside()
    print(returned_inside('Нет, вызови меня!'))


# При таком вызове всё будет ok:
app(printer, returner)

# А если во второй аргумент передать функцию,
# которая ничего не принимает и не возвращает...
app(printer, printer)
# ...mypy сообщит об ошибке:
# error: Argument 2 to "app" has incompatible type "Callable[[], None]";
# expected "Callable[[str], str]"
# "Передан вызываемый объект, который ничего не принимает и не возвращает,
# а ожидался объект, который на вход примет строку и вернёт
# строку. Непорядочек."

"""В передаваемой функции можно аннотировать только возвращаемый 
тип, не указывая тип аргументов:"""

from typing import Callable

# Вместо типов аргументов для Callable можно поставить Ellipsis (три точки)
# В случае использования Ellipsis квадратные скобки [] не нужны.
def app(printed_inside: Callable[[], None],
        returned_inside: Callable[..., str]) -> None:
    printed_inside()
    print(returned_inside('Нет, вызови меня!'))

"""Классы как типы
Новый класс — это новый тип данных. Если переменная ожидает 
объект какого-то класса, то этот класс и будет типом переменной."""

class WeirdObject:
    def work(self) -> None:
        print("Работает")


# Функция dependency_func() ожидает на вход объект класса WeirdObject:
def dependency_func(obj: WeirdObject) -> None:
    obj.work()

# Создаём объект класса WeirdObject
strange_item: WeirdObject = WeirdObject()

# При таком вызове всё будет ok (в функцию передаётся
# объект класса WeirdObject):
dependency_func(strange_item)
#>>> Работает

# А такая запись будет отмечена линтером как ошибка:
dependency_func(11) 
# error: Argument 1 to "dependency_func" has incompatible type "int";
# expected "WeirdObject"
# "В функцию передано число, а мы-то ожидали объект класса WeirdObject!"

"""Импорт из будущего
В Python 3.9 не понадобится импортировать коллекции из typing: с этими 
типами можно будет работать так же, как вы работаете с типами bool, 
str или int. Начиная с версии Python 3.7 можно заглянуть в будущее — 
специальный импорт даёт возможность уже сейчас применять новый синтаксис: 
названия типов dict, list, tuple и set нужно будет писать с маленькой буквы."""
# Импорт из будущего
from __future__ import annotations  

# И теперь можно работать коллекциями как со встроенными типами
# Список
var_list: list[str] = ['Ура', 'типы', 'можно', 'не импортировать отдельно!', ] 

# Словарь
var_dict: dict[str, float] = {"версия языка": 3.7, }

"""Отложенная проверка аннотаций
До выхода Python 3.7 определение типов в аннотациях происходило во 
время импорта модуля, что приводило к проблеме."""

class CarTracer:
    """Отслеживание автомобиля по номеру."""

    # Тут второй аргумент аннотирован типом Position,
    # но этот тип будет объявлен позже. Возникнет ошибка: "Неизвестное имя!"
    def __init__(self, number: int, position: Position) -> None:
        self.number = number
        self.position = position


# Класс Position объявлен после того, как использован в типизации
class Position:
    """Определяет широту и долготу."""

    def __init__(self, altitude: float, latitude: float) -> None:
        self.altitude = altitude
        self.latitude = latitude


"""При выполнении этого кода возникнет ошибка NameError: 
name 'Position' is not defined.
Ошибка связана с тем, что для переменной position (в начале кода) указан 
тип Position, который объявляется ниже, ближе к концу кода. Изменить 
же порядок кода зачастую бывает невозможно.
Для решения проблемы можно взять тип Position в кавычки: анализатор 
аннотаций всё равно поймёт, что вы имели в виду, а интерпретатор 
кода не споткнётся о незнакомое имя."""


def __init__(self, number: int, position: 'Position') -> None:
    ...


"""Другой вариант решения (начиная с Python 3.7) — воспользоваться 
отложенной обработкой аннотаций (Postponed Evaluation of Annotations, 
представленной в PEP 563) и импортировать annotations из «пакета будущего»:"""

from __future__ import annotations


class CarTracer:
    """Отслеживание автомобиля по номеру."""

    def __init__(self, number: int, position: Position) -> None:
        self.number = number
        self.position = position

    def __str__(self) -> str:
        return (f'Координаты автомобиля номер {self.number},: '
                f'{self.position.altitude}, {self.position.latitude}')


class Position:
    """Определяет широту и долготу."""

    def __init__(self, altitude: float, latitude: float) -> None:
        self.altitude = altitude
        self.latitude = latitude


moscow: Position = Position(55.7522, 37.6156)
car778: CarTracer = CarTracer(778, moscow)

print(car778)

"""Такой код сработает без ошибок.
Python 3.9 будет работать с отложенной обработкой аннотаций без 
импорта from __future__ import annotations."""

from __future__ import annotations.