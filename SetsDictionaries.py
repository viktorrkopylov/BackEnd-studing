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

N = int(input())
dictionary = dict()
names = list()
for _ in range(N):
    name_kasha = input().split()
    dictionary[name_kasha[0]] = name_kasha[1]

kasha = input().lower()
for name, kasha_type in dictionary.items():  
    if kasha_type == kasha:
        names.append(name)
names.sort()
print('Таких нет' if len(names) == 0 else '\n'.join(names))
    
#kasha = input()
