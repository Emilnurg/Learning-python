# Отгадай число
#
# Компьютер выбирает случайное число в диапазоне от 1 до 100
#Игрок пытается отгадать это число. и компьютер говорит.
# предположение больше/меньше. чем за.гаданное число.
# или попало в точку

print("\t\t\tДобро пожаловать в игру 'Отгадай число'!")
print("\nЯ загадал число от 1 до 100")
print("Постарайтесь отгадать его за минимальное число попыток\n\n")
import random
number = random.randint(1, 100)
younumber = int(input("Ваше предложение: "))
attempts = 1

while younumber != number:
    if younumber > number:
        print("Меньше...")
    if younumber < number:
        print("Больше...")
    younumber = int(input("Ваше предложение: "))
    if younumber == number:
        print("Вам удалось отгадать число!!! Это в самом деле ", number)
        print("Вы затратили на отгадывание всего", attempts, " попыток!")
    attempts += 1
    if attempts > 8:
        print("Ты че сука совсем тупой?")
        break

input("Жми Enter")

