from tkinter import *
from tkinter import messagebox as mb


class Appen:

    def __init__(self, parent, width=400, height=400, title="MyWindow", resizable=(True, True), icon=None):
        self.root = Toplevel(parent)
        self.root.title(title)
        #self.root.geometry(f"{width}x{height}+200+200")
        #self.root.config(bg='#E1D5C5')
        self.delobj = Entry(self.root)
        self.delobj1 = Entry(self.root)
        self.delobj2 = Entry(self.root)
        self.delobj3 = Entry(self.root)
        self.delobj4 = Entry(self.root)
        self.delobj5 = Entry(self.root)
        self.delobj6 = Entry(self.root)
        self.delobj7 = Entry(self.root)
        self.delobj8 = Entry(self.root)
        self.delobj9 = Entry(self.root)

        self.f = 0
        self.f1 = 0
        self.f2 = 0
        self.f3 = 0
        self.f4 = 0
        self.f5 = 0
        self.f6 = 0
        self.f7 = 0
        self.f8 = 0
        self.f9 = 0

        self.root.resizable(resizable[0], resizable[1])
        Button(self.root, text='Добавить', command=self.entry, font=('TimesNewRoman', 14))\
            .grid(column=1, row=10, sticky=EW)
        self.vvod()
        if icon:
            self.root.iconbitmap(icon)
        self.grab_focus()

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()

    def exit(self):
        self.root.destroy()

    def entry(self):
        self.get()
        d = f'{self.f}; {self.f1}; {self.f2}; {self.f3}; {self.f4}; {self.f5}; {self.f6}; {self.f7}' \
            f'; {self.f8}; {self.f9}.\n'
        sf = d
        if mb.askyesno('xz', f'добавить {d}'):
            f = open('data.txt').readlines()
            f.insert(-2, sf)
            with open('data.txt', 'w') as F:
                F.writelines(f)
            mb.showinfo('info', 'Успешно добавлено')
        self.exit()

    def vvod(self):

        self.lbl()
        self.delobj = Entry(self.root, width=20, font='TimesNewRoman 14')
        self.delobj.grid(column=1, row=0, sticky=W, padx=5, pady=7)
        self.delobj1 = Entry(self.root, width=20, font='TimesNewRoman 14')
        self.delobj1.grid(column=1, row=1, sticky=W, padx=5, pady=7)
        self.delobj2 = Entry(self.root, width=20, font='TimesNewRoman 14')
        self.delobj2.grid(column=1, row=2, sticky=W, padx=5, pady=7)
        self.delobj3 = Entry(self.root, width=20, font='TimesNewRoman 14')
        self.delobj3.grid(column=1, row=3, sticky=W, padx=5, pady=7)
        self.delobj4 = Entry(self.root, width=20, font='TimesNewRoman 14')
        self.delobj4.grid(column=1, row=4, sticky=W, padx=5, pady=7)
        self.delobj5 = Entry(self.root, width=20, font='TimesNewRoman 14')
        self.delobj5.grid(column=1, row=5, sticky=W, padx=5, pady=7)
        self.delobj6 = Entry(self.root, width=20, font='TimesNewRoman 14')
        self.delobj6.grid(column=1, row=6, sticky=W, padx=5, pady=7)
        self.delobj7 = Entry(self.root, width=20, font='TimesNewRoman 14')
        self.delobj7.grid(column=1, row=7, sticky=W, padx=5, pady=7)
        self.delobj8 = Entry(self.root, width=20, font='TimesNewRoman 14')
        self.delobj8.grid(column=1, row=8, sticky=W, padx=5, pady=7)
        self.delobj9 = Entry(self.root, width=20, font='TimesNewRoman 14')
        self.delobj9.grid(column=1, row=9, sticky=W, padx=5, pady=7)

    def get(self):
        self.f = self.delobj.get()
        self.f1 = self.delobj1.get()
        self.f2 = self.delobj2.get()
        self.f3 = self.delobj3.get()
        if self.delobj4.get():
            self.f4 = self.delobj4.get()
        else:
            self.f4 = ' - '
        self.f5 = self.delobj5.get()
        self.f6 = self.delobj6.get()
        self.f7 = self.delobj7.get()
        self.f8 = self.delobj8.get()
        self.f9 = self.delobj9.get()

    def lbl(self):
        Label(self.root, text="Название на русском", font='TimesNewRoman 14')\
            .grid(column=0, row=0, sticky=W, padx=5, pady=7)
        Label(self.root, text="Назание на английском", font='TimesNewRoman 14')\
            .grid(column=0, row=1, sticky=W, padx=5, pady=7)
        Label(self.root, text="Издатель", font='TimesNewRoman 14').grid(column=0, row=2, sticky=W, padx=5, pady=7)
        Label(self.root, text="Когда началось", font='TimesNewRoman 14')\
            .grid(column=0, row=3, sticky=W, padx=5, pady=7)
        Label(self.root, text="Когда закончилось", font='TimesNewRoman 14')\
            .grid(column=0, row=4, sticky=W, padx=5, pady=7)
        Label(self.root, text="Кол-во сезонов", font='TimesNewRoman 14').grid(column=0, row=5, sticky=W, padx=5, pady=7)
        Label(self.root, text="Кол-во серий", font='TimesNewRoman 14').grid(column=0, row=6, sticky=W, padx=5, pady=7)
        Label(self.root, text="Жанры", font='TimesNewRoman 14').grid(column=0, row=7, sticky=W, padx=5, pady=7)
        Label(self.root, text="Актеры", font='TimesNewRoman 14').grid(column=0, row=8, sticky=W, padx=5, pady=7)
        Label(self.root, text="Страна выпуска", font='TimesNewRoman 14').grid(column=0, row=9, sticky=W, padx=5, pady=7)
