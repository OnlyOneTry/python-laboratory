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

def intValid(num):
    """
    check if it int
    :param num: any
    :return: bool
    """
    if bool(re.fullmatch('\s*\d+\s*', num)):
        return True
    else:
        return False

def intCheck(a):
    """
    if a is int return it or force to enter int
    :param a: any
    :return: int
    """

    while True:
        if intValid(a):
            return int(a)
        else:
            print('Введить тильки цілі числа')
            a = input()

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

while True:
    n = input("Введите значение n: ")
    n = intCheck(n)
    x = input("Введите значение x: ")
    x = floatCheck(x)
    i = 1
    Sum = 0
    for i in range (1, n+1):
        Sum += x /(2 ** i)
    print(Sum)
    print("Повторить программу? +/-")
    answer = input("")
    if answer == "-":
        break