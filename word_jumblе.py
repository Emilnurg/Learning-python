# Анаrраммы (Word JumЬle)
#
# Компьютер выбирает какое-пибо слово и хаотически переставляет его буквы
# Задача иrрока - восстановить исходное слово

import random
print("Добро пожаловать в игру 'Анаграммы'!")
print("Надо переставить буквы так, чтобы получилось осмысленное слово")
print("Для выхода нажмите Enter, не вводя своей версии.")
WORDS = ("масленица", "игра", "сон", "параллелограмм", "dream", "белка",
         "сбербанк", "тупик", "деградация", "месси")

#high = len(words)-1
#younumber = random.randint(1, high)
#youword = words[younumber]

youword = random.choice(WORDS)
right = youword

anagram = ""
while youword != "":
    #high_word = len(youword)
    #position = random.randint(0, high_word) - 1
    position = random.randrange(len(youword))
    anagram += youword[position]
    youword = youword[:position] + youword[(position + 1):]
print("Вот анаграмма: ", anagram)

guess = input("\nПопоробуйте отгадать исходное слово: ")
while guess != right and guess != "":
    print("Вы неправы")
    guess = input("\nПопоробуйте отгадать исходное слово: ")
if guess == right:
        print("Йо хо хо! Верно!")

print("Cnacибo за игру.")
input("\n\nHaжмитe Enter. чтобы выйти.")

