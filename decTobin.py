
# Function to convert Decimal number
# to Binary number
 
# def decimalToBinary(n):
#     return bin(n).replace("0b","")
 
# if __name__ == '__main__':
#     print(decimalToBinary(8))
#     print(decimalToBinary(18))
#     print(decimalToBinary(7))





n = 4
binary = format(n, 'b')
print(binary) # Output: '100'
binary = '100'
decimal = int(binary, 2)
print(decimal) # Output: 4

