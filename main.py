# 1 задание

def triangle_area(x1, y1, x2, y2, x3, y3):

    area = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))

    a = 0.5 ** (x2 - x1) ** 2 + (y2 - y1) ** 2
    b = 0.5 ** (x3 - x2) ** 2 + (y3 - y2) ** 2
    c = 0.5 ** (x1 - x3) ** 2 + (y1 - y3) ** 2

    is_right = (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2)

    with open('area.txt', 'w') as f:
        f.write(str(area))

    with open('truefalse', 'w') as file:
        file.write('True' if is_right else 'False')


triangle_area(2, 2, 5, 6, 3, 0)


# 2 задание

def often_word(text: str):
    new_max = 0
    word = ''
    for i in text.split():
        max_ = text.count(i)
        if new_max < max_:
            new_max = max
            word = i
    print(word)


often_word(input('Введите текст: '))


# 3 задание

def sorting_time(n):
    times = []
    for i in range(n):
        h, m, s = map(int, input('Введите время: ').split())
        times.append((h, m, s))
    sorted_times = sorted(times)

    for hours in sorted_times:
        print(f'{hours[0]}:{hours[1]}:{hours[2]}')


sorting_time(2)
