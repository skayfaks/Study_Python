""" # Создание функций
def privetstvie():
    '''
    vivod Hello
    '''
    print ('Hello!')

privetstvie()
#Hello!
help(privetstvie) # просмотр коментария """
#Hello!
#Help on function privetstvie in module __main__:
#privetstvie()
#   vivod Hello

# Создание  функции с аргументами 

""" def function_this_arg(name = 'NAME'):  # = "Аргумент по умолчанию"
    '''
    :param 
    '''
    print('Hello ' + name + "  BRO")
function_this_arg('ANTON_argument_funkcii')
#  Hello ANTON_argument_funkcii  BRO
function_this_arg()
#Hello NAME  BRO

# часто функции должны нам возвращать результат вычисления выражений или рез-т действий
# результаты мы можем поместить в переменную или в какую-то другую функцию 

x=function_this_arg("Anton")
print(x)
#None """


# Создаем функцию возвращающую результат
def summ_of_2_numbers(a = 0,b=0):
    """_summary_

    Args:
        a (int, optional): первое слогаемое. Defaults to 0.
        b (int, optional): второе слогаемое. Defaults to 0.

    Returns:
        _type_: результат сложения
    """       
    return a + b #  Ключевое слово return для возврата функцией результата
x = summ_of_2_numbers(1,1)
print(x)
#2