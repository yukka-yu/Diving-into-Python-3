'''
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите, какие вещи влезут в рюкзак, передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
'''

CAPACITY = 15

equipment_dict = {'sleeping bag': 1.5, 'tent': 4, 'mat': 1, 'clothes': 3, 'shoes': 2, 'first aid kit': 1, 'kitchenware': 2, 'axe': 1}
backpack_list = []
for thing, weight in equipment_dict.items():
    if CAPACITY - weight >= 0:
        backpack_list.append(thing)
        CAPACITY -= weight
print(backpack_list)


