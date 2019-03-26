from functions import *

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
