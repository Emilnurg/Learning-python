"""
# Случайные буквы
# Демонстрирует индексацию строк

import random
word = "гравитация"
print ("В переменной word хранится слово: ", word, "\n")
high = len(word)
low = -len(word)
for i in range(20):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])
input("\n\nHaжмитe Enter. чтобы выйти.")
"""
"""
#no_vowels.ру

# Только согласные
#Демонстрирует. как создавать новые строки из исходных с помощью цикла for

message = input("Введите текст: ")
new_message = ""
VOWELS = "аеёиоуыэюя"
print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("Создана новая строка: ", new_message)
print("\nBoт ваш текст с изъятыми гласными буквами:", new_message)
input("\n\nHaжмитe Enter. чтобы выйти.")
"""

# pizza_slicer.ру

# Резчик пиццы
# Демонстрирует срезы строк

word = "пицца"
print( """

Памятка
0   1   2   3   4   5
+---+---+---+---+---+
| п | и | ц | ц | а |
+---+---+---+---+---+
-5 -4  -3  -2  -1
""")

print("Введите начальный и конечный индексы для того среза 'пиццы'. который хотите \
получить.")
print("Для выхода нажмите Enter. не вводя начальную позицию . ")
start = None
while start != "":
      start = (input("\nНачальная позиция: "))
      if start:
          start = int(start)
          finish = int(input("Koнeчнaя позиция: "))
          print("Cpeз word[", start, ":", finish, "] выглядит как", end=" ")
          print(word[start:finish])
input("\n\nHaжмитe Enter. чтобы выйти.")
