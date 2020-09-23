"""
Евлампия очень любит постить фотографии в инстаграм. Но она боится, что данные с сервера могут пропасть.
Поэтому она приняла решения хранить все изображения также в Трешландских датацентрах в двух экземплярах.

Всего есть N датацентров, в каждом из которых можно разместить fi фотографий, где i = 0..N-1.

Но хранить две копии фотографии в одном датацентре ненадежно. Вдруг с ним что-нибудь случится.
Поэтому так делать нельзя. Нужно определить, какое максимальное число фотографий Евлампия сможет сохранить.

Формат ввода
В первой строке записано n - количество датацентров. Оно не превосходит 10000.

В следующей строке через пробел записаны n чисел - вместимости датацентров в штуках фотографий.
Каждое из чисел не превосходит 10000.

Формат вывода
Нужно вывести число, равное максимальному количеству фотографий, для которых можно хранить копии в этих датацентрах.
"""
i = int(input())
x = list(map(int, input().split()))
max = sum(x) // 2

print(max)