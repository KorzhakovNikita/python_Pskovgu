import random


def get_two_random_elements(lst):
    return random.sample(lst, 2)


list_el = [100, 400, 500, 10, 50, "Банан", "Клубника", "Камень", "Морковь", "Огурец", "Пицца"]
print("Случайные элементы из списка:", get_two_random_elements(list_el))
