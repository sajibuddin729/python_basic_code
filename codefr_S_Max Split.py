def max_split(s):
    count = 0
    result = []
    c_s = ""
    for c in s:
        c_s += c
        if c_s.count('L') == c_s.count('R'):
            count += 1
            result.append(c_s)
            c_s = ""
    print(count)
    for r in result:
        print(r)
s = input().strip()
max_split(s)
