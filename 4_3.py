a=int(input('введите число A: '))
b=int(input('введите число B: '))
if a>b:
    for i in range(a,b,-1):
        if i%2!=0:
            print(i)
else:
    print("введите число A большее числа B")