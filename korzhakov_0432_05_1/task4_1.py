ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
user_shot = input("Введите координаты выстрела: ").upper()

if ship.find(user_shot) != -1:
    print("Попадание!")
else:
    print("Мимо!")
