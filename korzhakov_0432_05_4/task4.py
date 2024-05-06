def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(
            f"Функция {func.__name__} была вызвана с позиционными аргументами {args} и именованными аргументами {kwargs}")
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def fibonacci_generator(n: int):
    print(f"Первые {n} чисел Фибоначчи:")
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


fibonacci_sequence = fibonacci_generator(10)
for num in fibonacci_sequence:
    print(num, end=" ")
