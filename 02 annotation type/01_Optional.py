"""Компоновщик Optional аннотирует типы данных для переменных, которые могут
принять два типа данных: данные определённого типа и тип None;
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
