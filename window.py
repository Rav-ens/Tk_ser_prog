from tkinter import *
import tkinter as tk
from poiski import Poisk
from apen import Appen
from tkinter import ttk
from tkinter import messagebox as mb
from filter import Filter


class Window:

    def __init__(self, width=2000, height=600, title="MyWindow", resizable=(True, True), icon=None):

        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        self.prov = False

        self.fr = Frame(self.root)

        Button(self.fr, text='Добавить', command=self.appen, font=('Calibre', 14, 'bold'), width=20)\
            .grid(column=0, row=4, sticky='E')
        Button(self.fr, text='Перезагрузить', command=self.tabl, font=('Calibre', 14, 'bold'), width=20)\
            .grid(column=0, row=1)
        Button(self.fr, text='Найти', command=self.poisk, font=('Calibre', 14, 'bold'), width=20)\
            .grid(column=0, row=2)
        Button(self.fr, text='Фильтрованый поиск', command=self.filter, font=('Calibre', 14, 'bold'), width=20)\
            .grid(column=0, row=3)
        Label(self.fr, text='      |     ', font=('Calibre', 20, 'bold')).grid(column=1, row=1)
        Label(self.fr, text='      |     ', font=('Calibre', 20, 'bold')).grid(column=1, row=2)
        Label(self.fr, text='      |     ', font=('Calibre', 20, 'bold')).grid(column=1, row=3)
        Label(self.fr, text='      |     ', font=('Calibre', 20, 'bold')).grid(column=1, row=4)
        self.stat_de = BooleanVar()
        self.stat_de.set(False)
        Checkbutton(self.fr, text='Включить редакцию', var=self.stat_de, font=('Calibre', 14, 'bold')) \
            .grid(column=2, row=1, sticky=W)
        Button(self.fr, text='Применить', command=self.proverk, font=('Calibre', 14, 'bold'), width=20) \
            .grid(column=2, row=2)
        self.fr.grid(column=0, row=1, sticky='W')

        self.result = 'jo'

    def base(self):

        self.tabl()
        base = open('data.txt', 'r')
        n = []
        for line in base:
            n += line.split('\n')

    def run(self):
        self.root.mainloop()

    def proverk(self):
        self.prov = self.stat_de.get()

    def appen(self, width=400, height=400, title="Добавление", resizable=(True, True), icon=None):
        Appen(self.root, width, height, title, resizable, icon)
        self.tabl()

    def poisk(self, width=10400, height=2400, title="Поиск", resizable=(True, True), icon=None):
        Poisk(self.root, width, height, title, resizable, icon)
        self.tabl()

    def tabl(self):
        self.loh()
        columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11')
        tree = ttk.Treeview(self.root, columns=columns, show='headings')
        ttk.Style().configure("TButton", rowheight=30, foreground='#2da488', font=('Calibre', 13, 'bold'))

        style = ttk.Style(self.root)
        style.configure("Treeview", rowheight=30, font=('Calibre', 13, 'bold'))
        tree.configure(style="Treeview")

        tree.heading('#1', text='id')
        tree.heading('#2', text='Имя на русском')
        tree.heading('#3', text='Имя на англ.')
        tree.heading('#4', text='Студия')
        tree.heading('#5', text='Год выпуска')
        tree.heading('#6', text='Год конца')
        tree.heading('#7', text='сезоны')
        tree.heading('#8', text='серии')
        tree.heading('#9', text='Жанры')
        tree.heading('#10', text='Актеры')
        tree.heading('#11', text='страна')
        contacts = []
        for i in range(len(self.result)):
            contacts.append(self.result[i])
        for contact in contacts:
            tree.insert('', tk.END, values=contact)
        tree.column("#1", width=30)
        tree.column("#5", width=50)
        tree.column("#6", width=50)
        tree.column("#7", width=50)
        tree.column("#8", width=50)
        tree.column("#11", width=110)

        def item_selected(event):
            if self.prov:
                c = []
                vivodim = FALSE
                for selected_item in tree.selection():
                    # dictionary
                    item = tree.item(selected_item)
                    iop = item['values']
                    iu = iop[0] - 1
                    f = open('data.txt').readlines()
                    c += f[iu].split(';')
                    print(c)
                    try:
                        vivodim = mb.askyesno('Удаление', f'Вы точно хотите удалить сериал "{c[0]}"?')
                    except IndexError:
                        mb.showerror('error', 'Слишком большая цифра')
                    if vivodim:
                        f.pop(iu)
                        with open('data.txt', 'w') as F:
                            F.writelines(f)
                        if f[iu] in f:
                            mb.showinfo('info', 'Успешно удалено')
                            self.tabl()

        tree.bind('<<TreeviewSelect>>', item_selected)

        tree.grid(column=0, row=0)
        ysb = ttk.Scrollbar(self.root, orient='vertical', command=tree.yview)
        tree.configure(yscroll=ysb.set)
        ysb.grid(row=0, column=1, sticky='ns')

    def loh(self):
        addto = 0
        world_base = []
        x = 0
        g = 0
        result = []
        line_base = []
        base = open('data.txt', 'r')
        f = ('data.txt', 'r')
        for line_no, line in enumerate(f, start=1):
            print(line)
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
            g += 1
            addto += [world_base[_ * 10 + g]]
            g = 0
            result += [addto]
            h += 1
        addto += [world_base[-1]]

        result += [addto]
        del result[-1][0]
        self.result = result

    def filter(self, width=600, height=300, title="Поиск", resizable=(True, True), icon=None):
        Filter(self.root, width, height, title, resizable, icon)
        self.tabl()
