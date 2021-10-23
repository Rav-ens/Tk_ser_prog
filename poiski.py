from tkinter import *
import tkinter as tk

from tkinter import ttk
from tkinter import messagebox as mb


class Poisk:

    def __init__(self, parent, width=10000, height=20000, title="MyWindow", resizable=(True, True), icon=None):
        self.rel = ['loh']

        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.resizable(resizable[0], resizable[1])
        self.poi = Button(self.root, text='Найти', width=6, command=self.hol, font='TimesNewRoman 14')
        self.poi.grid(column=0, row=1, sticky=W)
        self.delobj = Entry(self.root, width=20, font='TimesNewRoman 14')
        self.delobj.grid(column=0, row=0, sticky=EW)

        if icon:
            self.root.iconbitmap(icon)
        self.grab_focus()

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()

    def loh(self):
        addto = 0
        world_base = []
        x = 0
        g = 0
        result = []
        line_base = []

        base = open('data.txt', 'r')

        for line in base:
            line_base += line.split('\n')
            x += 1

        for _ in range(len(line_base)):
            world_base += line_base[_].split(';')

        for _ in range(1, int((len(world_base) - x) / 10)):
            world_base.pop(_ * 10)

        h = 1
        for _ in range(x):
            addto = [h]
            addto += [world_base[_ * 10 + g]]
            g += 1
            addto += [world_base[_ * 10 + g]]
            g += 1
            addto += [world_base[_ * 10 + g]]
            g += 1
            addto += [world_base[_ * 10 + g]]
            g += 1
            addto += [world_base[_ * 10 + g]]
            g += 1
            addto += [world_base[_ * 10 + g]]
            g += 1
            addto += [world_base[_ * 10 + g]]
            g += 1
            addto += [world_base[_ * 10 + g]]
            g += 1
            addto += [world_base[_ * 10 + g]]
            g += 1
            addto += [world_base[_ * 10 + g]]
            g = 0
            result += [addto]
            h += 1
        addto += [world_base[-1]]

        result += [addto]
        del result[-1][0]
        self.rel = result

    def entry(self):
        base = open('data.txt', 'r')
        z = 0
        c = 2
        sf = self.delobj.get()
        self.delobj.destroy()
        self.poi.destroy()
        for line in base:
            if sf in line:
                Label(self.root, text=line, wraplength=1000, font='TimesNewRoman 14')\
                    .grid(column=0, row=c, sticky=W)
                c += 1
                z = 1
        if z == 0:
            mb.showwarning('warning', 'НИЧЕГО НЕ НАЙДЕНО')
            self.root.destroy()

    def hol(self):
        self.loh()
        kj = 0
        columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11')
        trees = ttk.Treeview(self.root, columns=columns, show='headings')

        style = ttk.Style(self.root)
        style.configure("Treeview", rowheight=30, font=('Calibre', 13, 'bold'))
        trees.configure(style="Treeview")

        trees.heading('#1', text='ids')
        trees.heading('#2', text='Имя на русском')
        trees.heading('#3', text='Имя на англ.')
        trees.heading('#4', text='Студия')
        trees.heading('#5', text='Год выпуска')
        trees.heading('#6', text='Год конца')
        trees.heading('#7', text='сезоны')
        trees.heading('#8', text='серии')
        trees.heading('#9', text='Жанры')
        trees.heading('#10', text='Актеры')
        trees.heading('#11', text='страна')
        contacts = []

        c = self.delobj.get()
        for z in range(1, 11):
            for i in range(len(self.rel)):
                if c in self.rel[i][z]:
                    if self.rel[i] in contacts:
                        print('повтор')
                    else:
                        contacts.append(self.rel[i])
                        kj = 1

        for contact in contacts:
            trees.insert('', tk.END, values=contact)

        trees.column("#1", width=30)
        trees.column("#5", width=50)
        trees.column("#6", width=50)
        trees.column("#7", width=50)
        trees.column("#8", width=50)
        trees.column("#11", width=110)
        if kj == 1:
            trees.grid(column=0, row=4)
        else:
            mb.showwarning('warning', 'НИЧЕГО НЕ НАЙДЕНО')
            self.root.destroy()
