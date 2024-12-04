# TODO импортировать необходимые молули
import csv
import json

file_input= "input.csv"
file_output = "output.json"


def task() -> None:
    with open(file_input, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]  # TODO считать содержимое csv файла

    with open(file_output, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False) # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(file_output) as output_f:
        for line in output_f:
            print(line, end="")
