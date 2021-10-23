from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb


class Filter:

    def __init__(self, parent, width=1400, height=1400, title="MyWindow", resizable=(True, True), icon=None):

        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.resizable(resizable[0], resizable[1])

        self.fram1 = Frame(self.root)
        self.fram2 = Frame(self.root)
        self.fram3 = Frame(self.root)
        self.fram4 = Frame(self.root)
        self.fram5 = Frame(self.root)
        self.fram6 = Frame(self.root)
        self.fram7 = Frame(self.root)
        self.fram8 = Frame(self.root)
        self.fram9 = Frame(self.root)
        self.fram10 = Frame(self.root)

        self.lbl = 0
        self.ckog = Entry(self.root)
        self.rel = 'gh'
        self.pokog = Entry(self.root)

        self.cco = Entry(self.fram6, font=('Calibre', 13, 'bold'))
        self.cakt = Entry(self.fram6, font=('Calibre', 13, 'bold'))
        self.cja = Entry(self.fram6, font=('Calibre', 13, 'bold'))
        self.posis = Entry(self.fram6, font=('Calibre', 13, 'bold'))
        self.csis = Entry(self.fram6, font=('Calibre', 13, 'bold'))
        self.poser = Entry(self.fram6, font=('Calibre', 13, 'bold'))
        self.cser = Entry(self.fram6, font=('Calibre', 13, 'bold'))
        self.pokogk = Entry(self.fram6, font=('Calibre', 13, 'bold'))
        self.ckogk = Entry(self.fram6, font=('Calibre', 13, 'bold'))
        self.pokogn = Entry(self.fram6, font=('Calibre', 13, 'bold'))
        self.ckogn = Entry(self.fram6, font=('Calibre', 13, 'bold'))

        self.chebn()

        self.chgn = False
        self.chgk = False
        self.chser = False
        self.chsis = False
        self.chakt = False
        self.chja = False
        self.chco = False

        self.loh()
        if icon:
            self.root.iconbitmap(icon)
        self.grab_focus()

    def chebn(self):
        h = 0
        if True:
            self.gn()
            self.chgn = True
            h = 1
        if True:
            self.chgk = True
            self.gk()
            h = 1
        if True:
            self.ser()
            self.chser = True
            h = 1
        if True:
            self.chsis = True
            self.sis()
            h = 1
        if True:
            self.akt()
            self.chakt = True
            h = 1
        if True:
            self.jarn()
            self.chja = True
            h = 1
        if True:
            self.cont()
            self.chco = True
            h = 1
        Button(self.fram10, text='Применить', command=self.intheend, font=('Calibre', 15, 'bold'), width=15) \
            .grid(column=0, row=8, sticky=W)
        self.fram10.pack(anchor=W)
        self.fram1.destroy()

    def gn(self):
        self.lbl = Label(self.fram6, text='Вышел', font=('Calibre', 13, 'bold'))
        self.lbl.grid(column=0, row=0, sticky=W, padx=5, pady=7)

        Label(self.fram6, text='c', font=('Calibre', 13, 'bold'))\
            .grid(column=1, row=0, sticky=E, padx=5, pady=7)

        self.ckogn.grid(column=2, row=0, sticky=EW, padx=5, pady=7)

        Label(self.fram6, text='по', font=('Calibre', 13, 'bold'))\
            .grid(column=3, row=0, sticky=W, padx=5, pady=7)

        self.pokogn.grid(column=4, row=0, sticky=EW, padx=5, pady=7)

    def gk(self):

        self.lbl = Label(self.fram6, text='Закончился', font=('Calibre', 13, 'bold'))
        self.lbl.grid(column=0, row=1, sticky=W, padx=5, pady=7)

        Label(self.fram6, text='c', font=('Calibre', 13, 'bold')) \
            .grid(column=1, row=1, sticky=E, padx=5, pady=7)

        self.ckogk.grid(column=2, row=1, sticky=EW, padx=5, pady=7)

        Label(self.fram6, text='по', font=('Calibre', 13, 'bold'))\
            .grid(column=3, row=1, sticky=W, padx=5, pady=7)

        self.pokogk.grid(column=4, row=1, sticky=EW, padx=5, pady=7)

    def ser(self):
        self.lbl = Label(self.fram6, text='Кол-во серий', font=('Calibre', 13, 'bold'))
        self.lbl.grid(column=0, row=2, sticky=W, padx=5, pady=7)

        Label(self.fram6, text='c', font=('Calibre', 13, 'bold')) \
            .grid(column=1, row=2, sticky=E, padx=5, pady=7)

        self.cser.grid(column=2, row=2, sticky=EW, padx=5, pady=7)

        Label(self.fram6, text='по', font=('Calibre', 13, 'bold'))\
            .grid(column=3, row=2, sticky=W, padx=5, pady=7)

        self.poser.grid(column=4, row=2, sticky=EW, padx=5, pady=7)

    def sis(self):
        self.lbl = Label(self.fram6, text='Кол-во сезонов', font=('Calibre', 13, 'bold'))
        self.lbl.grid(column=0, row=3, sticky=W, padx=5, pady=7)

        Label(self.fram6, text='c', font=('Calibre', 13, 'bold')) \
            .grid(column=1, row=3, sticky=E, padx=5, pady=7)

        self.csis.grid(column=2, row=3, sticky=EW, padx=5, pady=7)

        Label(self.fram6, text='по', font=('Calibre', 13, 'bold'))\
            .grid(column=3, row=3, sticky=W, padx=5, pady=7)

        self.posis.grid(column=4, row=3, sticky=EW, padx=5, pady=7)
        self.fram6.pack(anchor=W)

    def akt(self):
        self.lbl = Label(self.fram6, text='Актеры ', font=('Calibre', 13, 'bold'))
        self.lbl.grid(column=0, row=4, sticky=W, padx=5, pady=7)

        self.cakt.grid(column=2, row=4, sticky=EW, padx=5, pady=7)

    def jarn(self):

        self.lbl = Label(self.fram6, text='Жанры', font=('Calibre', 13, 'bold'))
        self.lbl.grid(column=0, row=5, sticky=W, padx=5, pady=7)

        self.cja.grid(column=2, row=5, sticky=EW, padx=5, pady=7)

    def cont(self):
        self.lbl = Label(self.fram6, text='Страна ', font=('Calibre', 13, 'bold'))
        self.lbl.grid(column=0, row=6, sticky=W, padx=5, pady=7)

        self.cco.grid(column=2, row=6, sticky=EW, padx=5, pady=7)

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

    def intheend(self):
        kj = 0
        k = 0
        columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11')
        trees = ttk.Treeview(self.fram2, columns=columns, show='headings')
        style = ttk.Style(self.fram2)
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

        id_colector = []

        if self.ckogn.get():
            gn = self.ckogn.get()
        else:
            gn = 1800
        if self.pokogn.get():
            pgn = self.pokogn.get()
        else:
            pgn = 2030

        if self.ckogk.get():
            gk = self.ckogk.get()
        else:
            gk = 1800
        if self.pokogk.get():
            pgk = self.pokogk.get()
        else:
            pgk = 2030

        if self.cser.get():
            ser = self.cser.get()
        else:
            ser = 0
        if self.poser.get():
            pser = self.poser.get()
        else:
            pser = 1000

        if self.posis.get():
            psis = self.posis.get()
        else:
            psis = 20
        if self.csis.get():
            sis = self.csis.get()
        else:
            sis = 0

        if self.cakt.get():
            akt = self.cakt.get()
        else:
            akt = ' '

        if self.cja.get():
            jarn = self.cja.get()
        else:
            jarn = ' '
        if self.cco.get():
            count = self.cco.get()
        else:
            count = '.'

        for i in range(len(self.rel)):
            for ki in range(int(pgn) - int(gn) + 1):
                h = int(gn) + ki
                h = str(h)
                if h in self.rel[i][4]:
                    if self.pokogk.get():
                        for kki in range(int(pgk) - int(gk) + 1):
                            hk = int(gk) + kki
                            hk = str(hk)
                            if hk in self.rel[i][5]:
                                for kil in range(int(psis) - int(sis) + 1):
                                    h = int(sis) + kil
                                    h = str(h)
                                    if f' {h}' == self.rel[i][6]:
                                        for kie in range(int(pser) - int(ser) + 1):
                                            hs = int(ser) + kie
                                            hs = str(hs)
                                            if f' {hs}' == self.rel[i][7]:
                                                if akt in self.rel[i][9]:
                                                    if jarn in self.rel[i][8]:
                                                        if count in self.rel[i][10]:
                                                            if str(self.rel[i][0]) not in id_colector:
                                                                id_colector += [str(self.rel[i][0])]
                                                                contacts.append(self.rel[i])
                                                                kj = 1
                    else:
                        for kki in range(int(pgk) - int(gk) + 1):
                            hk = int(gk) + kki
                            hk = str(hk)
                            if ('-' in self.rel[i][5]) or (hk in self.rel[i][5]):
                                for kii in range(int(psis) - int(sis) + 1):
                                    h = int(sis) + kii
                                    h = str(h)
                                    if f' {h}' == self.rel[i][6]:
                                        for kie in range(int(pser) - int(ser)+1):
                                            hs = int(ser) + kie
                                            hs = str(hs)
                                            if f' {hs}' == self.rel[i][7]:
                                                if akt in self.rel[i][9]:
                                                    if jarn in self.rel[i][8]:
                                                        if count in self.rel[i][10]:
                                                            if str(self.rel[i][0]) not in id_colector:
                                                                id_colector += [str(self.rel[i][0])]
                                                                contacts.append(self.rel[i])
                                                                kj = 1
        for contact in contacts:
            trees.insert('', tk.END, values=contact)
        print(self.rel[3][5])
        print(' 2012')

        trees.column("#1", width=30)
        trees.column("#5", width=50)
        trees.column("#6", width=50)
        trees.column("#7", width=50)
        trees.column("#8", width=50)
        trees.column("#11", width=110)
        if kj == 1:
            trees.grid(column=0, row=0)
            self.fram3.destroy()
            self.fram4.destroy()
            self.fram5.destroy()
            self.fram6.destroy()
            self.fram7.destroy()
            self.fram8.destroy()
            self.fram9.destroy()
            self.fram10.destroy()
            self.fram2.pack(anchor=W)
        else:
            mb.showwarning('warning', 'НИЧЕГО НЕ НАЙДЕНО')
