
def check_truth(a, b, c):
    return (a and b) or c
def logical_equivalence(a, b):
    return a == b
def xor(a, b):
    return (a and not b) or (not a and b)
def greet(condition):
    if condition:
        return "Hello, World!"
    else:
        return "Goodbye, World!"
def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y != z != x:
        return "All different"
    else:
        return "Neither"


def parity(number):
    binary_repr = bin(number)
    count_ones = binary_repr.count('1')
    return count_ones % 2 == 0

def majority_vote(a, b, c):
    return sum([a, b, c]) > 1


def switch(condition):
    return not condition
def ternary_check(condition, if_true, if_false):
    return if_true if condition else if_false
def validate(x, y, z):
    return x or (y and z)
def chain_check(a, b, c):
    if a < b < c:
        return "Increasing"
    elif a > b > c:
        return "Decreasing"
    else:
        return "Neither"
def filter_true(bool_list):
    return [value for value in bool_list if value]
def multiplexer(a, b, c, integer):
    if a:
        return integer * 2
    elif b:
        return integer * 3
    elif c:
        return integer - 5
    else:
        return integer

