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

class Problem:
    name = ''
    domain = ''
    objects = []
    htn_parameters = []
    htn_subtasks_cond = ''
    htn_subtasks = []
    htn_ordering_cond = ''
    htn_ordering = []
    init = []
