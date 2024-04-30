num_count = int(input("Введите количество чисел в списке: "))
exponent = int(input("Введите степень для возведения: "))

num_list = []

for i in range(num_count):
    num = input(f"Введите число {i + 1}: ")
    try:
        num = float(num)
        num_list.append(num)
    except ValueError:
        num_list.append(num)

powered_nums = []
for num in num_list:
    if isinstance(num, str):
        powered_nums.append(num * exponent)
    else:
        powered_nums.append(num ** exponent)

print(f"Числа, возведенные в степень: {powered_nums}")

