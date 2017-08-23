from tkinter import *

class Application(Frame):
    """GUI-приложение с тремя кнопками"""
    def __init__(self, master):
        """Инициализирует рамку"""
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.bttn_clicks = 0
        self.efficient = 100

    def create_widgets(self):
        """Создает три бесполезные кнопки"""
        # первая кнопка
        self.bttn = Button(self,text = "Рассчитать")
        self.bttn.grid(row = 0, column = 0, columnspan = 3, sticky = W)
        self.bttn["command"] = self.update_count
        #self.bttn["command"] = self.unefficent
        # вторая кнопка
        self.bttn = Button(self)
        self.bttn.grid(row = 1, sticky = E)
        self.bttn.configure(text = "Сделать")
        self.bttn["command"] = self.update_count
        # третья кнопка
        self.bttn = Button(self)
        self.bttn.grid(row = 2, column = 0, columnspan = 1, sticky = W)
        self.bttn["command"] = self.update_count
        self.bttn["text"] = "Указать"
        # вторая кнопка
        self.bttn = Button(self)
        self.bttn.grid(row = 3, sticky = E)
        self.bttn.configure(text = "Принести")
        self.bttn["command"] = self.update_count
        # вторая кнопка
        self.bttn = Button(self)
        self.bttn.grid(row = 4, sticky = W)
        self.bttn.configure(text = "Отдать")
        self.bttn["command"] = self.update_count
        # вторая кнопка
        self.bttn = Button(self)
        self.bttn.grid(row = 5, sticky = E)
        self.bttn.configure(text = "Оформить")
        self.bttn["command"] = self.update_count
        
       # Имя
        self.nm_lbl = Label(self)
        self.nm_lbl.grid(row = 6, column = 0, sticky = W)

        # Имя
        self.nn_lbl = Label(self)
        self.nn_lbl.grid(row = 9, column = 0, sticky = W)

        # Имя
        self.nt_lbl = Label(self, text = "Выполнено приказов: 0")
        self.nt_lbl.grid(row = 7, column = 0, sticky = W)

    def update_count(self):
        """Увеличивает количество нажатий на единицу и отображает его"""
        self.bttn_clicks += 1
        self.nm_lbl["text"] = "Приказаний отдано: " + str(self.bttn_clicks)
        #for(self.bttn_clicks>0):
         #   self.efficent -= 1
          #  self.nn_lbl["text"] = "Эффективность в процентах" + str(self.efficient)

    def unefficient(self):
        #if self.bttn_clicks > 3:
        self.efficent -= 1
        self.nn_lbl["text"] = "Эффективность в процентах" + str(self.efficient)


    """def unefficent(self):
        self.bttn_clicks += 1
        self.efficent -= 1
        self.nn_lbl["text"] = "Эффективность в процентах" + str(self.efficient)
        self."""

# основная часть
root = Tk()
root.title("КВЗ")
root.geometry("300x400")

app = Application(root)
root.mainloop()

                
