# Зверюшка с атрибутами
# Демонстрирует создание атрибутов объекта и доступ к ним

class Critter(object):
    """Виртуальный питомец"""
    
    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        
    def __str__(self):  #представлять объекты строками для вывода на экран.
        rep = "Объект класса Critter\n"
        rep += "имя: " + self.name + "\n"
        return rep
    
    def talk(self):
        print("Привет. Меня зовут", self.name, "\n")

# основная часть
critl = Critter("Бoбик")
critl.talk()

crit2 = Critter("Мурзик")
crit2.talk()

print("Bывoд объекта critl на экран:")
print(critl)

print("Непосредственный доступ к атрибуту critl.name:")
print(critl.name)


input("\n\nHaжмитe Enter. чтобы выйти.")
