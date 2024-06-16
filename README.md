Lab-14
Лабораторна робота 14: Логічні операції в Python
#
Мета роботи: Метою даної лабораторної роботи є освоєння основних логічних операцій в мові програмування Python та застосування їх для вирішення різноманітних задач. Очікуваний результат включає розуміння логічних операторів та вміння використовувати їх для побудови логічних умов.

Опис завдання: Необхідно реалізувати кілька функцій, які демонструють застосування логічних операцій у різних контекстах. Завдання включають базові логічні перевірки, умовні оператори, логічні еквівалентності, ексклюзивне "або" (XOR), та інші.
#
Виконання роботи: Кожне завдання реалізовано у вигляді окремої функції, яка приймає вхідні параметри та повертає результат. Усі функції містяться в одному файлі main.py.

Код програми:
#
**Завдання 1**
def check_truth(a, b, c): return (a and b) or c
#
**Завдання 2**
def logical_equivalence(a, b): return a == b
#
**Завдання 3**
def xor(a, b): return (a and not b) or (not a and b)
#
**Завдання 4**
def greet(condition): if condition: return "Hello, World!" else: return "Goodbye, World!"
#
**Завдання 5**
def nested_condition(x, y, z): if x == y == z: return "All same" elif x != y != z != x: return "All different" else: return "Neither"
#
**Завдання 7**
def parity(number): binary_repr = bin(number) count_ones = binary_repr.count('1') return count_ones % 2 == 0
#
**Завдання 8**
def majority_vote(a, b, c): return sum([a, b, c]) > 1
#
**Завдання 9**
def switch(condition): return not condition
#
**Завдання 10**
def ternary_check(condition, if_true, if_false): return if_true if condition else if_false
#
**Завдання 11**
def validate(x, y, z): return x or (y and z)
#
**Завдання 12**
def chain_check(a, b, c): if a < b < c: return "Increasing" elif a > b > c: return "Decreasing" else: return "Neither"
#
**Завдання 13**
def filter_true(bool_list): return [value for value in bool_list if value]
#
**Завдання 14 **
def multiplexer(a, b, c, integer): if a: return integer * 2 elif b: return integer * 3 elif c: return integer - 5 else: return integer

Для запуску програми необхідно: Встановити Python версії 3.6 або вище.
