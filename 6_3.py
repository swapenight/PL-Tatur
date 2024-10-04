def f(a):
    sum = 0
    for i in range(len(a)):
        if i % 2 != 0:
            sum += a[i]
    return sum

n = int(input("Введите длину списка: "))
a = [int(input(f"Введите {i} элемент списка: ")) for i in range(n)]
print("Исходный массив:", a)
r = f(a)
print("Сумма элементов с нечетными индексами: ", r)