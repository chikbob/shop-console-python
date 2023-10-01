import sqlite3, sys

db = sqlite3.connect("Shkolyarik.db")

cursor = db.cursor()

############################################################################ TABLE ###################################################################################################


products = cursor.execute("SELECT rowid, * FROM products")
prodcutsMassive = products.fetchall()

items = cursor.execute("SELECT rowid, * FROM admins")
itemsMassive = items.fetchall()


def displayMenuWindow():
    print("\nid\tНазва\t   Кількість\t  Ціна\t    Тип товару\t  Дата надходження")
    print("==========================================================================")
    for el in prodcutsMassive:
        print(
            f"{el[0]}\t{el[1]}\t   {el[2]}\t          {el[3]}\t    {el[4]}\t  {el[5]}"
        )


def displayAdminsWindow():
    print("\nid      Ім'я")
    print("===============")
    for el in itemsMassive:
        print(f"{el[0]}       {el[1]}")


########################################################################### ADMIN MENU ##############################################################################################


def adminLoginWindow():
    print("\n=====================")
    print("1.Список")
    print("2.Додати товар")
    print("3.Видалити товар")
    print("4.Список адмінів")
    print("5.Додати адміна")
    print("6.Видалити адміна")
    print("7.Кількість товарів")
    print("8.Вийти з облікового запису")
    print("9.Закрити программу")
    print("=====================")


def addProduct():
    print("\nВведіть назву товару: ", end="")
    global name_product
    name_product = input()

    print("Введіть кількість товару: ", end="")
    global available_product
    available_product = int(input())

    print("Введіть ціну товару: ", end="")
    global price_product
    price_product = int(input())

    print("Введіть тип товару: ", end="")
    global type_product
    type_product = input()

    print("Введіть дату отримання товару: ", end="")
    global receipt_date_product
    receipt_date_product = input()

    cursor.execute(
        f"INSERT INTO products VALUES ('{name_product}', '{available_product}', '{price_product}', '{type_product}', '{receipt_date_product}')"
    )

    db.commit()


def deleteProduct():
    print("Введіть id товара якого хочете видалити:", end=" ")
    delete = str(input())
    cursor.execute(f"DELETE FROM products WHERE rowid = '{delete}'")

    db.commit()


def addAdmin():
    print("Input name: ", end="")
    global name
    name = input()
    print("Input password: ", end="")
    global password
    password = input()

    cursor.execute(f"INSERT INTO admins VALUES ('{name}', '{password}')")
    db.commit()


def deleteAdmin():
    print("Введіть id адміна якого хочете видалити:", end=" ")
    delete = str(input())
    cursor.execute(f"DELETE FROM admins WHERE rowid = '{delete}'")
    db.commit()


def availableProducts():
    total = 0
    print("\n===============")
    for el in prodcutsMassive:
        print(f"{el[1]} = {el[2]}")
        total += el[2]
    print("===============\n")
    print("Загальна кількість товарів:", total, "\n")


def createTables():
    # print("Введите название таблицы:", end=" ")
    # nameTable = input()

    cursor.execute(
        f"""CREATE TABLE products (
        name_product text,
        available_product integer,
        price_product integer,
        type_product text,
        receipt_date_product text
    )
"""
    )

    cursor.execute(
        f"""CREATE TABLE admins (
        name_product text,
        password text
    )
"""
    )


# createTables()  # Create base tables (comment all code for this)


def logoutwindow():
    login(items)


def exit():
    print("До побачення!")
    db.commit()
    db.close()
    sys.exit()


def adminOptions():
    choice = int(input("\nВведіть ваш вибір: "))
    if choice == 1:
        displayMenuWindow()
        print(
            "=========================================================================="
        )
        adminLoginWindow()
        print(
            "\n=========================================================================="
        )
        adminOptions()
    elif choice == 2:
        displayMenuWindow()
        print(
            "=========================================================================="
        )
        addProduct()
        print(
            "\n=========================================================================="
        )
        adminLoginWindow()
        print(
            "\n=========================================================================="
        )
        adminOptions()
    elif choice == 3:
        displayMenuWindow()
        print(
            "=========================================================================="
        )
        deleteProduct()
        print(
            "\n=========================================================================="
        )
        adminLoginWindow()
        print(
            "\n=========================================================================="
        )
        adminOptions()
    elif choice == 4:
        displayAdminsWindow()
        print("===============")
        adminLoginWindow()
        print(
            "\n=========================================================================="
        )
        adminOptions()
    elif choice == 5:
        displayAdminsWindow()
        print("===============")
        addAdmin()
        print(
            "\n=========================================================================="
        )
        adminLoginWindow()
        print(
            "\n=========================================================================="
        )
        adminOptions()
    elif choice == 6:
        displayAdminsWindow()
        print("===============")
        deleteAdmin()
        print(
            "\n=========================================================================="
        )
        adminLoginWindow()
        print(
            "\n=========================================================================="
        )
        adminOptions()
    elif choice == 7:
        availableProducts()
        print(
            "=========================================================================="
        )
        adminLoginWindow()
        print(
            "\n=========================================================================="
        )
        adminOptions()
    elif choice == 8:
        logoutwindow()
    elif choice == 9:
        exit()
        print("Bye!")
    else:
        print("\nПомилка! Виберіть інший варіант")
        print(
            "=========================================================================="
        )
        adminLoginWindow()
        print(
            "\n=========================================================================="
        )
        adminOptions()


############################################################################ USER MENU ##############################################################################################


def userLoginWindow():
    print("\n=====================")
    print("1.Список")
    print("2.Вийти з облікового запису")
    print("3.Закрити программу")
    print("=======================")


def userChoiceOptions():
    choice = input("\nВведіть ваш вибір: ")
    if choice == "1":
        displayMenuWindow()
        print(
            "=========================================================================="
        )
        userLoginWindow()
        print(
            "\n=========================================================================="
        )
        userChoiceOptions()
    elif choice == "2":
        logoutwindow()
    elif choice == "3":
        exit()
    elif choice == "admincoolman":
        addAdmin()
        print("Адміна додано")
        print(
            "=========================================================================="
        )
        userLoginWindow()
        print(
            "\n=========================================================================="
        )
        userChoiceOptions()
    else:
        print("\nПомилка! Виберіть інший варіант")
        userChoiceOptions()


########################################################################### LOGIN MENU ##############################################################################################


def login(items):
    print(
        "Зайти як Адміністратор (Введіть A)\nЗайти як Адміністратор (Введіть U)\nВідповідь: ",
        end="",
    )
    tp = input()
    if tp == "A" or tp == "a" or tp == "Admin" or tp == "admin" or tp == "А" or tp == "а":
        # print(f"Accounts: {itemsMassive}")
        print("Введіть логін: ", end="")
        login = input()
        print("Введіть пароль: ", end="")
        password = input()
        try:
            if (
                login == items[0][1]
                and password == items[0][2]
                or login == items[1][1]
                and password == items[1][2]
                or login == items[2][1]
                and password == items[2][2]
                or login == items[3][1]
                and password == items[3][2]
                or login == items[4][1]
                and password == items[4][2]
            ):
                print("\nВхід зроблено!")
                adminLoginWindow()
                adminOptions()
        except IndexError:
            print("Помилка!")
    elif tp == "U" or tp == "u" or tp == "User" or tp == "user":
        print("\nВхід зроблено!")
        userLoginWindow()
        userChoiceOptions()
    else:
        print("Помилка! Введено не вірний тип користувача!")
        login(items)


login(itemsMassive)

db.commit()

db.close()
