# Понимание списков. Концепция по созданию списков.
# Можно сделать при помощи цикла


# for <переменная> in <итерируемый объект - у которого  можно перебирать значения>:
#     <Тело цикла>


# Создание списка из последовательности

""" greeating="Hello!"              #  переменная (строка) 
letter_list=[]                  #  переменная списка (создание пустого списка)
for letter in greeating:        #  цикл по добавлению в лист данных из переменной, перебор символа из пер-ой greeating
    letter_list.append(letter)  #  добавляем буквы в letter_list с помощью append
print(letter_list)
#['H', 'e', 'l', 'l', 'o', '!'] """

# Создание списка и его инициализация
""" greeating="Hello!"
letter_list=[letter for letter in greeating]   # for буквы из строки greeating поместить 
print(letter_list)
#['H', 'e', 'l', 'l', 'o', '!']

number_list=[number for number in '0123456']
print(number_list)
#['0', '1', '2', '3', '4', '5', '6']

number_list1=[num for num in range(0,5)]
print(number_list1)
#[0, 1, 2, 3, 4]

number_list2=[num **2 for num in range(0,5)] #можно производить возведение в степень
print(number_list2)
#[0, 1, 4, 9, 16]

number_list3=[(((num -3)/2)*2) for num in range(0,5)] #можно производить возведение в степень
print(number_list3)
#[-3.0, -2.0, -1.0, 0.0, 1.0] """




# Можно применить отбор элементов по заданному условию - через оператор if

number_list=[6,2,11,-55,-12,0,3,345]  # Можно отобрать только положительные значения
""" new_list = [number for number in number_list if number>0]
print(new_list)
#[6, 2, 11, 3, 345] """


# Пример - если встречаем положительное число помещаем +, если отрицательное -
new_list1=["+" if number>0 else "-" if number<0 else 'zero' for number in number_list]
# мы переносим вперед оператор if если применяется else !!
print(new_list1)
#['+', '+', '+', '-', '-', 'zero', '+', '+']


chislovoy_ryad=[-1,2,3,-23]
new=['+' if num>0 else print("otricetelnoe") for num in chislovoy_ryad]
print(new)
