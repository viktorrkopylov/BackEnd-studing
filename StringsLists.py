# ______________________ТЕОРИЯ__________________________

# text = input("Введите строку: ")

# for i in range(len(text)):
#     print(text[i], end='')

# for nigga in text:
#     print(nigga)

# for index, letter in enumerate(text):
#     print(f"{index}. {letter}")


# print(text[0:100:2], end="")      СРЕЗ
# print(text[:5])         # первые 5 элементов
# print(text[::3])        # каждый третий элемент
# print(text[::-2])       # строка в обратном порядке
# print(text[:])
# print(text[8::])        # с 8-ого (включительно) до конца

# print(text.islower())   # True - если все значения строки нижнего регистра



# ___________ЧАСТОИСПОЛЬЗУЕМЫЕ МЕТОДЫ СТРОКИ____________
# a = text.capitalize()   # делает первый символ заглавным, ост. - строчными
# b = text.count('lo')    # в 'Hello, my love' вывод: 2
# c = text.endswith("ga") # True, если строка заканчивается на 'ga'
# d = text.find('r')      # возвращает индекс первого вхождения 'g' в строке, иначе -1
# # e = text.index('t')     # как и find, но при ненахождении возвращает 'ValueError'
# f = text.isalnum()      # Возвращает True, если все символы строки являются буквами и цифрами и в строке есть хотя бы один символ. Иначе возвращает False
# g = text.isalpha()      # Возвращает True, если все символы строки являются буквами и в строке есть хотя бы один символ. Иначе возвращает False
# h = text.isdigit()      # Возвращает True, если все символы строки являются цифрами и в строке есть хотя бы один символ. Иначе возвращает False
# j = text.islower()      # Возвращает True, если все буквенные символы строки написаны строчными буквами. Иначе возвращает False
# k = text.isupper()      # Возвращает True, если все буквы в строке большие и в строке есть хотя бы одна буква. Иначе возвращает False

# ab = ['1', '2', '3']
# zi = ';'.join(ab)       # join используется для объединения элементов итерируемого объекта (например, списка) в одну строку, разделяя их указанным разделителем

# l = text.ljust(6, '-')  # выравнивает text по левому краю (добавляет т количество '-' до ширины 10)
# m = text.rjust(6, '-')  # ^ как и ljust, но выравнивает по правому краю
# n = text.lower()        # все буквы приводит к нижнему регистру
# o = text.lstrip('ACb')  # удаляет все символы аргумента СЛЕВА до первого отличного символа, далее в строке могут встречаться символы из аргумента (не удаленные)
# p = text.rstrip('ACb')  # ^ справа
# q = text.split(', ')     # выводит СПИСОК строк, разделенных по ',' Введите строку: Девочки, обычно, сосут, мальчикам. ВЫВОД: ['Девочки', ' обычно', ' сосут', ' мальчикам.']
# r = text.startswith('Nig')  # Проверяет начало строки на 'Nig'
# s = text.strip(" aBc")    # возвращает строку с удаленными в ней символами, встрещающимися в chars
# t = text.title()        # Возвращает строку, в которой каждое отдельное слово начинается с буквы в верхнем регистре, а остальные буквы идут в нижнем
# u = text.upper()        # все буквы делает заглавными
# print(s)

# ------------------CПИСКИ--------------------
# csc = ["apple", "banana", "cherry", "date"]
# csc.sort(key=csc[])
# print(csc)
# numbers = [10, 20, 30, 40, 50]
# print(numbers[0])
# print(numbers[-1])
# print(numbers[1:3])
# print(numbers[::-1])

# def gay():
#     del numbers[::-2]
#     print(numbers)
# gay()
# csc = [1, 2, 3, 4, 6, 7, 8, 9, 0]
# csc.insert(4, 5)
# print(csc)

# s = [2, 3, 1]
# new_s = sorted(s, reverse=True)
# print(new_s)









# __________________________ПРАКТИКА__________________________________


# _A_

# N = int(input())
# counter = 0
# for _ in range(N):
#     name = input()
#     if name[0] in 'авб':
#         counter += 1
# print("YES" if counter == N else "NO")





# _B_

# stroka = input()

# for i in range(len(stroka)):
#     print(stroka[i])

# ЛУЧШАЯ АЛЬТЕРНАТИВА
# for letter in stroka:
#     print(letter)





# _C_

# L = int(input())
# N = int(input())
# for _ in range(N):
#     string = input()
#     if len(string) <= L:
#         print(string)
#     else:
#         print(f"{string[:L - 3]}", end='...\n')
        
        

# _D_

# while (string := input()) != '':
#     a = ''
#     if string.endswith('#') and string.startswith('@@@'):
#         print(string)
#     elif string.endswith('@@@'):
#         continue
#     elif string.startswith('#'):
#         a = string.lstrip('###')
#         print(a)
#     else:
#         print(string)




# _E_

# string = input()
# if string == string[::-1]:
#     print("YES")
# else:
#     print("NO")        



# _F_

# N = int(input())
# counter = 0
# for i in range(N):
#     stroka = input()
#     counter += stroka.count('зайка')
# print(counter)





# _G_

# first, second = input().split()
# print(float(first) + float(second))





# _H_

# N = int(input())

# for i in range(1, N + 1):
#     stroka = input()
#     a = stroka.find("зайка") + 1
#     if a == 0:
#         print("Заек нет =(")
#     else:
#         print(a)




# _I_

# while (stroka := input()) != '':
#     comment = stroka.find('#')
#     if comment == -1:
#         print(stroka)
#     elif stroka.startswith('#'):
#         continue
#     else:
#         a = stroka[:comment:]
#         print(a)





# _J_
# letters = []
# counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# indices = []
# while (stroka := input()) != 'ФИНИШ':
#     stroka = stroka.lower().strip()
#     for letter in stroka:
#         if (index := letters.index(letter)) != -1:
#             counts[index] += 1
#         else:
#             letters.append(letter)
#             counts.append(1)
# print(max(counts))            
            
            
# indices = []
# while (stroka := input()) != 'ФИНИШ':
#     for letter in stroka:
#         stroka.find(letter)
#         indices.append(letter)






# _K_


# N = int(input())
# lst = []

# for i in range(N):
#     title = input()
#     lst.append(title)   

# request = input().lower()
# for string in lst:
#     if request in string.lower():
#         print(string)
#     else:
#         continue





# _L_

# menu = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
# N = int(input())
# j = 0

# for _ in range(N):
#     if j == len(menu):
#         j = 0
#     print(menu[j])
#     j += 1




# _M_

# N = int(input())
# lst = []

# for i in range(N):
#     num = int(input())
#     lst.append(num)

# power = int(input())
# for n in lst:
#     print(n**power)





# _N_

# N = input().split()
# power = int(input())

# for each in N:
#     print(int(each) ** power, end=" ")




# _O_

# nums = input().split()






# _P_               ОНА  МЕНЯ  ЗАЕБАЛА !!!!!!!!!

# L = int(input())
# N = int(input())
# lst = []

# for _ in range(N):
#     title = input()
#     lst.append(title)

# for each in lst:
#     if L >= len(each) + 3:
#         print(each)
#         L -= len(each)
#     elif len(each) <= L:
#         print(each)
#     elif L == len(each) + 3:
#         print(each[:L - 3] + '...')
#         break
#     elif L == len(each):
#         print(each)
#     elif 0 < len(each) - L < 3:
#         rem = len(each) - L
#         print(each[:L - 3 - rem] + '...')
#     else:
#         print(each[:L - 3] + '...')
#         break



# _Q_

# string = input()
# changed = string.lower().replace(" ", "")
# if changed == changed[::-1]:
#     print("YES")
# else:
#     print("NO")
    



# _R_

# string = input()
# ref = string[0]
# string = string[1::] + '_'
# counter = 1
# for number in string:
#     if ref == number:
#         counter += 1
#     else:
#         print(ref, counter)
#         ref = number
#         counter = 1



# _S_

# ___________________________________My Try______________________________
# string = input().split()
# operations = ['-', '+', '*', '/']
# ref1 = string[0]
# ref2 = string[1]
# result = 0

# for every in string:
#     if every.isdigit():
#         ref1 = ref2
#         ref2 = every
#     else:
#         operation = every 
#         match operation:
#             case '-':
#                 result = int(ref1) - int(ref2)
#             case '*':
#                 result = int(ref1) * int(ref2)
#             case '+':
#                 result = int(ref1) + int(ref2)
#             case '/':
#                 if int(ref2) == 0:
#                     raise ValueError("Деление на ноль")
#                 result = int(ref1) / int(ref2)
#         string.insert(string.index(ref1), str(result))
#         string.remove(operation)
#         string.remove(ref1)
#         string.remove(ref2)

# ref1 = string[0]
# ref2 = string[1]
# for every in string:
#     if every in operations:
#         match every:
#             case '-':
#                 result = int(ref1) - int(ref2)
#             case '*':
#                 result = int(ref1) * int(ref2)
#             case '+':
#                 result = int(ref1) + int(ref2)
#             case '/':
#                 if int(ref2) == 0:
#                     raise ValueError("Деление на ноль")
#                 result = int(ref1) / int(ref2)
#         string.insert(string.index(ref1), str(result))
#         string.remove(every)
#         string.remove(ref1)
#         string.remove(ref2)
# print(string[0])

    
                            
# _______________________________Correct Way___________________________

# string = input().split()
# operations = {'-', '+', '*', '/'}
# stack = []

# for every in string:
#     if every not in operations:
#         stack.append(int(every))
        
#     else:
#         # if len(stack) < 2:
#         #     raise ValueError("Недостаточно операндов")
        
#         b = stack.pop()
#         a = stack.pop()

#         match every:
#             case '+':
#                 result = a + b
#             case '-':
#                 result = a - b
#             case '*':
#                 result = a * b
#             case '/':
#                 # if b == 0:
#                 #     raise ValueError("Деление на ноль")
#                 result = a / b
        
#         stack.append(result)

# # В стеке должен остаться только один элемент - результат
# # if len(stack) != 1:
# #     raise ValueError("Некорректное выражение")

# print(stack[0])                    
            
            
            
            
            
            
            
            
string = input().split()
operations = {'-', '+', '*', '/', '~', '!', '#', '@'}
stack = []

for every in string:
    if every not in operations:
        stack.append(int(every))
        
    else:
        match every:
            case '@':
                if len(stack) < 3:
                    raise ValueError("В стеке меньше 3 элементов")
                stack[-3], stack[-2], stack[-1] = stack[-2], stack[-1], stack[-3]
            case '#':
                stack.append(stack[-1])
            case '!':
                b = stack.pop()
                if b < 0:
                    raise ValueError("b <= 0")
                elif not isinstance(b, int):
                    raise ValueError("Число не целое")
                else:
                    result = 1
                    for i in range(1, b + 1):
                        result *= i
                    stack.append(result)
            case '~':
                b = stack.pop()
                result = -b
                stack.append(result)
            case _:
                if len(stack) < 2:
                        raise ValueError("В стеке меньше 2 элементов")
                b = stack.pop()
                a = stack.pop()
                
                match every:
                    case '+':
                        result = a + b
                        stack.append(result)
                    case '-':
                        result = a - b
                        stack.append(result)
                    case '*':
                        result = a * b
                        stack.append(result)
                    case '/':
                        if b == 0:
                            raise ValueError("Деление на 0")
                        stack.append(result := a/b)                        
print(stack[0])

#____EDITION



#____EDITION 2nd
        
    