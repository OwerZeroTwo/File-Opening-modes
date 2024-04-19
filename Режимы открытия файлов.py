# Чтение и вывод содержимого текстового файла
with open("poem.txt", "r", encoding="utf-8") as file:
    print(file.read())