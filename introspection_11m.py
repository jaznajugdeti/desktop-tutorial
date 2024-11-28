# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).

from pprint import pprint

def introspection_info(obj):
    type__ = type(obj).__name__
    attribute = getattr(obj, '__dir__')
    methods = dir(obj)
    module = obj.__class__.__module__
    info = {'type': type__, 'attribute': attribute, 'methods': methods, 'module': module}
    return info
number_info = introspection_info(42)
print(number_info)
pprint(number_info)

from inspect import getmodule
def introspection_info(obj):
    return{
        'type': type(obj),
        'attributes': obj.__dict__,
        'methods': dir(obj),
       # /\ 'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': getmodule(obj)
    }
class Mycalass:
    def __init__(self):
        self.name = 'Myclass'
        self.description = 1
        self.attributes = 50

obj = Mycalass()
number_info = introspection_info(obj)
print(number_info)
