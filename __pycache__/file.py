with  open('mes.txt','w') as file:
    file.write('i love sojib')


with  open('mes.txt','a') as file:
    file.write('i love sojib')


with  open('mes.txt','r') as file:
   text= file.read()
   print(text)