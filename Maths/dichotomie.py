from math import e


def alpha(precision):
    a = 0
    b = 1
    while b - a >= precision:
        c = (b + a) / 2
        f = c ** 2 * e ** c
        if f <= 1:
            a = c
        else:
            b = c
    return a, b


print(alpha(0.0001))
