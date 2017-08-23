# Фастфуд
# Демонстрирует применение флажков

from tkinter import *

class Application(Frame):
    """GUI-приложение, позволяющее выбрать любимый фастфуд"""
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
              text = "Выберете продукты повреднее :)"
              ).grid(row = 1, column = 0, sticky = W)


        # создаем BooleanVar флажок "Биг-мак"
        self.likes_bigmac = BooleanVar()
        # сам флажок
        Checkbutton(self,
                    text = "Биг-мак",
                    variable = self.likes_bigmac,
                    command = self.update_text # при (де)активации вызывается update_text
                    ).grid(row = 2, column = 0, sticky = W)

        # флажок "картофель-фри"
        self.likes_free = BooleanVar()
        Checkbutton(self,
                    text = "картофель-фри",
                    variable = self.likes_free,
                    command = self.update_text # при (де)активации вызывается update_text
                    ).grid(row = 3, column = 0, sticky = W)

        # флажок "кола"
        self.likes_cola = BooleanVar()
        Checkbutton(self,
                    text = "кола",
                    variable = self.likes_cola,
                    command = self.update_text # при (де)активации вызывается update_text
                    ).grid(row = 4, column = 0, sticky = W)

        # текстовая область с результатами
        self.results_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):
        """Обновляет текстовый элемент по мере того. как пользователь выбирает свои любимые"""
        likes = ""
        
        if self.likes_bigmac.get():
            likes += "У вас хороший вкус\n"
        if self.likes_free.get():
            likes += "Картошки много не бывает\n"
        if self.likes_cola():
            likes += "И запить все это"
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, likes)

# основная часть
root = Tk()
root.title("Фастфуд")
app = Application(root)
root.mainloop()
