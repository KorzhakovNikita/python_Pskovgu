name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = input("Введите ваш возраст: ")

# через format, который давно устрарел :D
print("Ваше имя: {}, Фамилия: {}, Возраст: {} лет.".format(name, surname, age))
# через f-строку
print(f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет.")
