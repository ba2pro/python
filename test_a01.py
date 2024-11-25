
f= open ('pyzen.txt', 'wt')
f.write('파이썬 철학\n') 
f.write('아름다움이 추한 것보다 낫다\n')
f.write('나 일하러 가는 겨야 \n')
f.close()


f = open ('pyzen.txt', mode='r')
s = f.read()
print(s)
f.close()
 