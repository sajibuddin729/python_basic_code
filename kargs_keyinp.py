def fam(first,last,**addition):
    name=f'{first} {last}'
    for k,v in addition.items():
        print(k,v)
    return name
name=fam(first='sajib',last='uddin',title= 'student',title2='broken_man')
print(name)