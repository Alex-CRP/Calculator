import pathlib
import tkinter.ttk
from tkinter.ttk import Progressbar
from tkinter import *
from tkinter import scrolledtext, messagebox, ttk, filedialog


def clicked():
    res = "Привет {}".format(txt.get())
    lbl.configure(text=res)

window = Tk()
window.geometry("1200x400")
window.title("Добро пожаловать!")
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Первая")
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="ЫЫЫЫЫЫ")
tab_control.pack(expand=1, fill='both')
combo = tkinter.ttk.Combobox(tab1)
chk_state = BooleanVar()
chk_state.set(True) # задайте проверку состояния чекбокса
chk = Checkbutton(tab1, text="Выбрать", onvalue=chk_state, padx=100, pady=50)
chk.grid(column=0, row=0)
combo["values"] = (1,2,3,4,5, 'Текст')
combo.current(1)
combo.grid(column=0, row=1)
# lbl = Label(window, text="Hi", font=("Times new Roman", 50))
# lbl.grid(column=0, row=3)
# btn = Button(window, text="Кликай!", bg="black", fg='red',command=clicked).grid(column=1, row=0)
# txt = Entry(window, width=10)
# txt.focus()
# txt.grid(column=2,row=0)
# rad1 = Radiobutton(window,text='Первый', value=1)
# rad2 = Radiobutton(window,text='Второй', value=2)
# rad3 = Radiobutton(window,text='Третий', value=3)
# rad1.grid(column=4,row=0)
# rad2.grid(column=4,row=1)
# rad3.grid(column=4,row=2)
# scr_text = scrolledtext.ScrolledText(window, width=40, height=10)
# scr_text.grid()
# scr_text.insert(INSERT, lbl)
# scr_text.delete(1.0, END)
# # messagebox.askyesno("Заголовок", "Текст")
# # messagebox.askquestion("Заголовок", "Текст")
# var = IntVar()
# var.set(5)
# spin = Spinbox(window, from_=0,to=300, width=5,  textvariable=var).grid(column=4, row=3)
# style = ttk.Style()
# style.theme_use('default')
# style.configure('black.Horizontal.TProgressbar', background='black')
# bar = Progressbar(window, length=200, value=70, style='black.Horizontal.TProgressbar')
# bar.grid(column=3, row=5)
# bar["value"] = 70
# # file = filedialog.askopenfilename(initialdir=r'/home/zhandrov/Desktop')
# new_item = Menu(window, tearoff=0)
# new_item.add_command(label="Новый")
# menu =  Menu(window)
#
# hi = Menu(window, tearoff=0)
# hi.add_command(label="Хай :)")
# hi.add_command(label="Я ПОНЯЛ!")
#
# menu.add_cascade(label="Файл", menu=hi)
# new_item.add_separator()
# new_item.add_command(label='Изменить')
# window.config(menu=menu)
# menu.add_cascade(label="Автор", menu=new_item)


window.mainloop()
