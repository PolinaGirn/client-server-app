# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
# байтовового в строковый тип на кириллице.

from chardet import detect  # не получилось сделать с locale((((
import subprocess
import platform

param = '-n' if platform.system().lower() == 'windows' else '-c'
args = ['ping', param, '2', 'yandex.ru']
process = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in process.stdout:
    result = detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'), end='')

print('\n--------------------------------------------------------------------------')

param = '-n' if platform.system().lower() == 'windows' else '-c'
args = ['ping', param, '2', 'youtube.com']
process = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in process.stdout:
    result = detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'), end='')

