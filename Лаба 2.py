def cycled_input(text, input_type, valid_cond):
    input_type = type(input_type).__name__

    while True:
        try:
            if input_type == "int":
                user_input = int(input(text))
            elif input_type == "float":
                user_input = float(input(text))
            else:
                user_input = input(text)
        except ValueError:
            print("You entered wrong value. Let's try again.")
            continue

        if valid_cond is not None and valid_cond(user_input) is not True:
            print("input value is not valid.")
        else:
            return user_input
    return


while True:
    t1 = cycled_input("Количество баллов Иванова в первом туре: ", float(0), None)
    n1 = cycled_input("Количество баллов Иванова во втором туре: ", float(0), None)
    p1 = cycled_input("Количество баллов Иванова в третьем туре: ", float(0), None)
    t2 = cycled_input("Количество баллов Петрова в первом туре: ", float(0), None)
    n2 = cycled_input("Количество баллов Петрова во втором туре: ", float(0), None)
    p2 = cycled_input("Количество баллов Путрова в третьем туре: ", float(0), None)
    t3 = cycled_input("Количество баллов Сидорова в первом туре: ", float(0), None)
    n3 = cycled_input("Количество баллов Сидорова во втором туре: ", float(0), None)
    p3 = cycled_input("Количество баллов Сидорова в третьем туре: ", float(0), None)
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

