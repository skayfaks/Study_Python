# Некоторые часто используемые функции и операторы
""" for x in range(2,10,3):
    print(x)
print(range(5)) """
#2
#5
#8
#range(0, 5)  - получаем объект типа range

""" for x in range(2,10,3):
    print(x)
print(list(range(5))) """
#2
#5
#8
#[0, 1, 2, 3, 4]  - получаем список всех элементов




# распечатываем индексы элементов какой-то последовательности
""" my_str="asdadf"
letter_index=0   #создаем вспомогательную переменную
for letter in my_str:
    print(letter + ' это индекс ' + str(letter_index))
    letter_index+=1 """

""" 
a это индекс 0
s это индекс 1
d это индекс 2
a это индекс 3
d это индекс 4
f это индекс 5 
"""

# Можно сделать спомощью функции enumerate
""" my_str="asdadf"
for item in enumerate(my_str):
    print(item) """
# получаем вывов типа кортеж, где индекс связан с каждым элементом
""" 
(0, 'a')
(1, 's')
(2, 'd')
(3, 'a')
(4, 'd')
(5, 'f')
"""

#
""" my_str="asdadf"
for index,letter in enumerate(my_str):      # мы можем распокавать кортеж 
    print(letter + ' индекс ' + str(index)) # и сразу из кортежа печатаем первое значение index и второе букву """
"""
a индекс 0
s индекс 1
d индекс 2
a индекс 3
d индекс 4
f индекс 5 
"""



# Ключевое слово In - мы можем проверять, находится ли значение в последовательности
""" print('a' in 'anton') """
#True

""" letter_list=['a','b','c', True]
print('a' in letter_list)
print(True in letter_list)
#True

dict_1={1:'a', 2:'b', 3:'c'}
print(1 in dict_1)
#True - так как по умолчанию мы получаем ключи к словарю
print(1 in dict_1.keys())
#True - в ключах содержится значение 1
print('c' in dict_1.values())
#True  - спомощью ключа values мы можем узнать сод-ся ли в значениях  словаря искомое значение 'c' """




""" # функции MIN и MAX - возвращают минимум и максимум
print(min(1,2,3,4))
#1
print(max(1,2,3,4))
#4

my_list=[1,2,3,4]
print(min(my_list))
#1
print(max(my_list))
#4
print(max ('Hello'))
#o
for letter in 'Hello':
    print(ord(letter)) # узнаем код символа из-за того что у символа о-111 команда max НАМ Его и выдала!! """


# некторые фун-ции из встроеных библиотек

from random import shuffle # импорт функции из библиотеки
my_list=[1,3,56,4]
shuffle(my_list)
print(my_list) # при выводе код всегда перемешивается

from random import randint
print(randint(1,10)) 