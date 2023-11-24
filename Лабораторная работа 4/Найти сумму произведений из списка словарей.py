# TODO решите задачу
import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    summ = sum(item["score"] * item["weight"] for item in data)
    res = round(summ, 3)
    return res

print(task())