from classes import *

def convert_to_text(file, text):
    for line in file:
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

def parse_problem_subtask(line):
    tokens = (line.strip(')')).split()
    name_sub = tokens[0][1:]
    name_task = tokens[1][1:]
    args = []
    for i in range (2, len(tokens)):
        args.append(tokens[i])
    return (name_sub, name_task, args)
