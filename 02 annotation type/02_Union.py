"""Если переменная должна принимать данные нескольких разных типов
— применяют аннотацию Union. Разрешённые типы перечисляют через запятую,
в квадратных скобках:"""
from typing import Union


# Аргумент x может принимать целое число или строку
def hundreds(x: Union[int, str]) -> str:
    return str(x * 100)


hundreds(100)
hundreds('сто')

"""Кстати, аннотация Optional[<тип_данных>] 
эквивалентна Union[<тип_данных>, None]."""