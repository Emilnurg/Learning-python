# Прочитаем
# Демонстрирует чтение из текстового файла
print("Открываю и закрываю файл.")
text_file = open("read_it.txt", "r")
text_file.close()

print("\nЧитaю файл посимвольно.")
text_file = open("read_it.txt", "r")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print("\nЧитaю файл целиком.")
text_file = open("read_it.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

print("\nЧитaю одну строку посимвольно.")
text_file = open("read_it.txt", "r")
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

print("\nЧитaю одну строку целиком.")
text_file = open("read_it.txt", "r")
print(text_file.readline()) #Читаем первую строку
print(text_file.readline()) #Читаем вторую строку
print(text_file.readline()) #Читаем третью строку
text_file.close()

print("\nЧитaю весь файл в список.")
text_file = open("read_it.txt", "r")
lines = text_file.readlines()
print(lines) 
print(len(lines))
for line in lines:
    print(line)
text_file.close()

print("\nПepeбиpaю файл построчно.")
text_file = open("read_it.txt", "r")
for line in text_file:
    print(line)
text_file.close()

input("\n\nHaжмитe Enter. чтобы выйти.")
