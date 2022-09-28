# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
# программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое

from chardet import detect

lines = ['сетевое программирование', 'сокет', 'декоратор']

f = open('test_file.txt', 'w', encoding='utf-8')
for i in lines:
    f.write(str(i) + '\n')
f.close()

with open('test_file.txt', 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']
print('\nкодировка: ', encoding, '\n')

# не совсем поняла что значит "Принудительно открыть файл в формате Unicode"
with open('test_file.txt', encoding=encoding) as file:
    for line in file:
        print(line, end='')
