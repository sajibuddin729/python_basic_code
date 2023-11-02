#list  use []
#tuple ()
#set {}
#set ar modde dublicate hoi nah, and ekhan a kono order follow kore nah
numbers=[6,3,4,5,1,2,6,7,3,4,2,9]
numbers_set= set(numbers)
print(numbers_set)

if 92 in numbers_set:
    print('exits')
elif 98 in numbers_set:
    print ('yes')
else :
    print('no')


a={1,2,3,4}
b={1,4,5,6,2}
print(a&b)
print(a|b)