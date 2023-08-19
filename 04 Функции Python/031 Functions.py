# Создание функций
""" 
def privetstvie():
    '''
    vivod Hello
    '''
    print ('Hello!')

privetstvie()
#Hello!
help(privetstvie) # просмотр коментария 
"""
#Hello!
#Help on function privetstvie in module __main__:
#privetstvie()
#   vivod Hello



# Создание  функции с аргументами 
""" 
def function_this_arg(name = 'NAME'):  # = "Аргумент по умолчанию"
    '''
    :param 
    '''
    print('Hello ' + name + "  BRO")
function_this_arg('ANTON_argument_funkcii') 
"""
#  Hello ANTON_argument_funkcii  BRO
#function_this_arg()
#Hello NAME  BRO



# часто функции должны нам возвращать результат вычисления выражений или рез-т действий
# результаты мы можем поместить в переменную или в какую-то другую функцию 

""" 
x=function_this_arg("Anton")
print(x) 
"""
#None



# Создаем функцию возвращающую результат
"""
  def summ_of_2_numbers(a=0,b=0):
    '''  Рассказать о функции  ----- Это блок ДОКСТРИНГА ------ 
    Args:
        a (int, optional): первое слогаемое. Defaults = 0.
        b (int, optional): второе слогаемое. Defaults = 0.
    Returns:
        _type_: результат сложения
    '''   
    return a + b # !! Ключевое слово return для возврата функцией результата после нее ПРОИСХОДИТ ВЫХОД ИЗ Функции !!
x = summ_of_2_numbers(1,1)
print(x) 

""" 
#2
#help(summ_of_2_numbers)


""" Help on function summ_of_2_numbers in module __main__:

summ_of_2_numbers(a=0, b=0)
    _summary_

    Args:
        a (int, optional): первое слогаемое. Defaults = 0.
        b (int, optional): второе слогаемое. Defaults = 0.

    Returns:
        _type_: результат сложения 
"""


 # обычно функции решают какие-то проблемы. Например нам надо узнать
 # находится ли строка в тексте

""" 

def is_hello_in_text(text):
    if "hello" in text.lower():
        return True
    else:
        return False
print (is_hello_in_text('Sey privet'))

"""
#False
#print (is_hello_in_text('Sey hello'))
#True


# Это можно записать короче
""" 
text1=input('поздоровайся ')
def is_hello_in_text(text1):
    return "hello" in text1.lower() 
# .lower - приводит вводимый текст к нижнему регистру оператор in - возвращает True или False
print(is_hello_in_text('Privet'))
#False
print(is_hello_in_text('Hello'))
#True
print(is_hello_in_text(text1))
# добавил ввод с  калавиатуры
 """

#  Создадим функцию которая проверяет строку и сам текст

""" 
def is_string_in_text(string,text): # есть ни he в строке the apple
    return string in text.lower()
print(is_string_in_text("he", 'tHE apple'))
#True
print(is_string_in_text("het", 'the apple'))
#False 
"""

#  !если в функции есть еще какой-то код, то он должен быть  написан до ключевого слова return
def greeting_depends_on_gender(name,gender):
    if gender == "male":
        print('hello ' + name + ' !')
        return gender #Ключевое слово return для возврата функцией результата после нее ПРОИСХОДИТ ВЫХОД ИЗ Функции!!!!
    elif gender == "female":
        print('HELLO ' + name + " BAYBY")
        return gender
    else:
        print('HELLo ' + name + " ti che KRAB?")
        return gender


return_value1=greeting_depends_on_gender('Jack', "male")
return_value2=greeting_depends_on_gender('Jany', "female")
return_value3=greeting_depends_on_gender('Janasdasy', "assdasdsassadasdale")
print(return_value1)
print(return_value2)
print(return_value3)
#hello Jack !
#HELLO Jany BAYBY
#HELLo Janasdasy ti che KRAB?
#male
#female
#assdasdsassadasdale