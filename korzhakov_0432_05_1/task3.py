digit = input("Введите трехзначное число, где все цифры различны: ")

if not digit.isdigit() or len(digit) != 3 or len(set(digit)) != 3:
    print("Ошибка: Введенное число не соответствует условиям.")
else:
    digits = [digit[0] + digit[1] + digit[2],
              digit[0] + digit[2] + digit[1],
              digit[1] + digit[0] + digit[2],
              digit[1] + digit[2] + digit[0],
              digit[2] + digit[0] + digit[1],
              digit[2] + digit[1] + digit[0]]

    for i in digits:
        print(i, end=' ')
