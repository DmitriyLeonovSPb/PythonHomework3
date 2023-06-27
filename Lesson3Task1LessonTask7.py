UserInput = str(input("Введите строку символов: "))
CountBook = {}
for i in UserInput:
    CountBook[i] = CountBook.get(i, 0) + 1
print(CountBook)