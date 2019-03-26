from domain_parser import *
from problem_parser import *

file = open('f.txt', 'w')

for actions in D.actions:
    file.write('def ')
    file.write(actions.name)
    file.write('(')
    siz = len(actions.parameters)
    now = 0
    for types, names in actions.parameters:
        now += 1
        file.write(names)
        if (now < siz):
            file.write(',')
    file.write('):\n')
    cur = 0
    s = len(actions.precondition)
    file.write('    ')
    file.write('if ')
    for pred in actions.precondition:
        cur += 1
        if (pred[0] == 0):
            file.write('not')
        file.write(pred[1])
        file.write('(')
        siz = len(pred[2])
        now = 0
        for args in pred[2]:
            now += 1
            file.write(args)
            if (now < siz):
                file.write(',')
        file.write(')')
        if (cur < s):
            file.write(' and ')
    file.write(':\n    \treturn 1\n    else:\n    \treturn 0\n')

for pred in D.predicates:
    file.write('def ')
    file.write(pred.name)
    file.write('(')
    siz = len(pred.parameters)
    now = 0
    for types, names in pred.parameters:
        now += 1
        file.write(names)
        if (now < siz):
            file.write(',')
    file.write('):\n')
    file.write('    ')
    file.write('for un in P.init:\n        if un[0] == pred.name and un[1] == pred.parameters')
    file.write(':\n            return 1\n    return 0\n')

