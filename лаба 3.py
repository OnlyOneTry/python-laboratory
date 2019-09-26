def myfunc():
    try:
        x = float(input("Введите значение x: "))
    except:
        print("Введите числовое значение!")
        myfunc()

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