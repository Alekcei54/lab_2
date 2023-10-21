import math
def if15():
    # Введення трьох чисел
    number1 = int(input("Введіть перше число: "))
    number2 = int(input("Введіть друге число: "))
    number3 = int(input("Введіть третє число: "))

    # Знаходимо найбільше і друге найбільше число
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
    it=0
    a=int(input("Введіть a: "))
    r=int(input("Введіть r: "))
    n =int(input("Введіть кількість точок: "))
    for i in range(n):
        print(f"Введіть координати точки {i + 1}:")
        x = float(input("x: "))  # Введення координати x
        y = float(input("y: "))  # Введення координати y
        if x**2+(y+r)**2>r*r and x<r and y> -r and y<x-r:
            it=it+1
        elif x**2 + (y+r)**2<r*r and y<x-r and x<0:
            it = it + 1
        elif x**2+(y+r)**2>r*r and y>x-r and x<0 and x>-r and y<-r:
            it = it + 1
    print(f"Точок потрапляє у фігуру:{it}")

def task24():
    x = float(input("Введіть x:"))
    E = 1e-5  # Мала величина для збіжності
    G = 1e5  # Велика величина для розбіжності
    sum = 0
    n = 0
    u = 1  # Ініціалізуємо `u` значенням 1 перед використанням

    while abs(u) >= E and abs(u) <= G:
        u = math.pow(x, 3 * n) / math.factorial(2 * n + 1)
        sum += u
        print(u)
        n += 1

    if abs(u) < E:
        print("Сума сходиться до заданої точності.")
    elif abs(u) > G:
        print("Ряд розходиться.")
if __name__ == "__main__":
    while True:
        print("\nОберіть опцію:")
        print("1. Визначити найбільшу сумму 2 чисел")
        print("2. Попадання в фігуру")
        print("3. Дослідження ряду на збіжність ")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            if15()
        elif choice == "2":
            task10()
        elif choice == "3":
            task24()
        elif choice == "0":
            break
        else:
            print("Невірний вибір. Виберіть 1, 2, 3 або 0.")