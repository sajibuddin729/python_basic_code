
# def fibo(n):
#     f = [0, 1]
#     for i in range(2, n):
#         n_f = f[i - 1] + f[i - 2]
#         f.append(n_f)
#     return f

# n = int(input())
# ans = fibo(n)
# print(' '.join(map(str, ans)))
def main():
    n = int(input())
    fibo = [0] * (n + 5)
    fibo[1] = 0
    fibo[2] = 1
    for i in range(1, n + 1):
        if i == 1 or i == 2:
            print(fibo[i], end=" ")
        else:
            fibo[i] = fibo[i - 1] + fibo[i - 2]
            print(fibo[i], end=" ")

if __name__ == "__main__":
    main()
