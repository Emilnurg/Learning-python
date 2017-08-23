# «Сумасшедшего сказочника»

from tkinter import *

class Application(Frame):
    """GUI-приложение, позволяющее выбрать сказку"""
    def __init__(self, master):
        """Инициализирует рамку"""
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Создает элементы. с помощью которых пользователь будет выбирать"""
        # метка-описание
        Label(self,  # c Label не связана никакая переменная, потому что итак по умолчанию
              text = "Введите данные для создания нового рассказа"
              ).grid(row = 0, column = 0, sticky = W)
        Label(self,  # c Label не связана никакая переменная, потому что итак по умолчанию
              text = "Прилагательное(-ые):"
              ).grid(row = 4, column = 0, sticky = W)
        Label(self,  # c Label не связана никакая переменная, потому что итак по умолчанию
              text = "Часть тела:"
              ).grid(row = 5, column = 0, sticky = W)

        # Имя
        self.nm_lbl = Label(self, text = "Имя человека: ")
        self.nm_lbl.grid(row = 1, column = 0, sticky = W)

        #Ввод имени
        self.nm_ent = Entry(self)  # элемент нового типа - Entry
        self.nm_ent.grid(row = 1, column = 1, sticky = W)
        # Существительное
        self.nn_lbl = Label(self, text = "Существительное во мн.ч.:")
        self.nn_lbl.grid(row = 2, column = 0, sticky = W)
        #Ввод сущ.
        self.nn_ent = Entry(self)  # элемент нового типа - Entry
        self.nn_ent.grid(row = 2, column = 1, sticky = W)
        # Глагол
        self.vrb_lbl = Label(self, text = "Глагол в инфинитиве(что делать?):")
        self.vrb_lbl.grid(row = 3, column = 0, sticky = W)
        #Ввод глагола
        self.vrb_ent = Entry(self)  # элемент нового типа - Entry
        self.vrb_ent.grid(row = 3, column = 1, sticky = W)

        # флажок нетерпеливый
        self.impatient = BooleanVar()
        Checkbutton(self,
                    text = "нетерпеливый",
                    variable = self.impatient,
                    #command = self.update_text
                    ).grid(row = 4, column = 1, sticky = W)

        # флажок радостный
        self.glad = BooleanVar()
        Checkbutton(self,
                    text = "радостный",
                    variable = self.glad,
                    #command = self.update_text
                    ).grid(row = 4, column = 2, sticky = W)

        # флажок пронизывающий
        self.penetrating = BooleanVar()
        Checkbutton(self,
                    text = "пронизывающий",
                    variable = self.penetrating,
                    #command = self.update_text
                    ).grid(row = 4, column = 3, sticky = W)

        # переменная для хранения сведений о выбранной части тела
        self.favorite = StringVar() # StringVar() - переключатель
        self.favorite.set(None) #с помощью метода set() установлю начальное значение None 

        """# положение "Пупок" переключателя
        Radiobutton(self,
                    text = "Пупок",
                    variable = self.favorite,
                    value = "пупок", 
                    #command = self.update_text # при (де)активации вызывается update_text
                    ).grid(row = 5, column = 1, sticky = W)

        # положение "БПН" переключателя
        Radiobutton(self,
                    text = "Большой палец ноги",
                    variable = self.favorite,
                    value = "большой палец ноги",
                    #command = self.update_text # при (де)активации вызывается update_text
                    ).grid(row = 5, column = 2, sticky = W)
        # положение "ПМ" переключателя
        Radiobutton(self,
                    text = "Продолговатый мозг",
                    variable = self.favorite,
                    value = "продолговатый мозг",
                    #command = self.update_text # при (де)активации вызывается update_text
                    ).grid(row = 5, column = 3, sticky = W)"""

        # nереклюЧатель с названиями частей тела
        body_parts = ["пупок", "большой палец ноги", "продолговатый мозг"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                    text = part,
                    variable = self.favorite,
                    value = part,
                    ).grid(row = 5, column = column, sticky = W)
            column += 1

        # кнопка отправки значения
        self.submit_bttn = Button(self, text = "Получить рассказ", command = self.reveal)
        # Активация кнопки command методом reveal() - при вводе верного пароля
        self.submit_bttn.grid(row = 6, column = 0, sticky = W)

        #создание текстовой области. в которую будет выведен ответ (несколько строк)
        self.secret_txt = Text(self,
                               width = 85,
                               height = 10,
                               wrap = WORD)
        # wrap - перенос текста, напечатанного внутри
        # доступные значения - WORD, CHAR и NONE
        # WORD - на новую строку будут переноситься целые слова, заходящие за правую кромку текстовой области.
        # CHAR - посимвольно, NONE - нет переноса
        self.secret_txt.grid(row = 7, column = 0, columnspan = 4)

    def reveal(self):
        """Заполняет текстовую область очередной историей на основе пользовательского
ввода"""
        # Получение  данных из вводимых полей
        name = self.nm_ent.get()
        noun = self.nn_ent.get()
        verb = self.vrb_ent.get()
        adjectives = ""
        if self.impatient.get():
            adjectives += "нетерпеливый, "
        if self.glad.get():
            adjectives += "радостный, "
        if self.penetrating.get():
            adjectives += "пронизывающий, "
        body_part = self.favoritesticky #W.get()


        # соЗдание рассказа
        story = "Знаменитый путешественник "
        story += name
        story += " уже совсем отчаялся довершить дело всей своей жизни - поиск затерянного города, в котором, по легенде, обитали "
        story += noun.title()
        story += ". Но однажды "
        story += noun
        story += " и "
        story += name + " столкнулись лицом к лицу. "
        story += "Мощный, "
        story += adjectives
        story += "ни с чем не сравнимый восторг охватил душу путешественника. "
        story += "После стольких лет поисков цель была наконец достигнута. "
        story += name
        story += " ощутил, как его "
        story += body_part
        story += " промокает от слез. "
        story += "И тут внезапно "
        story += noun
        story += " перешли в атаку, и "
        story += name
        story += " был ими мгновенно сожран. "
        story += "Мораль? Если задумали "
        story += verb
        story += " - надо делать это с осторожностью."

        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, story)
        
        
        
        

        

        
        

        













# основная часть
root = Tk()
root.title("CУМАСШЕДШИЙ СКАЗОЧНИК")
#root.geometry("600x300")
app = Application(root)
root.mainloop()
