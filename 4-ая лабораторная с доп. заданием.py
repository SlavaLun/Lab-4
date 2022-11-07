from tkinter import *
from PIL import Image
import pygame
from random import *

list_of_random = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V',
                  'X', 'Y', 'Z', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
root = Tk()
root.title('4-ая Лабораторная')
root.geometry('800x700')
root.resizable(True, True)
file = "hollow knight.gif"

info = Image.open(file)
frames = info.n_frames  # Считывание количества кадров гиф изображения

im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]
slovo = StringVar()

count = 0
anim = None
pygame.mixer.init()


def play():  # Функция запуска песни
    pygame.mixer.music.load('hollow knight.mp3')
    pygame.mixer.music.play(loops=10)


def stop_music():  # Функция остановки песни
    pygame.mixer.music.stop()


def animation(count):  # Функция запуска гифки
    global anim
    im2 = im[count]
    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(200, lambda: animation(count))


def stop_animation():  # Функция остановки гифки
    global anim
    root.after_cancel(anim)


def change_button():  # Замена кнопки старт на кнопку стоп
    start.destroy()
    stop = Button(root, text="stop", command=lambda: [stop_animation(), stop_music(), change_second_button()])
    stop.place(x=750, y=670, width=50, height=30)


def change_second_button():  # Замена кнопки стоп на кнопку старт
    stop.destroy()
    start = Button(root, text="start", command=lambda: [animation(count), play(), change_button()])
    start.place(x=750, y=670, width=50, height=30)


def new_button():  # Создание поля для ввода чисел и кнопку активации программы
    txt = Entry(root, textvariable=slovo)
    txt.place(x=250, y=150, width=300, height=30)
    Click = Button(root, text="click", command=lambda: random_password(txt))
    Click.place(x=375, y=200, width=50, height=30)


def random_password(txt):  # Генерация ключа с выводом его на экран, создание кнопки повтора
    A = str(slovo.get())
    if len(A) == 3:
        x = sample(list_of_random, 5)
        s = ''
        for i in range(len(x)):
            s += str(x[i])
        A1 = int(A[0])
        A2 = int(A[1])
        A3 = int(A[2])
        s1 = s + s + s + s + s
        s2 = s
        if A1 == 0:
            s2 += ' ' + s1[0: 4:]
        else:
            s2 += ' ' + s1[A1-1:A1+3]
        if A2 == 0:
            s2 += ' ' + s1[0:3:]
        else:
            s2 += ' ' + s1[A2:A2 + 3:]
        if A3 == 0:
            s2 += ' ' + s1[0:2:]
        else:
            s2 += ' ' + s1[A3 - 1:A3 + 1:]
        Click.destroy()
        txt.destroy()
        login = Label(root, text=s2)
        login.place(x=250, y=150, width=300, height=30)
        Again = Button(root, text="try again", command=lambda: try_again(login))
        Again.place(x=375, y=200, width=50, height=30)
        slovo.set('')
        return login
    elif len(A) > 3 or len(A) < 3:
        login = Label(root, text="Недопустимое количество символов")
        login.place(x=250, y=150, width=300, height=30)
        Again = Button(root, text="try again", command=lambda: try_again(login))
        Again.place(x=375, y=200, width=50, height=30)
        slovo.set('')


def try_again(login):  # Удаление сгенерируемого кода и кнопки повтора, создание поля для ввода, кнпоки начало алгоритма
    login.destroy()
    Again.destroy()
    txt = Entry(root, textvariable=slovo)
    txt.place(x=250, y=150, width=300, height=30)
    Click = Button(root, text="click", command=lambda: random_password(txt))
    Click.place(x=375, y=200, width=50, height=30)


gif_label = Label(root, image="")  # Открытие гифки
gif_label.pack()

start = Button(root, text="start", command=lambda: [animation(count), play(), change_button(), new_button()])
start.place(x=375, y=150, width=50, height=30)
Click = Button(root, text="click", command=lambda: random_password(txt))
Again = Button(root, text="try again", command=lambda: try_again(login))
stop = Button(root, text="stop", command=lambda: [stop_animation(), stop_music(), change_second_button()])
txt = Entry(root, textvariable=slovo)
login = Label(root, text='')

root.mainloop()
