# numbers = [int(input()) for i in range(5)]
# print(numbers)



# numbers = [int(input()) for i in range(5)]
# avg = sum(numbers) // len(numbers)
# numbers = [element for element in numbers if element > avg]
# print(numbers)



# matrix = [[int(x) for x in input().split()] for i in range(5)]
# print(matrix)




# zeros = [[0] * 5 for i in range(5)]
# zeros[0][0] = 1
# print(zeros)


# text = "Строка символов"
# codes = [ord(symbol) for symbol in text]
# print(codes, len(codes) == len(text))



# countries = {
#     "Россия": ["русский"],
#     "Беларусь": ["белорусский", "русский"],
#     "Бельгия": ["немецкий", "французский", "нидерландский"],
#     "Вьетнам": ["вьетнамский"]
# }

# multiple_lang = [country for country, lang in countries.items() if len(lang) > 1]

# print(multiple_lang)


# numbers = (int(input()) for i in range(5))
# print(numbers)


# rere = 54542324
# print()


# x = 5
# print(id(x))
# x = 5/1
# print(id(x))




# a = {1, 2, 3, 4}
# b = [1, 2, 3]
# print(id(a), id(b))

# a.add(5)
# b.append(4)
# print(f"{id(a)} = {a}, {id(b)} = {b}")






# x = [1, 2, 3]
# y = x
# x[0], x[1] = 0, 100
# print(x)
# print(y)




# ______________Чтобы создать отдельный объект, можно использовать срез:______________
# x = [1, 2, 3]
# y = x[:]
# x[0] = 0
# print(x)
# print(y)



# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# numbers_copy = numbers[:]
# print([numbers_copy[i] is numbers[i] for i in range(len(numbers))])
# print([numbers is numbers_copy], end="\n")











# _________________________________________________________________________________

#_A_

# a = int(input())
# b = int(input())
# print(arr := [i**2 for i in range(a, b + 1)])



# _B_

# a = int(input())
# b = int(input())
# arr = [i**2 for i in (range(a, b + 1) if a < b else range(a, b - 1, -1))]
# print(arr)



# _C_

# a = -9
# b = 15
# d = 3
# arr = [i for i in range(a, b + 1) if i % d == 0]
# print(arr)


# _D_

# numbers = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]

# res = {i for i in numbers if i % 2 != 0}
# print(res)





# _E_

# numbers = [1, 2, 3, 4, 5]

# res = {number for number in numbers if number == int(number ** 0.5) ** 2}
# print(res)





# _F_

# sentence = 'Ехали медведи на велосипеде'
# res = [len(every) for every in sentence.split(' ')]
# print(res)



# _G_

# text = '33 коровы,\n' + \
#     '33 коровы,\n' + \
#     '33 коровы -\n' + \
#     'Свежая строка.\n' + \
#     '33 коровы,\n' + \
#     'Стих родился новый,\n' + \
#     'Как стакан парного молока.\n' + \
#     'Стих родился новый,\n' + \
#     'Как стакан парного молока.\n'
    
# print(text)
# text = '2 + 2 = 4'
# res = ''.join(num for num in text if num.isdigit())
# print(res)





# _H_

# string = 'Российская Федерация'

# res = ''.join(letter[0].upper() for letter in string.split())
# print(res)

# arr = string.split()
# for every in arr:
#     print(every[0], end='')







# _I_

# numbers = [1, 1, 3, 1, 10, 2, 4, 6, 7, 1, 2, 7]

# res = ' - '.join(str(every) for every in sorted(set(numbers)))
# print(res)

# print(str(sorted(set(numbers))))

# print(str(numbers))





# _J_

# words = 'Ехали медведи на велосипеде'
# # words = 'My homework is too difficult!'
# res = [word for word in words.split() if sum(1 for letter in word.lower() if letter in "aeiouyаеёиоуыэюя") >= 3]
# print(res)







# _K_

# numbers = [-8, 7, -3, -2, 5, 0, 7, -2, -8, 6, -10, 4, -9, -9, 7]
# res = {every for every in numbers if numbers.count(every) == 1}
# print(res)





# _L_

# numbers = {2, 4, 5, 7, -10, -8, 10, -9, -1}
# res = ''.join(str(max(first * second for first in numbers for second in numbers if first != second)))
# # q = ''.join('')
# print(res)





# _M_

# data = {'a': [100], 'b': [20, 5], 'c': [7, 15, 3]}

# res = str(key for key, value in data.items() if sum(value) == min)
# print(res)

# for key, value in data.items():
#     print(key,value)







# _N_

# data = {'a': [1, 2, 1], 'b': [2, 3, 2, 5, 1]}
# res = {key for key, value in data.items() if len(value) != len(set(value))}
# print(res)





# _O_

# text = 'Мама мыла раму!'
# res = {char: text.lower().count(char) for char in set(text.lower()) if char.isalpha()}
# print(set(text.lower()))




# _P_

# rle = [('1', 1), ('0', 2), ('5', 1), ('0', 2)]
# res = (''.join(i[0] * i[1] for i in rle))
# print(res)





# _Q_

# n = 3
# res = [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
# print(res)






# _R_

