from tkinter import *



class Topics:
    def __init__(self):
        global root
        self.v = []
        self.root = Tk()
        self.root.title('Topics')
        self.root.geometry('350x250')

        self.labelTopic = Label(self.root, text="Nume topic ")
        self.labelTopic.grid(row=0, column=0)
        self.entryTopic = Entry(self.root)

        self.entryTopic.grid(row=1, column=0)
        self.buttonOk = Button(self.root, text='OK', command=self.add)
        self.buttonOk.grid(row=3, column=0)

        button = Button(self.root, text="Stergere topic", command=self.stergere_topic)
        button.grid(row=3, column=1)

        button = Button(self.root, text="Abonare", command=self.abonare_topic)
        button.grid(row=4, column=1)

        button = Button(self.root, text="Dezabonare", command=self.dezabonare_topic)
        button.grid(row=4, column=2)


        self.root.mainloop()



    def add(self):
        self.v.append(self.entryTopic.get())
        self.textbox=Listbox(self.root, height=10, width=30)
        self.textbox.grid(row=4,column=0)

        for i in self.v:
            self.textbox.insert(END,i+'\n')


    def stergere_topic(self):
        sel = self.textbox.curselection()
        for index in sel[::-1]:
            self.textbox.delete(index)

    def abonare_topic(self):
        sel = self.textbox.curselection()
        #for index in sel[::-1]:
         #   self.textbox.delete(index)

    def dezabonare_topic(self):
        sel = self.textbox.curselection()
        # for index in sel[::-1]:
        #   self.textbox.delete(index)
