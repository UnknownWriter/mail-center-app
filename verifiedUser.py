# verifiedUser.py
# Neal Hamilton
# 11.7.14
# gui that show's once user is verified

from Tkinter import *

class verifiedUser(Frame):


    def Button_Click(self):
        print 'clicked'


    def create_gui(self):

        self.entry = Entry(self, bd=5)
        self.click = Button(text='Click Me', command=self.Button_Click())

        self.click.pack()
        self.entry.pack()



    def __init__(self, master=None , data = 0):
        self.data = data
        Frame.__init__(self, master)
        self.pack()
        self.create_gui()


def main():
    main = Tk()
    app = verifiedUser(master=main)
    app.mainloop()
    main.destroy()

if __name__ == "__main__":
    main()
