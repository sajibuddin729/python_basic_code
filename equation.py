
X, N = map(int, input().split())
result = 0
power_of_X = 1
for i in range(N + 1):
    if i % 2 == 0:
        result += power_of_X
    power_of_X *= X
print(result-1)
