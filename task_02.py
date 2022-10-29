# Задача 2
# Создайте список "города" с именами любых городов
# Количество элементов в списке "города" не меньше 3!

cities = ['Москва', 'Санкт-Петербург', 'Тула']

# Создайте список списков населения перечисленных городов

cities_population = [[cities [0], 12635466], [cities [1], 5377503], [cities [2], 461245]]

# Выведите на консоль население второго города в списке в формате
# Население Москвы - ХХ человек

print (f'Население {cities[1]} - {cities_population [1][1]}')


# Выведите на консоль общий размер населения перечисленных городов как сумму населения всех городов
# Итого размер населения - ХХ человек

total_population = cities_population [0][1] + cities_population [1][1] + cities_population [2][1]

print (f'Итого размер населения - {total_population} человек')

# Отлично! Есть ещё решения
# Решение 1 через функцию с циклом for 
def total_sum(lst):
    num_lst = []
    
    for i in lst:
        population = i[1]
        num_lst.append(population)
    
    sum_lst = sum(num_lst)
    
    return sum_lst

population_sum_1 = total_sum(town_population)


# Решение 2 с суммой результатов индексации
population_sum_2 = town_population[0][1] +  town_population[1][1] + town_population[2][1] + town_population[3][1]
