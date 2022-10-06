# Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров —
# товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
# Функция должна предусматривать запись данных в виде словаря в файл orders.json.
# При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import json
from typing import TextIO


def write_order_to_json(item, quantity, price, buyer, date):

    with open('orders.json', 'r', encoding='utf-8') as file_out:
        data = json.load(file_out)

    # тут подчеркивал f_in, поэтому переименовала
    with open('orders.json', 'w', encoding='utf-8', ) as file_in:
        orders_list = data['orders']
        order_info = {'item': item, 'quantity': quantity,
                      'price': price, 'buyer': buyer, 'date': date}
        orders_list.append(order_info)
        json.dump(data, file_in, indent=4, ensure_ascii=False)


with open('orders.json', 'w', encoding='utf-8') as f_in:
    json.dump({'orders': []}, f_in, indent=4)

write_order_to_json('гитара', '1', '15000', 'Шипилов А.А.', '06.10.2013')
write_order_to_json('пипитер', '10', '500', 'Литвинова И.Г.', '20.09.2016')
write_order_to_json('медиатор', '30', '30', 'Гирн А.В.', '31.01.2020')
write_order_to_json('фортепиано', '2', '50000', 'Криворуков Е.Т.', '14.02.2018')
write_order_to_json('скрипка', '1', '30000', 'Шипилова П.А', '28.02.2022')
write_order_to_json('струны', '3', '300', 'Шипилов А.А.', '09.09.2021')


