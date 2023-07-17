#  Кортэжи (). Похожи на Списки [] НО с не изменяемым сожержанием

tuple_1 = 1,2,3
tuple_2 = ('one', 'hello')
tuple_3 = (3,2.3,'three')
print(tuple_1)
print(type(tuple_1))
#<class 'tuple'>
print(tuple_2)
print(tuple_3)
#(1, 2, 3)
#('one', 'hello')
#(3, 2.3, 'tthree')

# для замены элемента создаем НОВЫЙ кортэж внутри которого обращаемся к значениям из предыдущего
new_tuple  = (tuple_1[0], 3, tuple_1[2], tuple_2[-1])
print(new_tuple)
#(1, 3, 3, 'hello')

x=y=z=12
print(y)

x, y, z = 12,13,14
print(x, y, z)
#12 13 14

# Распаковка кортэжа в переменные
person_tuple = ('Anton', 'Kriv','1985')
name, last_name, birth = person_tuple
print(person_tuple)
#('Anton', 'Kriv', '1985')

# Сколько раз встречается в кортэже значение - функция count. работает и для строковых значений
t1 = (1,2,5,1,7,9)
print(t1.count(1))
#2

# Метод Индекс. Можно вычеслить индекс указываемого значения
print(t1.index(5))
#2


