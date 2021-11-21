"""3.
Напишите аннотацию для всех функций. Логика работы функции add() описана
в docstring.
Подсказка
Числа могут быть как целыми, так и с плавающей точкой.
Тип float принимает и те, и другие."""
from typing import Callable


def add(number: float, callback: Callable[[float], float]) -> float:
    """Производит арифметические действия с числами.
    Принимает число и функцию, выполняющую арифметическое действие.
    """
    return callback(number)


def adder20(number: float) -> float:
    """Добавляет к аргументу 20."""
    return number + 20


def multiplier2(number: float) -> float:
    """Умножает аргумент на 2."""
    return number * 2
