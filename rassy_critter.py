# Рассово верная зверюшка
# Демонстрирует атрибуты класса и статические методы

class Critter(object):
    """Виртуальный питомец"""
    total = 0
    @staticmethod  # декоратор
    def status():
        print("\nBcero зверюшек сейчас", Critter.total) #Атрибут класса, а не имени
    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        Critter.total += 1  #каждый раз при создании нового объекта

# основная часть
print("Haxoжy значение атрибута класса Critter.total :", end=" ")
print(Critter.total)

print("\nCoздaю зверюшек.")
critl = Critter("зверюшка 1")
crit2 = Critter("зверюшка 2")
critЗ = Critter("зверюшка 3")
Critter.status()

print("\nOбpaщaюcь к атрибуту класса через объект:", end=" ")
print(critl.total)  #Не смотря что crit1 должен иметь total=1, /
#атрибут все равно относится только к классу total = 3


input("\n\nHaжмитe Enter. чтобы выйти.")
