import json

# Исходные данные в формате строки
data = '''
[
    {"score": 0.0009456152645028281, "weight": 1},
    {"score": 0.6477, "weight": 2},
    {"score": 0.5, "weight": 2}
]
'''


def task(json_string: str) -> float:
    # Преобразуем строку JSON в Python-объект
    data = json.loads(json_string)

    # Суммируем произведения score * weight
    total = sum(item["score"] * item["weight"] for item in data)

    # Возвращаем округленный результат
    return round(total, 3)


# Вызываем функцию с JSON-строкой
print(task(data))
