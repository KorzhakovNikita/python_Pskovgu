while True:
    digit_input = input("Введите число или 'exit' для выхода: ")

    if digit_input.lower() == 'exit':
        break

    if not digit_input.isdigit():
        print("Ошибка: Введенные данные не являются числом.")
        continue

    print("Длина введенного числа:", len(digit_input))
