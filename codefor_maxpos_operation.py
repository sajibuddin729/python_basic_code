N = int(input())
A = list(map(int, input().split()))
count = 0
while all(num % 2 == 0 for num in A):
    A = [num // 2 for num in A]
    count += 1
print(count if count > 0 else 0)
