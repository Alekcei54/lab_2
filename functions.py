import math


def if15():
    """Необхідно записувати умову завдання у строку документації"""
    # Введення трьох чисел
    try:
        number1 = int(input("Введіть перше число: "))
        number2 = int(input("Введіть друге число: "))
        number3 = int(input("Введіть третє число: "))
    except ValueError:
        print("Wrong input!")
    else:
        # Знаходимо найбільше і друге найбільше число
        # !!!Так може краще занходити мінімальне число і сумувати два інших? !!!
        max_number = max(number1, number2, number3)
        if number1 == max_number:
            second_max_number = max(number2, number3)
        elif number2 == max_number:
            second_max_number = max(number1, number3)
        else:
            second_max_number = max(number1, number2)

        # Знаходимо суму двох найбільших чисел
        sum_of_max_two = max_number + second_max_number
        print(f"Сума двох найбільших чисел: {sum_of_max_two}")


def task10():
    it = 0
    try:
        a = int(input("Введіть a: "))
        r = int(input("Введіть r: "))
        n = int(input("Введіть кількість точок: "))
    except ValueError:
        print("Wrong input!")
    else:
        for i in range(n):
            print(f"Введіть координати точки {i + 1}:")
            try:
                x = float(input("x: "))  # Введення координати x
                y = float(input("y: "))  # Введення координати y
            except ValueError:
                print("X, Y must be float")
            else:
                if x ** 2 + (y + r) ** 2 > r * r and x < r and y > -r and y < x - r:
                    it = it + 1
                elif x ** 2 + (y + r) ** 2 < r * r and y < x - r and x < 0:
                    it = it + 1
                elif x ** 2 + (y + r) ** 2 > r * r and y > x - r and x < 0 and x > -r and y < -r:
                    it = it + 1
            print(f"Точок потрапляє у фігуру:{it}")


def task24():
    E = 1e-5  # Мала величина для збіжності
    G = 1e5  # Велика величина для розбіжності
    sum = 0
    n = 0
    u = 1  # Ініціалізуємо `u` значенням 1 перед використанням
    try:
        x = float(input("Введіть x:"))
    except ValueError:
        print("Wrong input!")
    else:
        while abs(u) >= E and abs(u) <= G:
            u = math.pow(x, 3 * n) / math.factorial(2 * n + 1)
            sum += u
            print(u)
            n += 1

        if abs(u) < E:
            print("Сума сходиться до заданої точності.")
        elif abs(u) > G:
            print("Ряд розходиться.")