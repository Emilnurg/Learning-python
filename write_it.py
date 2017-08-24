# Запишем
# Демонстрирует чтение из текстового файла
print("Открываю и закрываю файл.")
text_file = open("write_it.txt", "w")
text_file.write("i feel it coming")
text_file.write("\nthis the perfect time")
text_file.write("\njust a simple touch")
text_file.close()

print("\nЧитaю вновь созданный файл.")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()

print("\nСоздаю текстовый файл методом writelines().")
text_file = open("write_it.txt", "w")
lines = ["just a simple touch",
         "\ni feel it coming"]
text_file.writelines(lines)
text_file.close()
print("\nЧитaю вновь созданный файл.")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()
