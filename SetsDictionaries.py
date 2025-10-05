#_____________________________ТЕОРИЯ____________________________

# vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
# for letter in vowels:
#     print(letter)

# Ex.:
# a = set()
# for _ in range(3):
#     string = str(input())
#     a.add(string)
# print(a)    
    
    
# Объединяет два множества — результат содержит все элементы из обоих.
# Повторы исключаются. Оператор: | или метод union().
# ~~~~~~~
# Возвращает только те элементы, которые есть в обоих множествах.
# Оператор: & или метод intersection().
# ~~~~~~~
# Возвращает элементы из первого множества, которых нет во втором. 
# Оператор: - или метод difference().
# ~~~~~~~
# Возвращает элементы, которые есть только в одном из двух множеств (в первом или втором, но не в обоих). 
# Оператор: ^ или метод symmetric_difference().

# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_union = s_1 | s_2
# # s_union = s_1.union(s_2)
# print(s_union)

# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_intersection = s_1 & s_2
# # s_intersection = s_1.intersection(s_2)
# print(list(s_intersection)[0])

# ____________________METHODS OF SET________________________
# set.add(e) - Добавить элемент во множество
# set.remove(e) - Удалить элемент множества. Возвращает исключение KeyError, если элемент не принадлежит множеству
# set.discard(e) - Удалить элемент, если он принадлежит множеству
# set.pop() - Вернуть и удалить произвольный элемент множества
# set.clear() - Очистить множество, удалив все его элементы
# __________________________________________________________



# a = set("Аббориген")
# a.update('qweqweqweqweqwe')
# print(a)






# _________________DICTIONARIES__________________

# countries_and_capitals = {"Россия": "Москва",
# "США": "Вашингтон",
# "Франция": "Париж"}                             # Франция is key 
# print(countries_and_capitals["Франция"]) 


# countries_and_capitals = {"Россия": "Москва",
#                           "США": "Вашингтон",
#                           "Франция": "Париж"}
# countries_and_capitals["Сербия"] = "Белград"              # changing the values of France
# countries_and_capitals["Франция"] = "Липецк"              # .values() - returns values only
# print("\n".join(countries_and_capitals.values()))         # .keys() - returns keys only
                                                            # .items() - returns both 
# countries_and_capitals = {"Россия": "Москва",
#                           "США": "Вашингтон",
#                           "Франция": "Париж",
#                           "Бельгия": "Сербия"}
# if "Сербия" in countries_and_capitals.values():
#     print(1)
# else:
#     print("Страна пока не добавлена в словарь")   
                                                     
                                                    

# countries_and_capitals = {"Россия": "Москва",
# "США": "Вашингтон",
# "Франция": "Париж"}
# for country, capital in countries_and_capitals.items():
#     print(f"У страны {country} столица — {capital}.")
    
    # items() - это метод словарей в Python (узнать, почему это метод, а не функция можно из этого урока курса "Основы Python"). 
    # Он возвращает итерируемый объект (особый DictView объект), позволяющий получить пары "ключ-значение" словаря.

# slovar = {1: 'Apple',
#           2: 'Orange',
#           3: 'Juice'}
# another = {12: 'Coke',
#            5: 'Mom'}
# slovar.update(another)
# print("I LOVE:", ", I LOVE: ".join(slovar.values()))



# countries = dict()
# str_number = 0

# while (country := input()) != "СТОП":

#     if country not in countries:
#         countries[country] = [str_number]
#     else:
#         countries[country].append(str_number)

#     str_number += 1
    
# for country, num in countries.items():
#     print(f"{country}: {num}")

# The same implementation but with '.get()'
# countries = dict()
# str_number = 0
# while (country := input()) != "СТОП":
#     countries[country] = countries.get(country, []) + [str_number]
#     str_number += 1
        
# for country, capital in countries.items():
#     print(f"{country}: {capital}")



# d = {"a": 1, "b": 2, "c": 3}
# print(d.get("b", "Ключа нет в словаре"))



# _______________________МЕТОДЫ СЛОВАРЯ____________________________

# .len(d) - Возвращает количество ключей в словаре
# .del d[key] - Удалить ключ из словаря. Если ключа нет, то вызывается исключение KeyError
# .clear() - Удалить все ключи и значения в словаре
# .get(key, default) - Возвращает значение по ключу key. Если ключа нет, то возвращает значение default
# .items() - Возвращает итерируемый объект, состоящий из кортежей (ключ, значение) словаря
# .keys() - Возвращает итерируемый объект, состоящий из ключей словаря
# .pop(key, default) - Возвращает значение по ключу key и удаляет его из словаря. Если ключа нет, то возвращает default
# .values() - Возвращает итерируемый объект, состоящий из значений словаря

# __________________________________________________________________





# __________________________________PRACTICE________________________________________________

# _A_

# stroka = set(input())
# print(''.join(stroka))

# ~~~~АЛЬТЕРНАТИВA~~~~

# stroka = set(input())
# print(*stroka, sep='')      # *stroka - set unpacking 'з', 'e', 'д', 'м'


# ____________________________


# _B_

# set_1 = set(input())
# set_2 = set(input())
# print(*(result := set_1 & set_2), sep='')

# ~~~~АЛЬТЕРНАТИВA~~~~

# set_1 = set(input())
# set_2 = set(input())
# print(*(result := set_1.intersection(set_2)), sep='')


# ______________________________


# _C_

# N = int(input())
# result = set()
# for _ in range(N):
#     string = str(input())
#     for every in string.split():
#         result.add(every)
#     result |= result
# print(*result, sep='\n')



# _D_


# mannaya = int(input())
# ovsyanaya = int(input())
# result_1 = set()
# result_2 = set()

# for _ in range(mannaya):
#     man = str(input())
#     result_1.add(man)
# for _ in range(ovsyanaya):
#     man = str(input())
#     result_2.add(man)

# l = len(result_1&result_2)
# print(l if l > 0 else "Таких нет")





# _E_

# mannaya = int(input())
# ovsyanaya = int(input())
# sum = mannaya + ovsyanaya
# result_1 = set()
# result_2 = set()

# for _ in range(mannaya):
#     man = str(input())
#     result_1.add(man)
# for _ in range(ovsyanaya):
#     man = str(input())
#     result_2.add(man)





# _G_

# text = input().split()
# st = '1asdasd'

# dictionary = {
#     'A': '.-', 'B': '-...', 'C': '-.-.',
#     'D': '-..', 'E': '.', 'F': '..-.',
#     'G': '--.', 'H': '....', 'I': '..',
#     'J': '.---', 'K': '-.-', 'L': '.-..',
#     'M': '--', 'N': '-.', 'O': '---',
#     'P': '.--.', 'Q': '--.-', 'R': '.-.',
#     'S': '...', 'T': '-', 'U': '..-',
#     'V': '...-', 'W': '.--', 'X': '-..-',
#     'Y': '-.--', 'Z': '--..',
#     '0': '-----', '1': '.----', '2': '..---',
#     '3': '...--', '4': '....-', '5': '.....',
#     '6': '-....', '7': '--...', '8': '---..',
#     '9': '----.'
# }

# for word in text:
#     word = word.upper()
#     for letter in word:
#         print(dictionary[letter], end=' ')
#     print()



# _H_

# N = int(input())
# dictionary = dict()
# names = list()
# foods = []
# for _ in range(N):
#     name, *food = input().lower().split()
#     names.append(name)
#     foods.append(food)
    
# target_kasha = input().lower()



# kasha = input().lower()
# for name, kasha_type in dictionary.items():  
#     if kasha_type == kasha:
#         names.append(name)
# names.sort()
# print('Таких нет' if len(names) == 0 else '\n'.join(names))
    
#kasha = input()






# N = int(input())
# dictionary = dict()
# names = list()
# for _ in range(N):
#     name, *food = input().split()
#     dictionary[name] = food

# target_food = input().lower()
# for every in dictionary:
#     if target_food in dictionary[every]:
#         names.append(every)
# names.sort()
# print('Таких нет' if len(names) == 0 else '\n'.join(names))



# _I_

# dictionary = {}
# counter = 1

# while len((lst_of_words := input().split())) != 0:
#     print(lst_of_words)
#     for every in lst_of_words:
#         if every not in dictionary:
#             dictionary[every] = counter
#         else:
#             dictionary[every] += 1
# for key, value in dictionary.items():
#         print(key, value)




# translit_dict = {
#     'А': 'A',    'Б': 'B',    'В': 'V',
#     'Г': 'G',    'Д': 'D',    'Е': 'E',
#     'Ё': 'E',    'Ж': 'Zh',   'З': 'Z',
#     'И': 'I',    'Й': 'I',    'К': 'K',
#     'Л': 'L',    'М': 'M',    'Н': 'N',
#     'О': 'O',    'П': 'P',    'Р': 'R',
#     'С': 'S',    'Т': 'T',    'У': 'U',
#     'Ф': 'F',    'Х': 'Kh',   'Ц': 'Tc',
#     'Ч': 'Ch',   'Ш': 'Sh',   'Щ': 'Shch',
#     'Ы': 'Y',    'Э': 'E',    'Ю': 'Iu',
#     'Я': 'Ia',   'а': 'a',    'б': 'b',
#     'в': 'v',    'г': 'g',    'д': 'd',
#     'е': 'e',    'ё': 'e',    'ж': 'zh',
#     'з': 'z',    'и': 'i',    'й': 'i',
#     'к': 'k',    'л': 'l',    'м': 'm',
#     'н': 'n',    'о': 'o',    'п': 'p',
#     'р': 'r',    'с': 's',    'т': 't',
#     'у': 'u',    'ф': 'f',    'х': 'kh',
#     'ц': 'tc',   'ч': 'ch',   'ш': 'sh',
#     'щ': 'shch', 'ы': 'y',    'э': 'e',
#     'ю': 'iu',   'я': 'ia'
# }

# string = input()

# for every in string:
#     if every in translit_dict:
#         print(translit_dict[every], end='')
#     elif every.lower() == 'ъ' or every.lower() == 'ь':
#         continue
#     else:
#         print(every, end='')



# _L_

# dictionary = {}
# counter = 1
# N = int(input())
# namesakes = 0

# for _ in range(N):
#     name = input()
#     if name not in dictionary:
#         dictionary[name] = counter
#     else:
#         dictionary[name] += 1
# for every_value in dictionary.values():
#     if every_value > 1:
#         namesakes += every_value
# print(namesakes)


# _L_

# _______ КЛЁВЫЙ ВАРИАНТ______
# dictionary = {}
# counter = 1
# key_stack = []
# for _ in range(N := int(input())):
#     name = input()
#     dictionary[name] = dictionary.get(name, 0) + 1
# items = dictionary.items()
# new_dictionary = dict(sorted_items := sorted(items))

# flag = True
# for key, value in new_dictionary.items():
#     if value > 1:
#         print(f'{key} - {value}')
#         flag = False
# if flag:
#     print("Однофамильцев нет")
# # print(items)
# # print(sorted_items)

# _______МОЕ ИСХОДНОЕ РЕШЕНИЕ________
# for key in dictionary.keys():
#     key_stack.append(key)
# key_stack.sort()
# flag = True
# for every in key_stack:
#     if dictionary[every] > 1:
#         print(f'{every} - {dictionary[every]}')
#         flag = False
# if flag:
#     print("Однофамильцев нет")
    

# flag = True
# for key, value in dictionary.keys():
#     if value > 1:
#         print(f'{key} - {value}')
#         flag = False
# if flag:
#     print("Однофамильцев нет")
# print(dictionary)



# _M_

# N = int(input())    # которые можно приготовить в столовой
# old_dishes = set()
# dishes_to_cook = set()

# for _ in range(N):
#     dishes_to_cook.add(names := input())

# M = int(input())    # имеется информация    
# for _ in range(M):
#     block_num = int(input())
#     for _ in range(block_num): 
#         old_dishes.add(names := input())
# sorted_dishes = sorted(dishes_to_cook - old_dishes)

# if len(sorted_dishes) == 0:
#     print("Готовить нечего")
# else:
#     for every in sorted_dishes:
#         print(every)



N = int(input())    # которые можно приготовить в столовой
products = set()
dictionary = dict()

for _ in range(N):
    products.add(names := input())
  
           # Число рецептов, о которых имеется информация.
for _ in range(M := int(input()) ):
    dish = str(input())
    for _ in range(num_of_ingr := int(input())):
        ingredient = input()
        dictionary[dish]
    
print(dictionary)

        
