

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
