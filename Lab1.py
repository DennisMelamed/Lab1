__author__ = 'Dennis Melamed'

# Csci 1913 Lab 1: Equation Solver
#     Dennis Melamed
#     18 Sept. 2015
#
# Given an equation in list form and a variable to solve for,
# solve() will return a list solved for that variable

# return different portions of an expression
def left(e):
    return e[0]


def op(e):
    return e[1]


def right(e):
    return e[2]


# is the variable given within the expression given (either right or left side)?
def isInside(v, e):
    if v == e:
        return True
    # call isInside again if we're operating on a list
    if len(e) != 1:
        return isInside(v, left(e)) or isInside(v, right(e))
    else:
        return False


# makes expressions interpretable by solving(): variable is on left side
def solve(v, q):
    if isInside(v, left(q)):
        return solving(v, q)
    elif isInside(v, right(q)):
        qnew = [right(q)] + [op(q)] + [left(q)]
        return solving(v, qnew)
    else:
        return None


# sends the expression on the left side to the appropriate solvingOperator() function
def solving(v, q):
    left_side = left(q)
    if v == left_side:
        return q
    elif op(left_side) == '+':
        return solvingAdd(v, q)
    elif op(left_side) == '-':
        return solvingSubtract(v, q)
    elif op(left_side) == '/':
        return solvingDivide(v, q)
    elif op(left_side) == '*':
        return solvingMultiply(v, q)
    else:
        return None


def solvingAdd(v, q):
    left_side = left(q)
    # rebuild list using needed equation
    if isInside(v, left(left_side)):
        qnew = [left(left_side)] + [op(q)] + [[right(q)] + ["-"] + [right(left_side)]]
    if isInside(v, right(left_side)):
        qnew = [right(left_side)] + [op(q)] + [[right(q)] + ["-"] + [left(left_side)]]
    return solving(v, qnew)


def solvingSubtract(v, q):
    left_side = left(q)
    if isInside(v, left(left_side)):
        qnew = [left(left_side)] + [op(q)] + [[right(q)] + ["+"] + [right(left_side)]]
    if isInside(v, right(left_side)):
        qnew = [right(left_side)] + [op(q)] + [[left(left_side)] + ["-"] + [right(q)]]
    return solving(v, qnew)


def solvingMultiply(v, q):
    left_side = left(q)
    if isInside(v, left(left_side)):
        qnew = [left(left_side)] + [op(q)] + [[right(q)] + ["/"] + [right(left_side)]]
    if isInside(v, right(left_side)):
        qnew = [right(left_side)] + [op(q)] + [[right(q)] + ["/"] + [left(left_side)]]
    return solving(v, qnew)


def solvingDivide(v, q):
    left_side = left(q)
    if isInside(v, left(left_side)):
        qnew = [left(left_side)] + [op(q)] + [[right(q)] + ["*"] + [right(left_side)]]
    if isInside(v, right(left_side)):
        qnew = [right(left_side)] + [op(q)] + [[left(left_side)] + ["/"] + [right(q)]]
    return solving(v, qnew)

# Instructor tests
print isInside('x', 'y')  # False
print isInside('x', ['x', '+', 'y'])  # True
print isInside('x', ['a', '+', 'b'])  # False
print isInside('x', [['m', '*', 'x'], '+', 'b'])  # True

print solve('x', [['a', '+', 'x'], '=', 'c'])  # ['x', '=', ['c', '-', 'a']]
print solve('x', [['x', '+', 'b'], '=', 'c'])  # ['x', '=', ['c', '-', 'b']]

print solve('x', [['a', '-', 'x'], '=', 'c'])  # ['x', '=', ['a', '-', 'c']]
print solve('x', [['x', '-', 'b'], '=', 'c'])  # ['x', '=', ['c', '+', 'b']]

print solve('x', [['a', '*', 'x'], '=', 'c'])  # ['x', '=', ['c', '/', 'a']]
print solve('x', [['x', '*', 'b'], '=', 'c'])  # ['x', '=', ['c', '/', 'b']]

print solve('x', [['a', '/', 'x'], '=', 'c'])  # ['x', '=', ['a', '/', 'c']]
print solve('x', [['x', '/', 'b'], '=', 'c'])  # ['x', '=', ['c', '*', 'b']]

print solve('x', ['y', '=', [['m', '*', 'x'], '+', 'b']])
# ['x', '=', [['y', '-', 'b'], '/', 'm']

# own test
print solve('z', [['y', '+', 'x'], '=', [['d', '/', 's'], '*', ['g', '+', 'z']]])
# ['z', '=', [[['y', '+', 'x'], '/', ['d', '/', 's']], '-', 'g']]
