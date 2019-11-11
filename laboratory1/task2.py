import re

def cycled_input(text, input_type, valid_cond):
    input_type = type(input_type).__name__



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

while True:
    t1 = input("Количество баллов Иванова в первом туре: ")
    n1 = input("Количество баллов Иванова во втором туре: ")
    p1 = input("Количество баллов Иванова в третьем туре: ")
    t2 = input("Количество баллов Петрова в первом туре: ")
    n2 = input("Количество баллов Петрова во втором туре: ")
    p2 = input("Количество баллов Путрова в третьем туре: ")
    t3 = input("Количество баллов Сидорова в первом туре: ")
    n3 = input("Количество баллов Сидорова во втором туре: ")
    p3 = input("Количество баллов Сидорова в третьем туре: ")

    t1 = floatCheck(t1)
    n1 = floatCheck(n1)
    p1 = floatCheck(p1)
    t2 = floatCheck(t2)
    n2 = floatCheck(n2)
    p2 = floatCheck(p2)
    t3 = floatCheck(t3)
    n3 = floatCheck(n3)
    p3 = floatCheck(p3)

    a = t1 + n1 + p1
    b = t2 + n2 + p2
    c = t3 + n3 + p3
    if a >= b and a >= c:
        print("Иванов набрал: ", a)
    if b >= a and b >= c:
        print("Петров набрал: ", b)
    if c >= a and c >= b:
        print("Сидоров набрал: ", c)
    is_continue = input("Повторить код? +/- : ")
    if is_continue != "+" :
        break

