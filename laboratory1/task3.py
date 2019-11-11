import re

def floatValid(num):

    """
        check if it float
        :param num: any
        :return: bool
        """
    if bool(re.fullmatch('\s*\d+(\.\d+)?\s*', num)):
        return True
    else:
        return False

def floatCheck(a):
    """
     if a is float return it or force to enter float
    :param a: any
    :return: float
    """
    while True:
        if floatValid(a):
            return float(a)
        else:
            print('введіть тільки цифри')
            a = input()

def myfunc():

    x = input("Введите значение x: ")
    x = floatCheck(x)


    if x > 3 :

        print("x = %.4f" %(1.2 * x ** 2 - 3*x - 9))
        c = input("Продолжить тестирование программы? +/-")
        if c == '+' :
            myfunc()
        else:
            return ()

    else:
        print("x = %.4f" %(12.1/(2 * x ** 2 + 1)))
        c = input("Продолжить тестирование программы? +/-")
        if c == '+':
            myfunc()
        else:
            return ()


myfunc()