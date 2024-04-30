dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

keys_set = set()
values_set = set()

for key, value in dct.items():
    keys_set.add(key)
    values_set.add(value)

result_set = keys_set | values_set

print(f"keys_set: {keys_set}")
print(f"values_set: {values_set}")
print(f"Результат объединения множеств: {result_set}")
