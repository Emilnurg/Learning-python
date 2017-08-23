# Счетчик щелчков
# Демонстрирует связывание событий с обработчиками

from tkinter import *

class Application(Frame):
    """GUI-приложение, которое подсчитывает количество нажатий кнопки"""
    def __init__(self, master):
        """Инициализирует рамку"""
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.bttn_clicks = 0 # добавляется счетчик щелчков

    def create_widgets(self):
        """Создает кнопку. на которой отображается
            количество совершенных нажатий"""
        self.bttn = Button(self)
        self.bttn.grid()
        self.bttn["text"] = "Количество щелчков: 0"
        self.bttn["command"] = self.update_count
        # я "связал событие (нажатие кнопки) с обработчиком
        # события (методом update count() ). Параметр command
        # любого элемента управления вообще предназначен для того,
        # чтобы при его активизации вызывать метод-обработчик.

    def update_count(self):
        """Увеличивает количество нажатий на единицу и отображает его"""
        self.bttn_clicks += 1
        self.bttn["text"] = "Количество щелчков: " + str(self.bttn_clicks)

# основная часть
root = Tk()
root.title("Количество щелчков")
root.geometry("400x200")

app = Application(root)
root.mainloop()
        
