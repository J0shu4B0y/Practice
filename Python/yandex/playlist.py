"""
Создай плейлист

Маруся очень любит слушать рок музыку. У нее есть два плейлиста: один - с песнями
российских исполнителей, другой - зарубежных. Помогите Марусе создать плейлист, в
котором иностранные и российские композиции шли бы через одну. При этом порядок
их следования в оригинальных плейлистах должен быть сохранен. Первой должна
звучать песня российского исполнителя.

Формат ввода
В первой строке записано число n - длина обоих плейлистов. Оно не превосходит
1000. В следующей строке записаны id российских рок композиций. Их n штук.
В последней строке - id зарубежных композиций. Их также n штук. Каждое из чисел
в двух последних строках не превосходит 1000.

Формат вывода
Выведите в строку через пробел id получившегося плейлиста.

Пример 1
Ввод
3
1 2 3
4 5 6

Вывод
1 4 2 5 3 6

Пример 2
Ввод
1
1
2

Вывод
1 2
"""

number: int = int(input())

if number:
    rus_songs: list = input().split()
    eng_songs: list = input().split()

    result: list = []

    for item in range(number):
        result.append(rus_songs[item])
        result.append(eng_songs[item])

    print(" ".join(result))
