import itertools


def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def dividedby(x, y):
    if y == 0:
        return 0

    return x / float(y)


def times(x, y):
    return x * y


def get_solutions(numbers):
    numbers = [int(i) for i in numbers]
    functions = [plus, minus, dividedby, times]
    function_combinations = [f for f in itertools.product(functions, repeat=3)]

    combinations = set(i for i in itertools.permutations(numbers))

    answers = []
    for a, b, c, d in combinations:
        for f1, f2, f3 in function_combinations:
            res1 = round(f3(f2(f1(a, b), c), d), 7)
            if res1 == 24.0:
                answers.append('{a} {f1} {b} {f2} {c} {f3} {d}'.format(
                    a=a, b=b, c=c, d=d, f1=f1.__name__, f2=f2.__name__, f3=f3.__name__
                ))

            res2 = round(f2(f1(a, b), f3(c, d)), 7)
            if res2 == 24.0:
                answers.append('({a} {f1} {b}) {f2} ({c} {f3} {d})'.format(
                    a=a, b=b, c=c, d=d, f1=f1.__name__, f2=f2.__name__, f3=f3.__name__
                ))

            res3 = round(f1(a, f3(f2(b, c), d)), 7)
            if res3 == 24.0:
                answers.append('{a} {f1} (({b} {f2} {c}) {f3} {d})'.format(
                    a=a, b=b, c=c, d=d, f1=f1.__name__, f2=f2.__name__, f3=f3.__name__
                ))

            res4 = round(f3(f1(a, f2(b, c)), d), 7)
            if res4 == 24.0:
                answers.append('({a} {f1} ({b} {f2} {c})) {f3} {d}'.format(
                    a=a, b=b, c=c, d=d, f1=f1.__name__, f2=f2.__name__, f3=f3.__name__
                ))

            res5 = round(f1(a, f2(b, f3(c, d))), 7)
            if res5 == 24.0:
                answers.append('{a} {f1} ({b} {f2} ({c} {f3} {d}))'.format(
                    a=a, b=b, c=c, d=d, f1=f1.__name__, f2=f2.__name__, f3=f3.__name__
                ))

    return answers
