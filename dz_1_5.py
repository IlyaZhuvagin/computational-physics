import math as m

k = float(input())
a = int(input())


def round_to_n(x, n):
    if x == 0:
        return x
    else:
        return round(x, -int(m.floor(m.log10(abs(x)))) + (n - 1))


print(round_to_n(k, a))

res = 0
for l in range(3000, 0, -1):
    res = round_to_n((res + 1 / l ** 2), 4)
print(res)
