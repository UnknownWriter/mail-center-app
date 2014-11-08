# LogIn.py
# Neal Hamilton
# 11.7.14
# simple login started for mail center app


# imports
from Tkinter import *
import NewUser as new_user_gui
import ForwardingInterface as forwarding_gui


def main():
    login = Tk()
    login.title('Log In')

    # labels
    id_label = Label(login, text='Id number: ').grid(row=0)
    pword_label = Label(login, text='Password: ').grid(row=1)

    # entrys
    id_num = Entry(login, bd=5).grid(row=0, column=1)
    pword = Entry(login, bd=5).grid(row=1, column=1)

    # button events
    def login_event():
        login.destroy()
        forwarding_gui.main()
        print 'login_event clicked from login.py'

    # button
    login_button = Button(login, text='Login', command=login_event).grid(row=2, column=1)


    # creates new user account
    def new_user():
        login.destroy()
        new_user_gui.main()
        print 'new user account button clicked from login.py'
        #login.destroy()

    # create new user
    new_label = Label(login, text='For non-students, please create\n an account by clicking this button!')
    new_label.grid(row=5)

    new_button = Button(login, text='Create Account', command=new_user)
    new_button.grid(row=5, column=1)


    # waiting for user's input
    login.mainloop()

if __name__ == "__main__":
    main()
