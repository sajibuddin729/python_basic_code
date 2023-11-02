
def sum_of_odd(x, y):
    if x > y:
        x, y = y, x
    sum_odd = 0
    for i in range(x+1,y):
        if i % 2 != 0:
            sum_odd += i
    return sum_odd

t = int(input())
for _ in range(t):
    x, y = input().split()
    x = int(x)
    y = int(y)
    result = sum_of_odd(x, y)
    print(result)
