
n = int(input("Введите конечное число последовательности: "))
for i in range (1, n):
    res = ''
    if (i % 3 == 0):
        res += 'Foo'
    if (i % 5 == 0):
        res += 'Bar'
    if not res:
        res += str(i)
    print(res)

numbers = [1, 4, 5, 7, 0, 17, 24, 45, 127, 16, 9, 3, 12, 75, 2]
numbers.sort(key = lambda
    x:
        x if x%2 != 0
        else 0
             )
print('\n', numbers)