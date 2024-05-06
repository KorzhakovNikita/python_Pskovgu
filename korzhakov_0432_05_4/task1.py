# 1.
squares = [x**2 for x in range(1, 11)]

# 2.
weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
weekdays_dict = {day: num + 1 for num, day in enumerate(weekdays)}

# 3.
tags = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
lowercase_tags = {tag.lower() for tag in tags}

print(f"Список квадратов первых 10 натуральных чисел: {squares}")
print(f"Словарь с порядковыми номерами дней недели: {weekdays_dict}")
print(f"Множество с тегами библиотек в нижнем регистре: {lowercase_tags}")
