def pack4(a, b, c, d):
    if c== 0:
        c = d
        d = 0

    if b == 0:
        b = c
        c = d
        d = 0

    if a == 0:
        a = b
        b = c
        c = d
        d = 0

    if a == b:
        a = a * 2
        b = c
        c = d
        d = 0

    if b == c:
        b = b * 2
        c = d
        d = 0

    if c==d:
        c = c * 2
        d = 0

    return a, b, c, d


print(pack4(2,8,4,4))
print(pack4(2,2,2,2))
print(pack4(2,0,4,4))
print(pack4(0,0,4,0))

