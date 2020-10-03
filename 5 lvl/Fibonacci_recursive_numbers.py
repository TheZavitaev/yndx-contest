"""
Помогите жителям Трешландии понять, сколько питомцев они могут завести.
Напишите рекурсивную реализацию функции, определяющей по номеру значение n-ого числа Фибоначчи.
Формат ввода
На вход подается n - целое число в диапазоне от 0 до 30.
Формат вывода
Нужно вывести n-ое число Фибоначчи.
Примечания
Функция должна быть реализована рекурсивно.
Обратите внимание на то, что в этом спринте считывать данные нужно из файла input.txt.
"""

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main(input_file):
    with open(input_file) as f:
        input_file = f.read().rstrip().split('\n')
    n = int(input_file[0])
    return fibonacci(n)


if __name__ == 'main':
    input_txt = 'input.txt'

    with open('output.txt', 'w') as f:
        f.write(str(main(input_txt)))
