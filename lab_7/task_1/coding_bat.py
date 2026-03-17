# Warmup-1

# Task 1: sleep_in
def sleep_in(weekday, vacation):
    return not weekday or vacation

# Task 2: monkey_trouble
def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

# Task 3: sum_double
def sum_double(a, b):
    return 2*(a+b) if a == b else a+b

# Task 4: diff21
def diff21(n):
    return 2*abs(n-21) if n > 21 else abs(n-21)

# Task 5: parrot_trouble
def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

# Warmup-2

# Task 1: string_times
def string_times(str, n):
    return str * n

# Task 2: front_times
def front_times(str, n):
    front = str[:3]
    return front * n

# Task 3: string_bits
def string_bits(str):
    return str[::2]

# Task 4: caught_speeding
def caught_speeding(speed, is_birthday):
    allowance = 5 if is_birthday else 0
    if speed <= 60 + allowance:
        return 0
    elif speed <= 80 + allowance:
        return 1
    else:
        return 2

# String-1

# Task 1: hello_name
def hello_name(name):
    return "Hello " + name + "!"

# Task 2: make_abba
def make_abba(a, b):
    return a + b + b + a

# Task 3: extra_end
def extra_end(str):
    return str[-2:] * 3

# Task 4: first_two
def first_two(str):
    return str[:2]

# Task 5: first_half
def first_half(str):
    return str[:len(str)//2]


# String-2

# Task 1: double_char
def double_char(str):
    return ''.join(c*2 for c in str)

# Task 2: count_hi
def count_hi(str):
    return str.count('hi')

# Task 3: cat_dog
def cat_dog(str):
    return str.count('cat') == str.count('dog')

# Task 4: end_other
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)

# List-1

# Task 1: first_last6
def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

# Task 2: same_first_last
def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]

# Task 3: make_pi
def make_pi():
    return [3,1,4]

# Task 4: sum3
def sum3(nums):
    return sum(nums)

# Task 5: rotate_left3
def rotate_left3(nums):
    return nums[1:] + nums[:1]

# List-2

# Task 1: count_evens
def count_evens(nums):
    return sum(1 for x in nums if x % 2 == 0)

# Task 2: big_diff
def big_diff(nums):
    return max(nums) - min(nums)

# Task 3: centered_average
def centered_average(nums):
    nums_sorted = sorted(nums)
    return sum(nums_sorted[1:-1]) // (len(nums_sorted) - 2)

# Task 4: sum13
def sum13(nums):
    total = 0
    skip = False
    for x in nums:
        if x == 13:
            skip = True
        elif skip:
            skip = False
        else:
            total += x
    return total

# Task 5: has22
def has22(nums):
    return any(nums[i] == 2 and nums[i+1] == 2 for i in range(len(nums)-1))
