from tkinter import *



class Topics:
    def __init__(self):
        global root
        self.v = []
        self.root = Tk()
        self.root.title('Topics')
        self.root.geometry('750x750')

        self.menubar=Menu(self.root)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Add", command=self.adaugare_topic)
        filemenu.add_command(label="Erase", command=self.go_to_stergere_topic)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(self.menubar, tearoff=0)

        editmenu.add_separator()

        self.root.config(menu=self.menubar)
        self.root.mainloop()


    def adaugare_topic(self):
        self.labelTopic = Label(self.root, text="Nume topic ")
        self.labelTopic.grid(row=0, column=0)
        self.entryTopic = Entry(self.root)

        self.entryTopic.grid(row=1, column=0)
        self.buttonOk = Button(self.root, text='OK', command=self.add)
        self.buttonOk.grid(row=3, column=0)

    def add(self):
        self.v.append(self.entryTopic.get())
        self.textbox=Listbox(self.root, height=10, width=30)
        self.textbox.grid(row=4,column=0)

        for i in self.v:
            self.textbox.insert(END,i+'\n')


    def go_to_stergere_topic(self):
        button = Button(self.root, text="Stergere topic", command=self.stergere_topic)
        button.grid()

    def stergere_topic(self):
        sel = self.textbox.curselection()
        for index in sel[::-1]:
            self.textbox.delete(index)

