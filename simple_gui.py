# Простейший GUI
# Демонстрирует создание окна

from tkinter import *

# создание базового окна
root = Tk()

# изменение окна
root.title("Простейший GUI")
root.geometry("1920x1080")

# старт событийного цикла
root.mainloop()
