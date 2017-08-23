# Виселица
#
#Классическая игра "Виселица". Компьютер случайным образом выбирает слово.
#которое игрок должен отгадать буква за буквой. Если игрок не сумеет
# отгадать за отведенное количество попыток. на экране появится фигурка повешенного.
# импорт модуля

import random

# константы
HANGMAN = (
    """
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
 --------
 """,
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
 --------
""",
"""
 ------
 |    |
 |    O
 |  /-:-/
 |
 |
 |
 |
 |
 --------
""",
"""
 ------
 |    |
 |    O
 |  /-:-/
 |    :
 |
 |
 |
 |
 --------
""",
"""
 ------
 |    |
 |    O
 |  /-:-/
 |    :
 |    :
 |
 |
 |
 --------
""",
"""
 ------
 |    |
 |    O
 |  \-:-/
 |    :
 |    :
 |   / /
 |
 |
 --------
""",
"""
 ------
 |    |
 |    O
 |  /-:-/
 |    :
 |    :
 |   / /
 |  |  |
 |
 --------
""", 
"""
 ------
 |    |
 |    O
 |  /-:-/
 |    :
 |    :
 |   / / 
 |  |  |
 |  |  |
 --------
""")

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("БЕЛКА", "ФУТБОЛ", "ДИВАН", "ПИТОН", "АЙФОН", "АНДРОИД")
word = random.choice(WORDS)
wrong = 0
used = []
so_far = "-" * len(word)

print("Дoбpo пожаловать в игру 'Виселица'. Удачи вам!")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nBы уже предлагали следующие буквы:\n", used)
    print("\nОтгаданное вами в слове сейчас выглядит так:\n", so_far)

    guess = input("\n\nВведите букву: ")
    guess = guess.upper()
    while guess in used:
        print("Вы уже предлагали букву", guess)
        guess = input("\n\nВведите букву: ")
        guess = guess.upper()
    used.append(guess)
    if guess in word:
        print("\nЙохоу! Буква ", guess, "есть в слове!")
        # новая строка "--------" so_far с отгаданной буквой/ами
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nЕще пара таких ", guess, " и его точно повесят")
        wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nD=Вы повешены(((")
else:
    print("\nУрааа отгадали!!")
print("\nЭто было слово ", word)
input("\n\nНажмите Enter для выхода из игры")
