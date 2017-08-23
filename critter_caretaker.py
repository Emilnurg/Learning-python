# Моя зверюшка
# Как тамогочи

class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):  # При любом действии повышаются
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        sad = self.boredom + self.hunger
        if sad < 5:
            m = "супер"
        elif sad >= 5 and sad <= 10:
            m = "not bad"
        elif sad > 10 and sad < 16:
            m = "так себе"
        else:
            m = "так, что щас сдохну"
        return m

    def talk(self):  # 1 - узнать о самочувтсвии
        print("Меня зовут ", self.name, ", и я сейчас чувствую себя", self.mood)
        self.__pass_time()  # каждый раз перещелкивает голод и скуку по +1

    def eat(self, food = 4):
        print("Едааааа!!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, game = 4):
        print("Крушить ломать))")
        self.boredom -= game
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
        
# Основная часть

def main():
    crit_name = input("Как вы назовете свою зверюшку? ")
    crit = Critter(crit_name)
        
    choice = None
    while choice != "0":
        print\
               ("""Моя зверушка
    0 - Выйти
    1- Узнать о самочувствии зверюшки
    2 - Покормить зверюшку
    3 - Поиграть со зверюшкой
    """)
        choice = input("Ваш выбор: ")
        print()
        if choice == "0":
            print("До свидания")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        else:
            print("Простите, я вас не понимаю. Выберете в диапозоне от 0 до 3")

# Запуск программы

main()
input("\n\nНажмите Enter, чтобы выйти")
