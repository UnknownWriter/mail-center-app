# ForwardingInterface.py
# Neal Hamilton
# 11.8.14
# user interface to set forwarding status


from Tkinter import *
import LogIn as login_ui

def main():

    forward_ui = Tk()
    forward_ui.title('Forwarding Interface')

	# labels
    street_lbl     = Label(forward_ui, text='Street: ').grid(row=0)
    city_lbl       = Label(forward_ui, text='City: ').grid(row=1)
    state_lbl      = Label(forward_ui, text='State: ').grid(row=2)
    postal_lbl     = Label(forward_ui, text='Zip Code: ').grid(row=3)
    start_date_lbl = Label(forward_ui, text='Start Date (mm/dd/yyyy): ').grid(row=4)
    end_date_lbl   = Label(forward_ui, text='End Date (mm/dd/yyyy): ').grid(row=5)


	# entrys
    street      = Entry(forward_ui, bd=5).grid(row=0, column=1)
    city        = Entry(forward_ui, bd=5).grid(row=1, column=1)
    state       = Entry(forward_ui, bd=5).grid(row=2, column=1)
    postal      = Entry(forward_ui, bd=5).grid(row=3, column=1)
    start_date  = Entry(forward_ui, bd=5).grid(row=4, column=1)
    end_date    = Entry(forward_ui, bd=5).grid(row=5, column=1)

	# button events
    def frwd_submit_event():
        forward_ui.destroy()
        print 'submit event from ForwardingInterface'


    def frwd_cancel_event():
        forward_ui.destroy()
        login_ui.main()
        print 'cancel event from ForwardingInterface'

	# buttons
    submit_info = Button(forward_ui, text='Submit Request', command=frwd_submit_event).grid(row=6, column=1)
    cancel = Button(forward_ui, text='Cancel', command=frwd_cancel_event).grid(row=6, column=2)

    # waiting for input from user
    forward_ui.mainloop()



if __name__ == "__main__":
    main()
