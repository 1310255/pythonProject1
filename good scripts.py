# 1  Извлечение домена из URL
from urllib.parse import urlparse

domain = urlparse('http://www.google.com').netloc
print(domain)


# 2 Разбить список на фрагменты и разделить его на меньшие части
def chunks(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(chunks(l, 3))

# 3 file.writelines() записывает последовательность (список) строк в файл file.
text = [
    "This is line 1\n",
    "This is line 2\n",
    "This is line 3\n", ]
fp = open("test.txt", "w")
fp.writelines(text)
fp.close()

#4 Изменить имя файла
import os
os.rename('old_name.txt', 'new_name.txt')