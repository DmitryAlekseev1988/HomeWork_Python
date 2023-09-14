def sum(a, b, m):
    if (b - 1) != 0:
        return sum(a, b - 1, m) + m
    return a

a = int(input("Введите 1-й элемент "))
b = int(input("Введите количество элементов "))
m = int(input("Введите шаг "))

for i in range(a, (sum(a, b, m)) + m, m):
    print(i, end=" ")
