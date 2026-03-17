#task a
def min4(a, b, c, d):
    return min(a, b, c, d)

a, b, c, d = map(int, input().split())
print(min4(a, b, c, d))
#task b
def power(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result

a, n = map(float, input().split())
n = int(n)
print(power(a, n))
#task c
def xor(x, y):
    return (x and not y) or (not x and y)

x, y = map(int, input().split())
print(int(xor(x, y)))
