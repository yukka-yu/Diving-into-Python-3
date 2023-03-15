'''
Создайте вручную кортеж содержащий элементы разных типов.
Получите из него словарь списков, где ключ - тип элемента, значение - список элементов данного типа.  
'''

'''Создайте вручную список с повторяющимися элементами. Удалите из него все элементы, которые встречаются дважды. '''

'''Создайте вручную список с повторяющимися целыми числами. Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
Нумерация начинается с единицы. '''

'''Пользователь вводит строку текста. Вывести каждое слово с новой строки. Строки нумеруются начиная с единицы Слова выводятся отсортированными
согласно кодировки Unicode Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки '''


'''
my_tuple = ("str1", "str2", 23, 14, True, [1, 2, 3], {1, 2, 3}, {3: "fff", 5: "ggg"}, 3.14, 3.489)
my_dict = {}
for entity in my_tuple:
    k = my_dict.setdefault(type(entity), [])
    k.append(entity)
print(my_dict)
'''
'''
#new_list = []
my_list = [1, 1, 1, 2, 2, 3, 4, 4, 7, 7]
for i in set(my_list):
    if my_list.count(i) == 2:
        #new_list.append(i)
        my_list.remove(i)
        my_list.remove(i)
print(my_list)
'''

'''
my_list = [1, 1, 1, 2, 2, 3, 4, 4, 7, 7]
new_list = []
for i, item in enumerate(my_list, start=1):
    if item % 2 != 0:
        new_list.append(i)
print(new_list)
'''
'''
text = "Enter some text abc"

max_len = max(len(w) for w in text.split()) 

for i, item in enumerate(sorted(text.split()), start=1):
    print(f'{i} {item :>{max_len}}')
'''
'''Пользователь вводит строку текста. Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
Результат сохраните в словаре, где ключ - символ, а значение - частота встречи символа в строке. Обратите внимание на порядок ключей.
Объясните почему они совпадают или не совпадают в ваших решениях. '''

text = "Enter some text again"
my_dict = {}
for letter in text:
    if letter not in my_dict:
        my_dict[letter] = 1
    else: 
        my_dict[letter] += 1
print(my_dict)

new_dict = {}
for letter in set(text):
    new_dict[letter] = text.count(letter)
print(new_dict)


