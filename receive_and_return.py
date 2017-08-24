# Принимай - возвращай
# Демонстрирует параметры и возвращаемые значения
def display(message):
    print(message)
def give_me_five():
    five = 5
    six = 6
    return five, six
def ask_yes_no(question):
    """Задает вопрос с ответом 'да' или 'нет' """
    response = None
    while response not in ("у", "n"):
        response = input(question).lower()
    return response

# основная часть
display("Baм сообщение\n")
number = give_me_five()
print("Boт что возвратила функция give_me_five(): ", number)
answer = ask_yes_no("\nПожалуйста. введите ·у· или 'n': ")
print("Спасибо. что ввели", answer)

input("\n\nHaжмитe Enter. чтобы выйти.")
