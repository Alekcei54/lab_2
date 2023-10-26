import functions


if __name__ == "__main__":
    while True:
        print("\nОберіть опцію:")
        print("1. Визначити найбільшу сумму 2 чисел")
        print("2. Попадання в фігуру")
        print("3. Дослідження ряду на збіжність ")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            functions.if15()
        elif choice == "2":
            functions.task10()
        elif choice == "3":
            functions.task24()
        elif choice == "0":
            break
        else:
            print("Невірний вибір. Виберіть 1, 2, 3 або 0.")
