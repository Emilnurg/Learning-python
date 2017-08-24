# Зверюшка со свойствами
# Демонстрирует свойства

class Critter(object) :
    """Виртуальный питомец"""
    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
    @property

    def name(self):
        return self.__name

    @name.setter #setter системное слово, устанавливает новое значение свойства name
    def name(self, new_name):
        if new_name == "":
            print("Имя зверюшки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")

    def talk(self):
        print("\nПpивeт. меня зовут", self.name)

# основная часть
crit = Critter("Бoбик")
crit.talk()

print("\nМою зверюшку зовут", end=" ")
print(crit.name)
print( "\nПробую изменить имя зверюшки на Мурзик")
crit.name = "Мурзик"
print("Moю зверюшку зовут", end= " ")
print(crit.name)
#Появится текст "Мою зверюшку зовут Мурзик".
#Теперь предприму попытку заменить имя зверюшки на пустую строку:
print("\nПробую изменить имя зверюшки на пустую строку")
crit.name = ""
print("Мою зверюшку зовут", end= " ")
print(crit.name)

input("\n\nНажмите Eпter. чтобы выйти.")
#Компьютер скажет нам. что имя зверька - все еще Мурзик.
