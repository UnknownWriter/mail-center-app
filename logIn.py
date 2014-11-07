# logIn.py
# Neal Hamilton
# 11.7.14
# simple login started for mail center app


# imports
from Tkinter import *


def main():
    login = Tk()
    login.title('Login')

    # labels
    id_label = Label(login, text='Id number: ').grid(row=0)
    pword_label = Label(login, text='Password: ').grid(row=1)

    # entrys
    id_num = Entry(login, bd=5).grid(row=0, column=1)
    pword = Entry(login, bd=5).grid(row=1, column=1)

    # button events
    def button_click():
        print 'clicked'

    # button
    login_button = Button(login, text='Login', command=button_click).grid(row=2, column=1)

    # waiting for user's input
    login.mainloop()

if __name__ == "__main__":
    main()
