'''
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
'''

list_ = [1, 2, 2, 3, 3, 3, 5]
duplicates_list = []
for item in set(list_):
    if item not in duplicates_list and list_.count(item) > 1:
        duplicates_list.append(item)
print(duplicates_list)