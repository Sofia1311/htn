from problem_parser import *

print('Problem')
print('name:', P.name)
print('domain name:', P.domain)
print('objects:')
for obj in P.objects:
    print('\t', obj[0], ' is a ', obj[1], sep='')
print('parameters:', sep='')
for args in P.htn_parameters:
    print('\t', args[1], ' is a ', args[0], sep='')
print('subtasks:')
size_sub = len(P.htn_subtasks)
cur = 0
for args in P.htn_subtasks:
    cur += 1
    print('\t', end = '')
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
        print('\t', P.htn_subtasks_cond, sep='', end='')
    print()
print('ordering:')
size_ord = len(P.htn_ordering)
cur = 0
for args in P.htn_ordering:
    cur += 1
    print('\t', end = '')
    print(args[0], ' < ', args[1], sep='')
    if (cur < size_ord):
        print('\t', P.htn_ordiring_cond, sep='', end = '')
    print()
