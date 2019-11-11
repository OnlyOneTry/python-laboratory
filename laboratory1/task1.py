import re

def bit_operations():
    a = input("Введите число a в двоичной системе исчесления: ")
    b = input("Введите число b в двоичной системе исчесления: ")

    def bit_Valid(bit):
        """
        check if it 0 and 1 only
        :param bit: string
        :return: bool
        """
        if bool(re.fullmatch('\s*[01]+\s*', bit)):
            return True
        else:
            return False
    while not bit_Valid(a):
        a = input("Введите число a в двоичной системе исчесления: ")
    while not bit_Valid(b):
        b = input("Введите число b в двоичной системе исчесления: ")
    bit_and = int(a, 2) & int(b, 2)
    print("Результат побитового и: %s" % bin(bit_and))
    bit_or = int(a, 2) | int(b, 2)
    print("Результат побитового или:  %s" % bin(bit_or))
    bit_xor = int(a, 2) ^ int(b, 2)
    print("Результат побитового исключающего или: %s" % bin(bit_xor))

    p = input("Запустить программу заново? +/-")
    if p == "+":
        bit_operations()
    else:
        return


bit_operations()