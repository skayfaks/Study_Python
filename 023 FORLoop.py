# https://pythonclass.ru/python/cikl-for-i-funkciya-range-v-python/
# Цикл с известным колличеством повторений
# C помощью него можно обойти все элементы этерируемой последовательности или этер-ого объекта
# Решает задачу - перебрать весь список и извлечь из него необходимые данные.
# Цикл for позволяет перебрать любой итерируемый объект, то есть объект, из которого команда for 
# сможет брать элементы по одному, пока не будет обработан последний элемент, не зависимо от его длины.


# https://www.youtube.com/watch?v=yPUA8xBEyzM
# for <переменная> in <объект>:
#     <Тело цикла>


#                                      ---- Обходим последовательность -------

""" number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
     print(str(number) + ' ПРИВЕТ!')

x=['q','w','e','r','t','y']
for y in x:
     print(y) """


#Числа которые делятся на 2 и на 7 - все 3х значные числа 100 (включено в посл-ть), 1000 (не вкд-но)

""" for i in range(100,1000):
    if i%2==0 and i%7==0:
        print(i) """

# Все квадраты чисел от 1 до 10
""" for v in range(1,11):
    print(v, v**2) """


# Ищем сумму всех 2х значных чисел
""" s=0 #заводим пер-ю в которой будет накапливаться сумма (на начало цикла =0)
for i in range(10,100):
    s=s+i #к сумме добавляем пер-ю i и при этом сохр в переменную суммы s
    # s=0+10 s=10+11 s=21+12  .... и так далее на входе s=0  далее ей присвоено другое значение
print(s) """



# Задача - найти факториал числа 3  3!=1*2*3 -  тоесть range(1,4)
# После выполнения цикла, переменная будет принимать последнее значение range
""" proizvedenie=1
for x in range(1,4):
    proizvedenie=proizvedenie*x
    print(proizvedenie)
print(proizvedenie) """


# Как найти факт-л  n  числа (вводимого)
""" n=int(input())
pr=1
for i in range(1,n+1):     # что бы взялось вводимое значение надо +1
    pr=pr*i
print(pr) """
#3
#6     -  ??? почему вывод два значения ???

#                       ---- Выполняем какое-то действие n - кол-во раз -------
""" n=int(input())
for i in range(n):
    print("PRIVET") """

# нужно вывести 5 случайных чисел в приделах от 1 до 100 в строчку
""" from random import randint
s=0
for i in range(3):  # количество чисел
    a=randint(1,10) # интервал цисел
    s+=a            # добавим сумму случайных чисел
    print(a, end=" ")
print()
print(s) """

# до этого мы нигде не использовали пер i. Пример использования
# в пер i - пробежимся от  1 до 10

""" for i in range(1,11):
    print("*"*i)
#***
#****
#*****
#******
#*******
#********
#*********
#********** """

# вводим n. Затем цикл повторяем n раз и внутри цикла вводим число a

n=int(input())
s=0
for i in range(n):
    a=int(input())
    s+=a                  # Суммируем вводимые  значения
    print('current s:',s) # выводим текущее значение суммы чисел
print('total',s)          # выводим готовую сумму
print('sred arrif=', s/n) # находим среднее арифм
















""" for number in number_list:
     if number % 2 == 0:
         print(number)
     else:
         print('Hey!') """

"""  list_numbers_sum = 0
 for number in number_list:
     list_numbers_sum = list_numbers_sum + number
 print(list_numbers_sum) """

""" 
 greeting = 'Hello Python!'
 for letter in greeting:
     print(letter) """

"""  greeting = 'Hello Python!'
 for letter in greeting:
     if letter != 'o':
         print(letter) """

"""  for letter in 'Hello Python!':
     if letter != 'o':
         print(letter)
 """

""" for letter in 'Hello Python!':
     print('One more letter!') """

"""  tuple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
 for item in tuple_list:
     print(item)
 for letter_1, letter_2 in tuple_list:
     print(letter_1, letter_2)
 for letter_1, letter_2 in tuple_list:
     print(letter_1) """

"""  tuple_list_1 = [('a', 'b', 1), ('c', 'd', 4), ('e', 'f', 5)]
 for letter_1, letter_2, number in tuple_list_1:
     print(letter_1, letter_2, number) """

"""  dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
  key-value pairs in tuples
 for item in dictionary.items():
     print(item) """


# # keys
"""  for item in dictionary:
     print(item)
 for item in dictionary.keys():
     print(item)
 for key, value in dictionary.items():
     print(key) """


# # values
"""  for item in dictionary.values():
     print(item)
 for key, value in dictionary.items():
     print(value)
 """


""" for _ in range(5):
    print('Hello!') """
