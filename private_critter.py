# Закрытая зверюшка
# Демонстрирует закрытые переменные и методы

class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, mood):
        print("Появилась на свет новая зверюшка!")
        self.name = name #открытый атр~бут
        self.__mood = mood # закрытый атрибут
    #Чтобы создать собственный закрытЬiй атрибут,
    #просто начните его имя с двух символов подчеркивания.

    # Это верно и для атрибутов класса и методов.

    def talk(self):
        print("\nMeня зовут", self.name)
        print("Ceйчac я чувствую себя", self.__mood, "\n")

    def __private_method(self):
        print("Этo закрытый метод.")

    def public_method(self):
        print("Этo открытый метод.")
        self.__private_method()

# основная часть
crit = Critter(name ="Бобик", mood ="прекрасно")
crit.talk()
crit.public_method()

input("\n\nHaжмитe Enter. чтобы выйти.")

