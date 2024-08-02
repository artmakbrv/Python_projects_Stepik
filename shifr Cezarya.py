def is_valid_int(num):
    while True:
        if num.isdigit() or (num[0] == "-" and num[1:].isdigit()):
            return int(num)
        else:
            num = input(
                "Ввести можно только одно положительное или отрицательное число: "
            )


def is_valid_str(text):
    while text == "" or text.isspace():
        text = input("Введите хоть какой-нибудь текст! ")
    true_text = ""
    for i in text:
        if i == "ё":
            true_text += "е"
        elif i == "Ё":
            true_text += "Е"
        else:
            true_text += i
    return true_text


def coder_decoder(text, k):
    alpha_ru = [chr(i) for i in range(1072, 1104)]
    alpha_en = [chr(i) for i in range(97, 123)]
    text_Caesar = ""

    for i in text:
        if i.isalpha() and i.lower() in alpha_ru:
            if i.islower():
                text_Caesar += alpha_ru[(alpha_ru.index(i) + k) % 32]
            elif i.isupper():
                text_Caesar += alpha_ru[(alpha_ru.index(i.lower()) + k) % 32].upper()
        elif i.isalpha() and i.lower() in alpha_en:
            if i.islower():
                text_Caesar += alpha_en[(alpha_en.index(i) + k) % 26]
            elif i.isupper():
                text_Caesar += alpha_en[(alpha_en.index(i.lower()) + k) % 26].upper()
        else:
            text_Caesar += i

    return text_Caesar


def start():

    text = is_valid_str(input("Введите текс для шифрования: "))
    k = is_valid_int(input("На какой сдвиг текста шифровать? "))
    print(coder_decoder(text, k))


start()
