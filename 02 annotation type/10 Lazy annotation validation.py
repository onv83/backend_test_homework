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
Ошибка связана с тем, что для переменной position (в начале кода) 
указан тип Position, который объявляется ниже, ближе к концу кода. 
Изменить же порядок кода зачастую бывает невозможно.
Для решения проблемы можно взять тип Position в кавычки: анализатор 
аннотаций всё равно поймёт, что вы имели в виду, а интерпретатор кода 
не споткнётся о незнакомое имя."""


def __init__(self, number: int, position: 'Position') -> None:
    ...


"""Другой вариант решения (начиная с Python 3.7) — воспользоваться 
отложенной обработкой аннотаций (Postponed Evaluation of Annotations, 
представленной в PEP 563) и импортировать annotations из «пакета будущего»:"""


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
Python 3.9 будет работать с отложенной обработкой аннотаций без импорта 
from __future__ import annotations."""