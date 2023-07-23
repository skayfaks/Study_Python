number_list = [32,21,48,34.34]
print(number_list)
#[32, 21, 48, 34.34]

some_list =  [12,35.22, 'STROKA']
print(some_list)
#[12, 35.22, 'STROKA']

print(len(some_list)) #через функцию len узнаем количество элементов в листе
#3

#индексация и слайсинг элементов списка
print(some_list[1])
#35.22

#слайсинг (например хотим скопировать первые два элемента)
slising_list = (some_list[:2])
print(slising_list)
#[12, 35.22]

# В списках можно менять значение сод-ся во внутренних данных заменим значение STROKA на NEW
some_list[2] = "NEW"
print(some_list)
#[12, 35.22, 'NEW']

# Применение канкатенации 2х списков
konkat = number_list + slising_list
print(konkat)
#[32, 21, 48, 34.34, 12, 35.22]

# добавляем эл-т в конец имеющегося списка - юзаем метод .append
konkat.append ('new_item')
print(konkat)
#[32, 21, 48, 34.34, 12, 35.22, 'new_item']

# что делать, когда надо добавить в другое место списка? например в начало
konkat.insert(0,'START')
print(konkat)
#['START', 32, 21, 48, 34.34, 12, 35.22, 'new_item']

# можем вставить в любое место списка
konkat.insert(2, 12345678)
print(konkat)
#['START', 32, 12345678, 21, 48, 34.34, 12, 35.22, 'new_item']

# Removing items - используем метод .pop 
list_2 = ['y',1,2,3,4,5,6,'x']
list_2.pop()
print(list_2)
#['y', 1, 2, 3, 4, 5, 6]

list_2.pop(-2)
print(list_2)
#['y', 1, 2, 3, 4, 6]

# мы  можем сохвранить удаленный элемент в переменную и вывести ее на печать 
deleted_item = list_2.pop()
print(list_2)
print(deleted_item)
#['y', 1, 2, 3, 4]
#6 

# удаление по значению из списка .remove
deleted_item = list_2.remove(1)
print(list_2)
#['y', 2, 3, 4]

# заводим новые два листа!!
number_list2 = [45,12,3,-445,22]
letter_list = ['s', 'w', 't', 'a']
print(number_list2)
print(letter_list)
#[45, 12, 3, -445, 22]
#['s', 'w', 't', 'a']

# Сортировка .sort (НЕ возвращает никакого значения - просто сортирует)
number_list2.sort()
letter_list.sort()
print(number_list2)
print(letter_list)
#[-445, 3, 12, 22, 45]
#['a', 's', 't', 'w']

# ЧАСТАЯ ОШИБКА
X  =  number_list2.sort()
print(X)
#None

# Правильно сначала сортить потом присваивать для переменной
number_list2.sort()
x = number_list2
print(x)
#[-445, 3, 12, 22, 45]

# Медод реверса .reverse
print(number_list2)
print(letter_list)
#[-445, 3, 12, 22, 45]
#['a', 's', 't', 'w']
number_list2.reverse()
letter_list.reverse()
print(number_list2)
print(letter_list)
#[45, 22, 12, 3, -445]
#['w', 't', 's', 'a']

# Создание структуры данных лист в тисте
number_list2.append(letter_list)
print(number_list2)
#[45, 22, 12, 3, -445, ['w', 't', 's', 'a']]