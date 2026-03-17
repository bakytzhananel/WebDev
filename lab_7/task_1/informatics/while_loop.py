#task a
N = int(input())
i = 1
while i * i <= N:
    print(i * i)
    i += 1
#task b
N = int(input())
i = 2
while N % i != 0:
    i += 1
print(i)
#task c
N = int(input())
x = 1
while x <= N:
    print(x, end=" ")
    x *= 2
#task d
N = int(input())
x = N
while x > 1 and x % 2 == 0:
    x //= 2
print("YES" if x == 1 else "NO")
#task e 
N = int(input())
k = 0
x = 1
while x < N:
    x *= 2
    k += 1
print(k)
