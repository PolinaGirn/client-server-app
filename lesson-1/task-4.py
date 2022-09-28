# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
# строкового представления в байтовое и выполнить обратное преобразование (используя
# методы encode и decode).

words_str = ['разработка', 'администрирование', 'protocol', 'standard']
words_bytes = []
words_bytes_str = []


def iteratorNameContent(header, arr):
    print(header)
    for elem in arr:
        print(type(elem), ' - ', elem)
    print()


for i in words_str:
    words_bytes.append(i.encode('utf-8'))

for i in words_bytes:
    words_bytes_str.append(i.decode('utf-8'))

iteratorNameContent('Строки:', words_str)
iteratorNameContent('Преобразование в байты:', words_bytes)
iteratorNameContent('Преобразование обратно в строки:', words_bytes_str)
