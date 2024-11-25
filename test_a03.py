with open('data.txt', mode='w') as file:
    file.write('파이썬')
   
with open ('data.txt', mode='r') as file:
    print(file.read())    