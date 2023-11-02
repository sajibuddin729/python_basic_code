# def doubled(x):
#     return x*2

doubled= lambda num : num*2
add= lambda x,y:x+y
r=doubled(44)
print(r)


numbers=[1,3,2,6,64,534,34,2]
double=map(doubled,numbers)
double=map(lambda x:x*2,numbers)
print(numbers)
squre=map(lambda x:x*x,numbers)
print(list(squre))



actors=[
    {'name' : 'sajib', 'age':23},
    {'name' : 'sjib', 'age':2},
    {'name' : 'saib', 'age':3},
    {'name' : 'sajb', 'age':0},
    {'name' : 'saji', 'age':1},
]
joinors= filter(lambda actor : actor['age'] < 40 , actors)
print(list(joinors))