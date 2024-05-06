import os
import pytest


def merge_and_write(file1_path, file2_path, output_file_path):
    try:
        with open(file1_path, 'r') as file1:
            data1 = file1.read().strip()

        with open(file2_path, 'r') as file2:
            data2 = file2.read().strip()

        merged_data = data1 + ' ' + data2

        with open(output_file_path, 'w') as output_file:
            output_file.write(merged_data)

        with open(output_file_path, 'r') as output_file:
            data = output_file.read()
        return data
    except FileNotFoundError:
        return "Один из файлов не найден"


@pytest.fixture
def create_test_files(tmp_path):
    file1_path = tmp_path / "file1.txt"
    file2_path = tmp_path / "file2.txt"
    output_file_path = tmp_path / "output.txt"

    with open(file1_path, "w") as file1:
        file1.write("Hello")

    with open(file2_path, "w") as file2:
        file2.write("World")

    yield file1_path, file2_path, output_file_path

    for file_path in [file1_path, file2_path, output_file_path]:
        if os.path.exists(file_path):
            os.remove(file_path)


def test_merge_and_write_existing_files(create_test_files):
    file1_path, file2_path, output_file_path = create_test_files
    result = merge_and_write(file1_path, file2_path, output_file_path)
    assert result == "Hello World"


def test_merge_and_write_missing_file(tmp_path):
    file1_path = tmp_path / "file1.txt"
    file2_path = tmp_path / "non_existent_file.txt"
    output_file_path = tmp_path / "output.txt"

    with open(file1_path, "w") as file1:
        file1.write("Hello")

    result = merge_and_write(file1_path, file2_path, output_file_path)
    assert result == "Один из файлов не найден"
