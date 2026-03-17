#task a
n = int(input())
a = list(map(int, input().split()))
for i in range(0, n, 2):
    print(a[i], end=" ")
#task b
n = int(input())
a = list(map(int, input().split()))
for x in a:
    if x % 2 == 0:
        print(x, end=" ")
#task c
n = int(input())
a = list(map(int, input().split()))
count = 0
for x in a:
    if x > 0:
        count += 1
print(count)
#task d
n = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(1, n):
    if a[i] > a[i - 1]:
        count += 1
print(count)
#task e
n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
    if a[i] * a[i - 1] > 0:
        print("YES")
        break
else:
    print("NO")
#task f
n = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(1, n - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        count += 1
print(count)
#task g
n = int(input())
a = list(map(int, input().split()))
for i in range(n // 2):
    a[i], a[n - 1 - i] = a[n - 1 - i], a[i]
print(*a)
