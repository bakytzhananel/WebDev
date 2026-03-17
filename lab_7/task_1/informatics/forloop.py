#task a
a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=" ")
#task b
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a, b + 1):
    if i % d == c:
        print(i, end=" ")
#task c
import math
a = int(input())
b = int(input())
for i in range(a, b + 1):
    if int(math.sqrt(i)) ** 2 == i:
        print(i, end=" ")
#task d
x = input()
d = input()
print(x.count(d))
#task e
x = input()
print(sum(int(d) for d in x))
#task f
x = input()
print(int(x[::-1]))
#task g
x = int(input())
for i in range(2, x + 1):
    if x % i == 0:
        print(i)
        break
#task h
x = int(input())
for i in range(1, x + 1):
    if x % i == 0:
        print(i, end=" ")
#task i
x = int(input())
count = 0
i = 1
while i * i <= x:
    if x % i == 0:
        count += 2 if i * i != x else 1
    i += 1
print(count)
#task j
total = 0
for _ in range(100):
    total += int(input())
print(total)
#task k
n = int(input())
total = 0
for _ in range(n):
    total += int(input())
print(total)
#task l
x = int(input())
while x >= 10:
    x = sum(int(d) for d in str(x))
print(x)
#task m
n = int(input())
count = 0
for _ in range(n):
    if int(input()) == 0:
        count += 1
print(count)
