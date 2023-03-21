'''
Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
 Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей, кроме одного, и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами.
Код должен расширяться на любое большее количество друзей.
'''
names = ['George', 'Sam', 'Frodo']
backpacks = [('sleeping bag', 'food', 'clothes', 'tent', 'first aid kit', 'axe', 'towel'),
             ('sleeping bag', 'food', 'clothes', 'camera', 'kitchenware', 'towel'),
             ('sleeping bag', 'food', 'clothes', 'shoes', 'axe', 'camera')]

#friends = zip(names, backpacks)
friends_dict = {}
for i in range(len(names)):
    friends_dict[names[i]] = set(backpacks[i])

#Какие вещи взяли все три друга
common = set(backpacks[0])
for backpack in friends_dict.values():
    common &= backpack 
print(f'All friends have these things in common: {common}')

all_things = set(backpacks[0])
for friend, backpack in friends_dict.items():
    all_things |= backpack 
print(f'All things our friends have in their backpacks: {all_things}')

# Какие вещи уникальны, есть только у одного друга
unique = all_things.copy()
for friend, backpack in friends_dict.items():
    for other_friend, other_backpack in friends_dict.items():
        if other_friend != friend:
            unique -= other_backpack
    print(f'Just {friend} has {unique}')
    unique = all_things.copy()

# Какие вещи есть у всех друзей, кроме одного, и имя того, у кого данная вещь отсутствует

#Для Джорджа это камера
#print(set(backpacks[1]) & set(backpacks[2]) - common)
#print(set(backpacks[0]) & set(backpacks[2]) - set(backpacks[1]))
#print(set(backpacks[1]) & set(backpacks[0]) - set(backpacks[2]))


for i in range(len(names)):
    unique_two = set(backpacks[i - 1])
    for j in range(len(names)):
        if j != i:
            unique_two &= set(backpacks[j])
    unique_two -= set(backpacks[i])
    print(f'Just {friend} has no {unique_two}')
    





