N = int(input())
nums = list(map(int, input().split()))
mp = {}
for num in nums:
    if num in mp:
        mp[num] += 1
    else:
        mp[num] = 1
sum = 0
for val, cnt in mp.items():
    if cnt < val:
        sum += cnt
    elif cnt > val:
        sum += (cnt - val)
print(sum)
