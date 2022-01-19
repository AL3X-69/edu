def termes(p):
    u = 1
    for _ in range(p):
        u = u / (u + 8)
    return u


print(termes(10))
