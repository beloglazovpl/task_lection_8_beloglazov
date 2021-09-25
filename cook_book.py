from pprint import pprint


def get_cook_book(file_name):
    cook_book = dict()
    with open(file_name) as file:
        for line in file:
            dish = line.strip()
            counter = int(file.readline())

            temp_list = []
            for item in range(counter):
                ingredient_name, quantity, measure = file.readline().split(' | ')
                temp_list.append(
                    {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()}
                )
            cook_book[dish] = temp_list
            file.readline()
    return cook_book


pprint(get_cook_book('recipes.txt'))


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = dict()
    for dish in dishes:
        for k, v in get_cook_book('recipes.txt').items():
            if k == dish:
                for a in v:
                    indgredient_name, quantity, measure = a.values()
                    temp_dict = {'measure': measure, 'quantity': quantity * person_count}
                    if indgredient_name in shop_list.keys():
                        temp_dict['quantity'] = shop_list[indgredient_name]['quantity'] + (quantity * person_count)
                    else:
                        temp_dict['quantity'] = quantity * person_count
                    shop_list[indgredient_name] = temp_dict
    return shop_list


pprint(get_shop_list_by_dishes(['Борщ', 'Запеченный картофель', 'Утка по-пекински'], 3))
