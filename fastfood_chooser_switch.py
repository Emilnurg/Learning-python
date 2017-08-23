# Фастфуд-2
# Демонстрирует переключатель

from tkinter import *

class Application(Frame):
    """GUI-приложение, позволяющее выбрать один любимый фастфуд"""
    def __init__(self, master):
        """Инициализирует рамку"""
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Создает элементы. с помощью которых пользователь будет выбирать"""
        # метка-описание
        Label(self,  # c Label не связана никакая переменная, потому что итак по умолчанию
              text = "Выбирете любимый фастфуд"
              ).grid(row = 0, column = 0, sticky = W)
        # метка-инструкция
        Label(self,
              text = "Выберете продукт повреднее: )"
              ).grid(row = 1, column = 0, sticky = W)
        
        # переменная для хранения сведений о единственном любимом жанре
        self.favorite = StringVar() # StringVar() - переключатель
        self.favorite.set(None) #с помощью метода set() установлю начальное значение None 

        # положение "Бигмак" переключателя
        Radiobutton(self,
                    text = "Биг-мак",
                    variable = self.favorite,
                    value = "биг-мак", 
                    command = self.update_text # при (де)активации вызывается update_text
                    ).grid(row = 2, column = 0, sticky = W)

        # положение "Фри" переключателя
        Radiobutton(self,
                    text = "Kартофель-фри",
                    variable = self.favorite,
                    value = "kартофель-фри",
                    command = self.update_text # при (де)активации вызывается update_text
                    ).grid(row = 3, column = 0, sticky = W)
        # положение "Кола" переключателя
        Radiobutton(self,
                    text = "Kола",
                    variable = self.favorite,
                    value = "kола",
                    command = self.update_text # при (де)активации вызывается update_text
                    ).grid(row = 4, column = 0, sticky = W)

        self.results_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)


    def update_text(self):
        """Обновляя текстовую область. вписывает в нее любимый жанр"""
        message = "Ваша любимая еда - "
        message += self.favorite.get()
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)

# основная часть
root = Tk()
root.title("Фастфуд 2.0")
root.geometry("600x300")
app = Application(root)
root.mainloop()
