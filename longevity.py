# Долгожитель
# Демонстрирует текстовое поле. текстовую область и менеджер размещения Grid

from tkinter import *

class Application(Frame):
    """GUI-приложение, владеющее секретом долголетия"""
    def __init__(self, master):
        """Инициализирует рамку"""
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Создает кнопку, текстовое поле и текстовую область"""
        # метка-инструкция
        self.inst_lbl = Label(self, text = "Чтобы узнать секрет допголетия. введите пароль")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        # row - cтрока
        # column - cтолбец
        # columnspan - «растягивает» элемент по горизонтали, помещая его более чем в один столбец.
        # rowspan - «растянуть» элемент по вертикали)
        # sticky - выровнять его внутри ячейки(W E S N - cтороны света)

        self.pw_lbl = Label(self, text = "Пароль: ")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)
        # метка около поля ввода пароля
        
        
        # текстовое поле для ввода пароля (одна строка)
        self.pw_ent = Entry(self)  # элемент нового типа - Entry
        self.pw_ent.grid(row = 1, column = 1, sticky = W)

        # кнопка отправки значения
        self.submit_bttn = Button(self, text = "Узнать секрет", command = self.reveal)
        # Активация кнопки command методом reveal() - при вводе верного пароля
        self.submit_bttn.grid(row = 2, column = 1, sticky = W)


        #создание текстовой области. в которую будет выведен ответ (несколько строк)
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        # wrap - перенос текста, напечатанного внутри
        # доступные значения - WORD, CHAR и NONE
        # WORD - на новую строку будут переноситься целые слова, заходящие за правую кромку текстовой области.
        # CHAR - посимвольно, NONE - нет переноса
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)


    def reveal(self):
        """В зависимости от введенного пароля отвечает разными сообщениям"""
        contents = self.pw_ent.get() # метод get() экземпляра Entry (ввода пароля)
        # get() - метод, возвращает текстовое содержимое элемента.
        if contents == "secret":
            message = "Чтобы дожить до 100 лет. надо сначала дожить до 99," \
            " а потом вести себя ОЧЕНЬ осторожно."
        else:
            message = "Вы ввели неправильный пароль. так что я не могу " \
            "поделиться тайной с вами."

        self.secret_txt.delete(0.0, END)
        # delete() - удаляет любое содержимое,ранее существовавшее внутри указанного элемента
        # 0.0 - строка и столбец, с которого все удалять(т.е. с самого начала)
        # END - конец текста(удалять до конца)

        self.secret_txt.insert(0.0, message)
        # insert() - вставляет строку в текстовый элемент
        # Метод insert() не заменяет текст в текстовых элементах, а только добавляет его

# основная часть
root = Tk()
root.title("Долгожитель")
root.geometry("600x300")

app = Application(root)
root.mainloop()

