def write_even_lines(text: str, filename: str) -> None:

    with open(filename, "a+") as file:
        file.write(text + "\n")

    with open(filename, "r") as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            if (index + 1) % 2 == 0:
                print(line.strip())


text = """Это первая строка.
Это вторая строка.
Это третья строка.
Это четвертая строка."""
filename = "test.txt"

write_even_lines(text, filename)
