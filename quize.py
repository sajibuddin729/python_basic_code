# def solve(a, b):
#     return a**b
    
# result = solve(2, 4)
# print(result)

# def display_person(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")


# display_person(Name="Amir Khan", Age="45")

# numbers =[7,8,5,4,3,2,4]
# print(numbers[::-1])

# numbers =[22,19,19,14,33]
# numbers.sort()
# print(numbers)
numbers = [10, 20, 30, 40, 50]
print(numbers[-4:-1])

numbers = [9, 15, 2, 36]
numbers[1:4] = [20, 14, 36]
print(numbers)

person_info = {"name": "Sakib", "salary": 80000}
value = person_info.get("salary")
print(value)
try:
    result =20/5
except:
    print("error happened")
finally:
    print("finally here")
num = lambda a:a*a
print(num(2**2))