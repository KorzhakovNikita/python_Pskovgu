import re
import calendar


def generate_calendar(date_str):
    if not re.match(r'^\d{4}-\d{2}$', date_str):
        return "Неверный формат даты. Используйте формат 'ГГГГ-ММ'."

    year, month = map(int, date_str.split('-'))

    if month < 1 or month > 12:
        return "Неверный номер месяца. Месяц должен быть от 01 до 12."

    cal = calendar.month(year, month)

    return cal


date = input("Введите дату в формате 'ГГГГ-ММ': ")
print(generate_calendar(date))

# регулярное выражение для российского номера. Я здесь не понял нужна ли фунция, но в условии только написать регулярное выражение.
phone_rus = re.compile(r'^(\+7|7|8)\d{10}$')
