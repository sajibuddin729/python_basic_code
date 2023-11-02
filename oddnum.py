numbers=[32,43,646,232,565,23,5,78,45,23,4532,54]
odds=[]
for num in numbers:
    if num%2==1 and num % 5==0:
        odds.append(num)
print(odds)
odd_num=[num for num in numbers if num%2==1 if num%5==0]
print(odd_num)


