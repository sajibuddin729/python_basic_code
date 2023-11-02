
# def print_digits(n):
#     digits = []
#     while n > 0:
#         digits.append(str(n % 10))
#         n //= 10
#     print(' '.join(digits[::-1]))

# #

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     print_digits(n)
t = int(input())

for _ in range(t):
    s = input().strip()
    reversed_s = s[::-1]
    
    for char in reversed_s:
        print(char, end=' ')
    
    print()