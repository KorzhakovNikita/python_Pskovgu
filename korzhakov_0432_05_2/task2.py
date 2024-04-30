user_string = input("Введите строку: ").lower()

char_count = {}

for char in user_string:
    if char != ' ':
        char_count[char] = user_string.count(char)

print(f"Словарь с количеством символов в строке: {char_count}")
