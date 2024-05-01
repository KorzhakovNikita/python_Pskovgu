def check_types(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Ошибка: Некорректный тип данных. Ожидается целое или вещественное число.")


def add(x, y):
    check_types(x, y)
    return x + y


def subtract(x, y):
    check_types(x, y)
    return x - y


def multiply(x, y):
    check_types(x, y)
    return x * y


def divide(x, y):
    check_types(x, y)
    if y == 0:
        raise ZeroDivisionError("Ошибка: Деление на ноль")
    return x / y


def power(x, y):
    check_types(x, y)
    return x ** y


def calculator():
    print("Выберите пример:")
    print("Сложение (+)")
    print("Вычитание (-)")
    print("Умножение (*)")
    print("Деление (/)")
    print("Возведение в степень (^)")
    print("Выход для завершения работы с калькулятором")

    while True:
        choice = input("Введите операцию (+, -, *, /, ^, выход ): ")

        if choice in ('+', '-', '*', '/', '^',):
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Ошибка: Введите числа заново.")
                continue

            if choice == '+':
                print("Результат:", add(num1, num2))
            elif choice == '-':
                print("Результат:", subtract(num1, num2))
            elif choice == '*':
                print("Результат:", multiply(num1, num2))
            elif choice == '/':
                try:
                    print("Результат:", divide(num1, num2))
                except (TypeError, ZeroDivisionError) as e:
                    print(e)
            elif choice == '^':
                print("Результат:", power(num1, num2))
        elif choice.lower() == 'выход':
            print("Программа завершена.")
            break
        else:
            print("Ошибка: Неверный ввод.")


calculator()
