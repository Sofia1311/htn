from classes import *
from functions import *

def parse_Problem(Problem_file):
    P = Problem()
    text = []
    text = convert_to_text(Problem_file, text)
    line = text[1]
    tokens = line.split()
    P.name = tokens[1][:-1]
    i = 0
    while (i < len(text)):
        line = text[i]
        tokens = line.split()
        if (tokens[0] == '(:domain'):
            P.domain = tokens[1][:-1]
        elif (tokens[0] == '(:objects'):
            i += 1
            while (text[i] != ')'):
                tokens = text[i].split()
                P.objects.append((tokens[0], tokens[2]))
                i += 1
        elif (tokens[0] == ':parameters'):
            P.htn_parameters = parse_parameters(line[12:])
        elif (tokens[0] == ':subtasks'):
            P.htn_subtasks_cond = tokens[1][1:]
            args = []
            i += 1
            while (text[i] != ')'):
                arg = parse_problem_subtask(text[i])
                args.append(arg)
                i += 1
            P.htn_subtasks = args
        elif (tokens[0] == ':ordering'):
            P.htn_ordering_cond = tokens[1][1:]
            i += 1
            args = []
            while (text[i] != ')'):
                arg = parse_order(text[i])
                args.append(arg)
                i += 1
            P.htn_ordering = args
        elif (tokens[0] == ':init'):
            i += 1
            while (text[i] != ')'):
                tokens = (text[i].strip('(').strip(')')).split()
                name = tokens[0]
                args = []
                for j in range(1, len(tokens)):
                    args.append(tokens[j])
                P.init.append((name, args))
                i += 1
        i += 1
    return P

Problem_file = open('Problem.hddl', 'r')
P = parse_Problem(Problem_file)
