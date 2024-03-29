"""
Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.
Шаги:
1. Создай класс Store: -Атрибуты класса: name: название магазина. address: адрес магазина.
items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
Методы класса:
__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems`.
-  метод для добавления товара в ассортимент. метод для удаления товара из ассортимента. метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
метод для обновления цены товара.
2. Создай несколько объектов класса Store:
Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
3. Протестировать методы:
Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.
В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания.
"""

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Пустой словарь для товаров

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

# Создание магазинов
store1 = Store("М-Видео", "Цветной бульвар, 25")
store2 = Store("Глобус", "Болотная, 13")
store3 = Store("Бершка", "Зеленая, 17")

# Добавление товаров в магазины
store1.add_item("ТВ", 27000)
store1.add_item("Ноутбук", 51000)
store2.add_item("Яблоки", 160)
store2.add_item("Молоко", 92)
store3.add_item("Джинсы", 3500)
store3.add_item("Рубашка", 2100)

# Тестирование на примере store1
print("Цена ТВ до обновления:", store1.get_price("ТВ"))
store1.update_price("ТВ", 32000)
print("Цена TV после обновления:", store1.get_price("ТВ"))

store1.add_item("Смартфон", 15400)
print("Цена Headphones:", store1.get_price("Смартфон"))

store1.remove_item("Ноутбук")
print("Цена Ноутбука после удаления:", store1.get_price("Ноутбук"))
