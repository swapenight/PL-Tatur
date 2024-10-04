k=0
s=input('Введите строку: ')
while '.' in s:
    if '.' in s:
        s=s.replace('.','',1)
        k+=1
print(s, '\n', k)