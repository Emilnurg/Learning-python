# Эксклюзивная сеть
# Демонстрирует составные условия и логические операторы
print("\tЭксклюзивная компьютерная сеть")
print("\tТoлькo для зарегистрированных пользователей!\n")
security = 0
username = ""
while not username:
    username = input("Логин: ")
password = ""
while not password:
    password = input("Пapoль: ")
if username == "D.Lawson" and password == "secret":
    print("Привет. Дрейк. ")
    security = 5
elif username == "S.Meier" and password == "civilization":
    print("Здравствуй. Сид.")
    security = 3
elif username == "S.Miyamoto" and password == "mariobros":
    print("Дoбporo времени суток. Сигеру.")
    security = 3
elif username == "W.Wright" and password == "thesims":
    print("Kaк дела. Уилл?")
    security = 3
elif username == "guest" or password == "guest":
    print("Дoбpo пожаловать к нам в гости.")
    security = 1
else:
    print( "Войти в систему не удалось. Должно быть. вы не очень-то эксклюзивный\
 гражданин.\n")
input("\n\nHaжмитe Enter. чтобы выйти.")









