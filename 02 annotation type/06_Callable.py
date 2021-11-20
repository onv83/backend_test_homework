""" Если функция передаётся в качестве аргумента в другую функцию или в метод
и там вызывается — такому аргументу присваивается тип Callable."""
from typing import Callable

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
# app(printer, printer)
# ...mypy сообщит об ошибке:
# error: Argument 2 to "app" has incompatible type "Callable[[], None]";
# expected "Callable[[str], str]"
# "Передан вызываемый объект, который ничего не принимает и не возвращает,
# а ожидался объект, который на вход примет строку и вернёт строку.
# Непорядочек."


"""В передаваемой функции можно аннотировать только возвращаемый тип, 
не указывая тип аргументов:
from typing import Callable"""

# Вместо типов аргументов для Callable можно поставить Ellipsis (три точки)
# В случае использования Ellipsis квадратные скобки [] не нужны.
def app1(printed_inside: Callable[[], None],
        returned_inside: Callable[..., str]) -> None:
    printed_inside()
    print(returned_inside('Нет, вызови меня!'))

app1(printer, returner)