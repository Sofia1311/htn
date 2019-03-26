class Domain:
    name = ''
    types = []
    predicates = []
    actions = []
    methods = []
    tasks = []

class Predicate:
    name = ''
    arity = 0
    parameters = []

class Method:
    parameters = []
    task_name = ''
    task_args = []
    subtasks = []
    subtasks_cond = ''
    ordering = []
    ordering_cond = ''

class Task:
    name = ''
    parameters = []
    precondition_cond = ''
    precondition = []
    effect_cond = ''
    effect = []

class Action:
    name = ''
    parameters = []
    precondition_cond = ''
    precondition = []
    effect_cond = ''
    effect = []

def convert_to_text(Domain_file, text):
    for line in Domain_file:
        line = line.strip()
        if (len(line) > 0):
            text.append(line)
    return text

def parse_parameters(line):
    tokens = (line.strip('(').strip(')')).split()
    i = 0
    args = []
    while i < len(tokens):
        if (tokens[i][0] == '?'): 
            name = tokens[i][1:]
            i += 2
            args.append((tokens[i], name))
        i += 1
    return args

def fill_predicates(line):
    tokens = (line.strip('(').strip(')')).split()
    P = Predicate()
    P.name = tokens[0]
    i = 0
    args = []
    while i < len(tokens):
        if (tokens[i][0] == '?'):
            P.arity += 1
            name_arg = tokens[i][1:]
            i += 2
            args.append((tokens[i], name_arg))
        i += 1
    P.parameters = args
    return P

def parse_precondition_and_effect(line):
    tokens = line.split()
    is_true = 1
    if (tokens[0] == '(not'):
        is_true = 0
        line = line[5:]
    tokens = (line.strip(')').strip('(')).split()
    name = tokens[0]
    args = []
    for i in range(1, len(tokens)):
        args.append(tokens[i][1:])
    return (is_true, name, args)

def parse_subtask(line):
    tokens = (line.strip(')')).split()
    name_sub = tokens[0][1:]
    name_task = tokens[1][1:]
    args = []
    for i in range (2, len(tokens)):
        args.append(tokens[i][1:])
    return (name_sub, name_task, args)

def parse_order(line):
    tokens = (line.strip(')').strip('(')).split()
    return (tokens[0], tokens[2])

def parse_Domain(Domain_file):
    D = Domain()
    text = []
    text = convert_to_text(Domain_file, text)
    line = text[0]
    tokens = line.split()
    D.name = tokens[2][:-1]
    i = 0
    while (i < len(text)):
        line = text[i]
        tokens = line.split()
        
        if (tokens[0] == '(:types'):
            args = []
            i += 1
            while (text[i] != ')'):
                key = text[i].split()
                args.append((key[0], key[2]))
                i += 1
            D.types = args

        if (tokens[0] == '(:predicates'):
            i += 1
            while (text[i] != ')'):
                P = fill_predicates(text[i])
                i += 1
                D.predicates.append(P)

        elif (tokens[0] == '(:task'):
            T = Task()
            T.name = tokens[1]
            while (text[i] != ')'):
                line = text[i]
                tokens = line.split()
                
                if (tokens[0] == ':parameters'):
                    T.parameters = parse_parameters(line[12:])
                
                elif (tokens[0] == ':precondition'):
                    if (len(tokens) > 1 and tokens[1] == '()'):
                        T.precondition_cond = ''
                        T.precondition = []
                    else:
                        i += 1
                        T.precondition_cond = text[i][1:]
                        i += 1
                        args = []
                        while (text[i] != ')'):
                            prec = parse_precondition_and_effect(text[i])
                            args.append(prec)
                            i += 1
                        T.precondition = args
                
                elif (tokens[0] == ':effect'):
                    if (len(tokens) > 1 and tokens[1] == '()'):
                        T.effect_cond = ''
                        T.effect = []
                    else:
                        i += 1
                        T.effect_cond = text[i][1:]
                        i += 1
                        args = []
                        while (text[i] != ')'):
                            efc = parse_precondition_and_effect(text[i])
                            args.append(efc)
                            i += 1
                        T.effect = args
                i += 1
            
            D.tasks.append(T)
        
        elif (tokens[0] == '(:action'):
            A = Action()
            A.name = tokens[1]
            while (text[i] != ')'):
                line = text[i]
                tokens = line.split()
                
                if (tokens[0] == ':parameters'):
                    A.parameters = parse_parameters(line[12:])
                
                elif (tokens[0] == ':precondition'):
                    i += 1
                    A.precondition_cond = text[i][1:]
                    i += 1
                    args = []
                    while (text[i] != ')'):
                        prec = parse_precondition_and_effect(text[i])
                        args.append(prec)
                        i += 1
                    A.precondition = args
                
                elif (tokens[0] == ':effect'):
                    i += 1
                    A.effect_cond = text[i][1:]
                    i += 1
                    args = []
                    while (text[i] != ')'):
                        efc = parse_precondition_and_effect(text[i])
                        args.append(efc)
                        i += 1
                    A.effect = args
                i += 1

            D.actions.append(A)

        elif (tokens[0] == '(:method'):
            M = Method()
            M.name = tokens[1]
            while (text[i] != ')'):
                line = text[i]
                tokens = line.split()

                if (tokens[0] == ':parameters'):
                    M.parameters = parse_parameters(line[12:])
                
                elif (tokens[0] == ':task'):
                    line = line[6:]
                    tokens = (line.strip('(').strip(')')).split()
                    name = tokens[0]
                    args = []
                    for j in range (1, len(tokens)):
                        args.append(tokens[j][1:])
                    M.task_name = name
                    M.task_args = args
                elif (tokens[0] == ':subtasks'):
                    M.subtasks_cond = tokens[1][1:]
                    args = []
                    i += 1
                    while (text[i] != ')'):
                        arg = parse_subtask(text[i])
                        args.append(arg)
                        i += 1
                    M.subtasks = args
                elif (tokens[0] == ':ordering'):
                    M.ordering_cond = tokens[1][1:]
                    i += 1
                    args = []
                    while (text[i] != ')'):
                        arg = parse_order(text[i])
                        args.append(arg)
                        i += 1
                    M.ordering = args
                i += 1
            D.methods.append(M)
        i += 1
    
    return D

Domain_file = open('Domain.hddl', 'r')
D = parse_Domain(Domain_file)

#Вывод содержимого домена:
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
            print('\t\t', method.subtasks_cond, sep='', end = '')
        print()
    print('\t', 'ordering:', sep='')
    size_ord = len(method.ordering)
    cur = 0
    for args in method.ordering:
        cur += 1
        print('\t\t', end = '')
        print(args[0], ' < ', args[1], sep='', end='')
        if (cur < size_eff):
            print('\t\t', task.effect_cond, sep='', end = '')
        print()
