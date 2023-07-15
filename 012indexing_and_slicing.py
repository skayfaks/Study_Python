
greeting_length = len(greeting)
print(len(greeting))
print(greeting_length)
 
# Indexing
print(greeting[0])
print(greeting[6])
print(greeting[-1]) # первый элемент с конца - ! знак
print(greeting[12]) # тот же знак 
 
greeting = 'Hello Python!'
# Slicing
print(greeting[2:5]) # символ с последним индексом не включается
#llo
print(greeting[1:7])
#ello P
print(greeting[-4:-1]) # элименты с конца ( отсчет с 1)
#hon
print(greeting[7:]) # с 7ого символа до  конца
#ython!
print(greeting[:4]) # c начала до 4 не вкл-я его
#Hell
print(greeting[:]) # вырезается вся строка
print(greeting[::2]) # шаг с которым будет слайсится вся строка
#HloPto!
print(greeting[1::3]) # слайсим 3й символ с первого символа (как бы делаем сдвиг)
#eoyo
print(greeting[1:9:3])
#eoy
print(greeting[::-1]) # выстраиваем элементы в обратном порядке
#!nohtyP olleH