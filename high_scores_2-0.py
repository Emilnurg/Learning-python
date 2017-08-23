# Рекорды 2.0
# Демонстрирует вложенные последовательности

scores = []
choice = None
attempts = 0
while choice != "0":
    print(
    """
Рекорды 2. О
О - Выйти
1 - Показать рекорды
2 - Добавить рекорд
""")
    choice = input("Baш выбор: ")
    print()
    # выход
    if choice == "0":
        print("До свидания.")
    elif choice == "1":
        print("Рекорды :")
        print("ИМЯ      РЕЗУЛЬТАТ")
        for you in scores:
            print(you[0], "   ", you[1])  
    elif choice == "2":
        you_name = str(input("Введите имя игрока: "))
        you_score = int(input("Впишите его результат: "))
        you = (you_name, you_score)
        scores.append(you)
        scores.sort(reverse=True)
        scores = scores[:5] # останется только 5 рекордов
    else:
        print("Ну нету такого рекорда(( ")
    

input("\n\nHaжмитe Enter. чтобы выйти.")
