#Это я. метка
# Демонстрирует применение меток

from tkinter import *

# создание базового окна

root = Tk()
root.title("Это я, метка")
root.geometry("400x200")

# внутри окна создается рамка для размещения других элементов
app = Frame(root)
app.grid()  # менеджер размещения, позже

# создание метки внутри рамки
lbl = Label(app, text = "Вот она я!")  #рамка арр - родительский элемент относительно метки
lbl.grid()

root.mainloop()
