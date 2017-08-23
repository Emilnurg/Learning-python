# Зверюшка с конструктором
# Демонстрирует метод-конструктор

class Critter(object):
    """Виртуальный питомец"""
    def __init__(self):
        print("Появилась на свет новая зверюшка!")
    def talk(self):
        print("\nПpивeт. Я зверюшка - экземпляр класса Critter.")
# основная часть
critl = Critter()
crit2 = Critter()
critl.talk()
crit2.talk()
input("\n\nHaжмитe Enter. чтобы выйти.")
