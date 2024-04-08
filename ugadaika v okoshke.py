import tkinter as tk

from tkinter import Tk, ttk

import random


def provernum():

    try:

        user_num = int(textnums.get())

        if user_num <= 0 or user_num > 100:

            otvet = "Число не в интервале от 0 до 100"

        elif user_num == nums:

            otvet = "Вы угадали, поздравляем!"

        elif user_num > nums:

            otvet = "Слишком много, попробуйте еще раз"

        elif user_num < nums:

            otvet = "Слишком мало, попробуйте еще раз"

        else:

            otvet = "Что-то не то"

    except:

        otvet = "Это не число!"

    lotvet.config(text=otvet)


nums = random.randint(1, 100)


textnum = ""


window = tk.Tk()

window.title("Игра, угадайка")

window.geometry("450x130")

lnum = ttk.Label(window, text="Введите число от 1 до 100:")

lnum.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)


textnums = ttk.Entry(window, textvariable=textnum)

textnums.grid(column=1, row=0, sticky=tk.E, padx=10, pady=10)


lotvet = ttk.Label(window)


proverka = ttk.Button(window, text="Проверка")

proverka.config(command=provernum)

proverka.grid(column=1, row=1, sticky=tk.W, padx=10, pady=10)

proverka.focus()


lotvet.grid(column=0, row=2, columnspan=3, sticky=tk.W, padx=10, pady=10)


butquit = ttk.Button(window, text="Выход", command=lambda: window.quit())

butquit.grid(column=2, row=1, sticky=tk.SE, padx=10, pady=10)


window.mainloop()
