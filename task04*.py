
def find_combinations(equipment, capacity):
    result = []
    equipment_sorted_list = sorted(equipment.items(), key=lambda x: x[1], reverse=True)

    def find_combinations_recursive(current_weight, current_combination, remaining_items):

        # Нашли вариант комплектации рюкзака
        if current_weight <= capacity:
            result.append(current_combination)
            
        # Для каждой оставшейся вещи рекурсивно ищем результаты
        for i in range(len(remaining_items)):
            new_combination = current_combination + [remaining_items[i]]
            new_weight = current_weight + remaining_items[i][1]
            new_remaining = remaining_items[i+1:]
            find_combinations_recursive(new_weight, new_combination, new_remaining)

    find_combinations_recursive(0, [], equipment_sorted_list)
        
    return result


equipment = {'axe': 2, 'sleeping bag': 1.5, 'boots': 2, 'food': 4, 'clothes': 3, 'gadgets': 1.5, 'mat': 0.4, 'tent': 3.9}
capacity = int(input('Введите грузоподъёмность Вашего рюкзака \t'))

result = find_combinations(equipment, capacity)
for equip_list in result:
    print(equip_list)





     














    

