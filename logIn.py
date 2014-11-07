


from Tkinter import *


def main():
    login = Tk()
    login.title('Login')

    # button events
    def button_click():
        print 'clicked'

    # labels
    id_label = Label(login, text='Id number: ').grid(row=0)
    pword_label = Label(login, text='Password: ').grid(row=1)

    # entrys
    id_num = Entry(login, bd=5).grid(row=0, column=1)
    pword = Entry(login, bd=5).grid(row=1, column=1)

    # button
    login_button = Button(login, text='Login', command=button_click).grid(row=2, column=1)

    login.mainloop()

if __name__ == "__main__":
    main()
