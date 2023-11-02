
# # Removal of elements in a Array

# # importing "array" for array operations
# import array

# # initializing array with array values
# # initializes array with signed integers
# arr = array.array('i', [1, 2, 3, 1, 5])

# # printing original array
# print("The new created array is : ", end="")
# for i in range(0, 5):
# 	print(arr[i], end=" ")

# print("\r")

# # using pop() to remove element at 2nd position
# print("The popped element is : ", end="")
# print(arr.pop(2))

# # printing array after popping
# print("The array after popping is : ", end="")
# for i in range(0, 4):
# 	print(arr[i], end=" ")

# print("\r")

# # using remove() to remove 1st occurrence of 1
# arr.remove(1)

# # printing array after removing
# print("The array after removing is : ", end="")
# for i in range(0, 3):
# 	print(arr[i], end=" ")
numbers=[43,34,54,23,12,43,54,5657,43,642232,45456,3434,34,244]
numbers.append(43432)
print(numbers)
numbers.insert(4,343)
print(numbers)
numbers.remove(34)
print(numbers)
last=numbers.pop()
print(last,numbers)
index=numbers.index(23)
print(index)
count=numbers.count(43)
print(count)
sorted=numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)