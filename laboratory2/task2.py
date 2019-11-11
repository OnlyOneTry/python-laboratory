import re

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

def oCheck(num):
    """
    if a is Natural+0 number return it or force to enter Natural+0 number
    :param num: any
    :return: NAtural+0 number
    """
    b = intCheck(num)
    while True:
        if b >= 0:
            return b
        print('введіть занчення ≥ 1')
        b = intCheck()

while True:
    n = input("Введите целое число: ")
    n = oCheck(n)

    k = 0
    while k ** 2 <= n:
        k += 1
    print(k-1)
    print("Повторить программу? +/-")
    answer = input("")
    if answer == "-":
        break