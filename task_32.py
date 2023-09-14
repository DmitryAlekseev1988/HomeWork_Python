list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

def f(list_1, min_1, max_1):
    for i in range(len(list_1)):
        if min_1 <= list_1[i] <= max_1:
            print(i, end=" ")

min_el = int(input("Введите min "))
max_el = int(input("Введите max "))

f(list_1, min_el, max_el)
