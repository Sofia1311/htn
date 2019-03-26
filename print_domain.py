from domain_parser import *

print('Domain')
print('name: ', D.name)
print('types:')
for type in D.types:
    print('\t', type[0], ' is a ', type[1], sep='')
i = 0
print('predicates:')
for predicate in D.predicates:
    i += 1
    print('\t', i, ': ', 'name: ', predicate.name, sep='')
    print('\t', 'parameters:', sep='')
    for args in predicate.parameters:
        print('\t\t', args[1], ' is a', args[0])
i = 0
print('actions:')
for action in D.actions:
    i += 1
    print('\t', i, ': ', 'name: ', action.name, sep='')
    print('\t', 'parameters:', sep='')
    for args in action.parameters:
        print('\t\t', args[1], ' is a ', args[0], sep='')
    print('\t', 'precondition:', sep='')
    size_prec = len(action.precondition)
    cur = 0
    for args in action.precondition:
        cur += 1
        print('\t\t', end = '')
        if (args[0] == 0):
            print('!', end='')
        print(args[1], '(', sep='', end='')
        now = 0
        size_args = len(args[2])
        for param in args[2]:
            now += 1
            print(param, end='')
            if (now < size_args):
                print(', ', end='')
        print(')')
        if (cur < size_prec):
            print('\t\t', action.precondition_cond, sep='', end = '')
        print()
    print('\t', 'effect:', sep='')
    size_eff = len(action.effect)
    cur = 0
    for args in action.effect:
        cur += 1
        print('\t\t', end = '')
        if (args[0] == 0):
            print('!', end='')
        print(args[1], '(', sep='', end='')
        now = 0
        size_args = len(args[2])
        for param in args[2]:
            now += 1
            print(param, end='')
            if (now < size_args):
                print(', ', end='')
        print(')')
        if (cur < size_eff):
            print('\t\t', action.effect_cond, sep='', end = '')
        print()
i = 0
print('tasks:')
for task in D.tasks:
    i += 1
    print('\t', i, ': ', 'name: ', task.name, sep='')
    print('\t', 'parameters:', sep='')
    for args in task.parameters:
        print('\t\t', args[1], ' is a ', args[0], sep='')
    print('\t', 'precondition:', sep='')
    size_prec = len(task.precondition)
    cur = 0
    for args in task.precondition:
        cur += 1
        print('\t\t', end = '')
        if (args[0] == 0):
            print('!', end='')
        print(args[1], '(', sep='', end='')
        now = 0
        size_args = len(args[2])
        for param in args[2]:
            now += 1
            print(param, end='')
            if (now < size_args):
                print(', ', end='')
        print(')')
        if (cur < size_prec):
            print('\t\t', task.precondition_cond, sep='', end = '')
        print()
    print('\t', 'effect:', sep='')
    size_eff = len(task.effect)
    cur = 0
    for args in task.effect:
        cur += 1
        print('\t\t', end = '')
        if (args[0] == 0):
            print('!', end='')
        print(args[1], '(', sep='', end='')
        now = 0
        size_args = len(args[2])
        for param in args[2]:
            now += 1
            print(param, end='')
            if (now < size_args):
                print(', ', end='')
        print(')')
        if (cur < size_eff):
            print('\t\t', task.effect_cond, sep='', end = '')
        print()

i = 0
print('methods:')
for method in D.methods:
    i += 1
    print('\t', i, ': ', 'name: ', method.name, sep='')
    print('\t', 'parameters:', sep='')
    for args in method.parameters:
        print('\t\t', args[1], ' is a ', args[0], sep='')
    print('\t', 'task: ', sep='', end='')
    print(method.task_name, '(', sep='', end='')
    cur = 0
    size_args = len(method.task_args)
    for args in method.task_args:
        cur += 1
        print(args, end='')
        if (cur < size_args):
            print(', ', end='')
    print(')')
    print('\t', 'subtasks:', sep='')
    size_sub = len(method.subtasks)
    cur = 0
    for args in method.subtasks:
        cur += 1
        print('\t\t', end = '')
        print(args[0], ': ', args[1], '(', sep='', end='')
        now = 0
        size_args = len(args[2])
        for param in args[2]:
            now += 1
            print(param, end='')
            if (now < size_args):
                print(', ', end='')
        print(')')
        if (cur < size_sub):
            print('\t\t', method.subtasks_cond, sep='', end='')
        print()
    print('\t', 'ordering:', sep='')
    size_ord = len(method.ordering)
    cur = 0
    for args in method.ordering:
        cur += 1
        print('\t\t', end = '')
        print(args[0], ' < ', args[1], sep='')
        if (cur < size_ord):
            print('\t\t', method.ordering_cond, sep='', end='')
            print()
