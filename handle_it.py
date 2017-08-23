# Обработаем
# Демонстрирует обработку исключительных ситуаций
# try/except
try:
    num = float(input("Bвeдитe число: "))
except ValueError:
    print("Пoxoжe, это не число!")

print()
for value in (None, "Привет!"):
    try:
        print("Пытаюсь преобразовать в число: ", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Я умею преобразовывать только строки и числа!")
    except ValueError as e:
        print("Я умею преобразовывать только строки. составленные из цифр!")
        print(e)
