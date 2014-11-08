# new_user.py
# Neal Hamilton
# 11.7.14
# creates new user for non-students


from Tkinter import *
import logIn as user_login


def main():


    new_user = Tk()
    new_user.title('New User Registration')



    # contact info and address labels
    lname_lbl  = Label(new_user, text='Last Name: ').grid(row=1)
    fname_lbl  = Label(new_user, text='First Name: ').grid(row=1, column=2)
    phone_lbl  = Label(new_user, text='Phone Number: ').grid(row=2)
    email_lbl  = Label(new_user, text='Email Address: ').grid(row=2, column=2)
    street_lbl = Label(new_user, text='Street: ').grid(row=3)
    city_lbl   = Label(new_user, text='City: ').grid(row=3, column=2)
    state_lbl  = Label(new_user, text='State: ').grid(row=4)
    postal_lbl = Label(new_user, text='Zip Code: ').grid(row=4, column=2)

    # contact info and address entries
    lname  = Entry(new_user, bd=5).grid(row=1, column=1)
    fname  = Entry(new_user, bd=5).grid(row=1, column=4)
    phone  = Entry(new_user, bd=5).grid(row=2, column=1)
    email  = Entry(new_user, bd=5).grid(row=2, column=4)
    street = Entry(new_user, bd=5).grid(row=3, column=1)
    city   = Entry(new_user, bd=5).grid(row=3, column=4)
    state  = Entry(new_user, bd=5).grid(row=4, column=1)
    postal = Entry(new_user, bd=5).grid(row=4, column=4)

    divider = Label().grid(row=5)

    # username and password
    username_lbl = Label(new_user, text='Username: ').grid(row=6)
    username = Entry(new_user, bd=5).grid(row=6, column=1)
    password_lbl = Label(new_user, text='Password: ').grid(row=7)
    password= Entry(new_user, bd=5).grid(row=7, column=1)


    # button events
    def validate_create_event():
        # TODO:
        # check that they're all filled
        # check that username, email, etc isn't already in db
        # create record in db
        # alert user that this had been done
        # redirect them to login page
        print 'validate_create'


    def cancel_event():
        print 'cancel_event clicked from within NewUser.py'
        new_user.destroy()
        user_login.main()



    submit = Button(text='Create Account', command=validate_create_event)
    submit.grid(row=6, column=4)

    cancel = Button(text='Cancel', command=cancel_event)
    cancel.grid(row=7, column=4)

    new_user.mainloop()


if __name__ == "__main__":
    main()
