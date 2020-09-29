import math

alpha1 = float(input())
I1 = 1 - alpha1 * math.log(1 + alpha1) + alpha1 * math.log(alpha1)
n = 1
while n != 25:
    I1 = I1 * (-alpha1) + 1 / n
    n += 1
print(I1)

alpha2 = float(input())
I1000 = 0
n = 1000
while n != 25:
    I1000 = ((1 / n) - I1000) / alpha2
    n -= 1
print(I1000)
