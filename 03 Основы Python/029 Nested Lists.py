#   Вложенные списки
# !! Вложенные списки и вложенные циклы используются очень часто. Например при извлечении вложенной информации.
#  !! Используеься в DataSince используется в матрицах.

""" nested_list=[[1,2,3],[4,5,6,7],[7,8]] """

""" print(nested_list)
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(len(nested_list))
# 3  - длинна списка 3-элемента внутри

# узнать длинну вложенного списка  - нумерация с 0
print(len(nested_list[1]))
#4
print(len(nested_list[-1]))     #- нумерация с 1
#2 """

#получение 5
""" print(nested_list[1][1]) # обращение к значению  внутри 
print(nested_list[-2][1])
print(nested_list[-2][-3]) """


#как распечатать все значения листа и внутреннего и внешнего ? 

""" for inner_list in nested_list:
    print(inner_list) """
#[1, 2, 3]
#[4, 5, 6, 7]
#[7, 8]
 #          Когда у нас есть вложенные списки, нам необходимо использовать вложенные циклы !!
""" nested_list=[[1,2,3],[4,5,6,7],[7,8]]
for inner_list in nested_list:
    for number in inner_list:
        print(number, end=' ')   """
# 1 2 3 4 5 6 7 7 8


# Запись с использованием List Comprehension
""" nested_list=[[1,2,3],[4,5,6,7],[7,8]]
[[print(number,end='') for number in inner_list] for inner_list in nested_list] """
#123456778

# ролик на ютубе https://www.youtube.com/watch?v=0qtLrRm36J0 
""" a=[[1,2,3],[4,5,6,7],[7,8]]
b=['hello', 'hi', 'bro']
print((a[1][1]),(b[0])) """
#5 hello

a=[[1,2,3],
   [4,5,6],
   [7,8,7]]

""" for i in a:
    print(i) """
#[1, 2, 3]
#[4, 5, 6]
#[7, 8, 7]

""" for i in a:
    for j in i: # Так как переменная i - хранит в себе список, мы вправе обойти все ее элементы. Заводим вторую переменную
        print(j, end =' ') # вывод 123456787
    print()     """           # перенос можно сделать пустым принтом
#123
#456
#787
# При таком варианте обхода у нас нет номера элемента в списке 
# и нет возможности повлиять на значение элемента хранимого в списке
""" for i in a:
    for j in i:
        j+=10 # Так как переменная i - хранит в себе список, мы вправе обойти все ее элементы. Заводим вторую переменную
        print(j, end =' ') # вывод 123456787
    print()               # перенос можно сделать пустым принтом
print(a) """
#111213
#141516
#171817
#[[1, 2, 3], [4, 5, 6], [7, 8, 7]]

# Второй вариант обход по индексам  тайминг 6.46
# [строка][столбец]
a=[[1,2,3,11],
   [4,5,6,22],
   [7,8,7,33]]

""" for stroki in range(3):
    for stolbci in range(4):
        a[stroki][stolbci]+=10  # Увеличение каждого элемента на 10
        print(a[stroki][stolbci], end=' ')
    print()
print(a) """
# 11 12 13 21
# 14 15 16 32
# 17 18 17 43
#[[11, 12, 13, 21], [14, 15, 16, 32], [17, 18, 17, 43]]  Элементы списка изменились

#  вариант обхода по столцам. для  этого в данном примере меняем циклы местами
""" for stolbci in range(4):
    for stroki in range(3):
        a[stroki][stolbci]+=10  # Увеличение каждого элемента на 10
        print(a[stroki][stolbci], end=' ')
    print() """
# 11 14 17
# 12 15 18
# 13 16 17
# 21 32 43

# можно обходить справа на лево и снизу вверх
""" a=[[1,2,3,11], #0
   [4,5,6,22], #1
   [7,8,7,33]] #2 
for stroki in range(2,-1,-1): # начинаем со строки и идем в убыв порядке со 2  строки  -1 (до 0) с шаг -1
    for stolbci in range(3,-1,-1):
        print(a[stroki][stolbci], end=' ')
    print("\n") """
# 33 7 8 7 
# 22 6 5 4 
# 11 3 2 1

# Например нам надо посчитать суммы каждой строки и каждого столбца
#  считаем стороки
for stroki in range(3):
    s=0                 # сумма должна обнулиться после вычисления строки
    for stolbci in range(4):
        s+=a[stroki][stolbci]
    print(s)

#  считаем столбцы
for stolbci in range(4):
    s=0                 # сумма должна обнулиться после вычисления строки
    for stroki in range(3):
        s+=a[stroki][stolbci]
    print(s)