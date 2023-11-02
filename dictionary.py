numbers=[12,56,98,56,12,98]
#key value pair
#{key:value,key:value}
person ={'name':'sajib','age':23,'job':'student'}
print(person)
print(person['job'])
print(person.keys())
person['language']='python'
print(person)


for key,value in person.items():
    print(key,value)


