# Task 1 – Strings: Count vowels
s = input("Task 1 - Enter a string: ").lower()
vowels = "aeiou"
print("Task 1 output:", sum(1 for c in s if c in vowels))


# Task 2 – Lists: Sum of even numbers
n = int(input("Task 2 - Enter number of elements: "))
arr = list(map(int, input("Enter numbers: ").split()))
print("Task 2 output:", sum(x for x in arr if x % 2 == 0))


# Task 3 – Sets: Unique elements
n = int(input("Task 3 - Enter number of elements: "))
arr = list(map(int, input("Enter numbers: ").split()))
print("Task 3 output:", len(set(arr)))


# Task 4 – Dictionaries: Count word frequency
words = input("Task 4 - Enter words: ").split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print("Task 4 output:")
for k, v in freq.items():
    print(k, v)


# Task 5 – Functions: Check palindrome
def is_palindrome(s):
    return s == s[::-1]

s = input("Task 5 - Enter string: ")
print("Task 5 output:", "YES" if is_palindrome(s) else "NO")


# Task 6 – Tuples: Max element
t = tuple(map(int, input("Task 6 - Enter tuple numbers: ").split()))
print("Task 6 output:", max(t))


# Task 7 – Loops: Print multiplication table
n = int(input("Task 7 - Enter number for multiplication table: "))
print("Task 7 output:")
for i in range(1, 11):
    print(n, "x", i, "=", n*i)


# Task 8 – Data types: Convert binary string to integer
b = input("Task 8 - Enter binary string: ")
print("Task 8 output:", int(b, 2))


# Task 9 – List comprehensions: Squares of odd numbers
n = int(input("Task 9 - Enter number of elements: "))
arr = list(map(int, input("Enter numbers: ").split()))
print("Task 9 output:", *[x**2 for x in arr if x % 2 != 0])


# Task 10 – Sets: Set intersection
a = set(map(int, input("Task 10 - Enter first list: ").split()))
b = set(map(int, input("Task 10 - Enter second list: ").split()))
print("Task 10 output:", *sorted(a & b))
