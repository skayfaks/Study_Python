# SETS - Множества. Это не упорядоченная коллекция уникальных элементов. Тоесть в множестве не может
# быль 2х одинаковых элементов

rainbow_colors={'red', 'orange', 'yellow', 'green', 'blue','indigo','violet'}
print(rainbow_colors)
print(type(rainbow_colors))
#{'indigo', 'blue', 'yellow', 'orange', 'violet', 'red', 'green'}
#<class 'set'>

#  Создаем пустое множество
Empty_set={}
print(Empty_set)
print(type(Empty_set))
#{}
# !!! <class 'dict'> !!
# для создания пустого множ надо записать так
Empty_set2 = set()
print(Empty_set2)
print(type(Empty_set2))
#set()
#<class 'set'>

# Можно создать  множ из других структур данных
numper_list=[1, 2, 3, 4]
text_tuple=('wer','wwer','sdf')
set_from_list = set(numper_list)
set_from_tuple = set(text_tuple)
print(set_from_list)
print(set_from_tuple)

# Так как во множестве сод-ся только уникальных элементы, то добавить в него такой же элемент нельзя!!
set_from_list.add(777777)
set_from_tuple.add('xxxxxxxx')
#{1, 2, 3, 4, 777777}
#{'sdf', 'xxxxxxxx', 'wwer', 'wer'}
set_from_list.add(777777)
set_from_tuple.add('xxxxxxxx')
print(set_from_list)
print(set_from_tuple)
#{1, 2, 3, 4, 777777}
#{'sdf', 'xxxxxxxx', 'wwer', 'wer'}
# Как мы видем по выводу команды. Добавление еще одних повторяющихся значений не произошло

# Метод .remove при удалении не сущ-ого объекта выдаст ошибку
# Метод .discard при удалении не выдаст ничего

set_from_list.remove(1)
set_from_list.discard(1)
print(set_from_list)
print(set_from_tuple)