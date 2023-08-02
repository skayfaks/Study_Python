# https://pythonclass.ru/python/cikl-for-i-funkciya-range-v-python/
# Цикл с известным колличеством повторений
# C помощью него можно обойти все элементы этерируемой последовательности или этер-ого объекта
# Решает задачу - перебрать весь список и извлечь из него необходимые данные.
# Цикл for позволяет перебрать любой итерируемый объект, то есть объект, из которого команда for 
# сможет брать элементы по одному, пока не будет обработан последний элемент, не зависимо от его длины.


# https://www.youtube.com/watch?v=yPUA8xBEyzM
# for <переменная> in <объект>:
#     <Тело цикла>

""" number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
     print(str(number) + ' Hola!')

x=['q','w','e','r','t','y']
for y in x:
     print(y) """


# сумма всех 2х значных чисел
s=0
for i in range(10,100):
    s=s+i
print(s)



# Задача - найти факториал числа 3  3!=1*2*3 

y=1
for x in range(1,4):
    y=y*x
    print(y)
print(y)

#Числа которые делятся на 2 и на 7
for i in range(100,1000):
    if i%2==0 and i%7==0:
        print(i)

# Все квадраты чисел от 1 до 10
for v in range(1,11):
    print(v, v**2)



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
