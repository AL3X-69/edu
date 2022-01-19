def seuil(A):
    U = 2
    n = 0
    while U <= A:
        U = U + 2 * n + 1
        n += 1

    return n


def minimum(A):
    u = 1
    n = 0
    while u <= A:
        u = 1 / 3 * u + n - 2
        n += 1
    return n


def baleines():
    u = 3000
    n = 2019
    while u >= 2000:
        u = 0.95 * u + 76
        n += 1
    return n


# >>> min(200)
# 137
# >>> min(5000)
# 3337

print(seuil(100))
print(seuil(1000))
