digit = int(input("Введите число: "))
negative_sum = 0
positive_sum = 0

for i in range(-digit, digit + 1):
    print(i)
    if i < 0:
        negative_sum += i
    else:
        positive_sum += i

print("Сумма отрицательных чисел:", negative_sum)
print("Сумма положительных чисел:", positive_sum)
