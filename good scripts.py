# %% 1  Извлечение домена из URL
from urllib.parse import urlparse

domain = urlparse('http://www.google.com').netloc
print(domain)


# %% 2 Разбить список на фрагменты и разделить его на меньшие части
def chunks(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(chunks(l, 3))

# %% 3 file.writelines() записывает последовательность (список) строк в файл file.
text = [
    "This is line 1\n",
    "This is line 2\n",
    "This is line 3\n", ]
fp = open("test.txt", "w")
fp.writelines(text)
fp.close()

# %% 4 Изменить имя файла
import os

os.rename('old_name.txt', 'new_name.txt')

# %% 5 Генераторы словарей и мнжеств
x = {i: i ** 2 for i in range(10)}
d = {i: i ** 2 for i in range(10) if i % 2 == 0}
print(x)
print(d)

# %% 6 Объединение списков в один
lst = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
print([i for j in lst for i in j])
print(sum(lst, []))

# %% 7 Функция filter() для создания списка,состоящего из значений,для которых функция возвращает True
num = [1, 2.0, 3.1, 4, 5, 8.9, 4]
f = filter(lambda x: x > 4, num)  # сравнение  x>4
print(list(f))
f = filter(lambda x: type(x) is int, num)  # идентичность с целыми цислами
print(list(f))

# %% 8 Обмен ключей и значений словаря
a = {1:11, 2:22, 3:33}
b = dict(zip(a.values(), a.keys()))
print(b)

# %% 9 Воспроизведение звука
import os
f="test.mp3"
os.system(f)

# %% 10 Открытие веб-страницы
import webbrowser
webbrowser.open('https://www.google.com')

# %% 11 shorten() модуля textwrap усекает заданный текст,
# чтобы он поместился в заданную ширину width

import textwrap
textwrap.shorten("Hello world", width=10)
textwrap.shorten("Hello world", width=11)
textwrap.shorten("Hello world", width=12)
textwrap.shorten("Hello world", width=13, placeholder="...")

# %% 12 Query JSON
import jmespath
persons={
    "persons": [
        {"name": "John", "age": 20},
        {"name": "Jane", "age": 30},
        {"name": "Jack", "age": 40},
    ]
}
jmespath.search('persons[*].name', persons)
# %% 13 Проверка наличия ключа в словаре