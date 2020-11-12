from tkinter import *


def main():
    root = Tk()

    ent_e1 = Entry(root, width=40, fg='red', borderwidth=4)
    ent_e1.pack()
    ent_e1.insert(0, 'your name: ')

    def btn1_click():
        lbl_l1 = Label(root, text='hello ' + ent_e1.get(), fg='red')
        lbl_l1.pack()

    btn_b1 = Button(root, text='enter your name', fg='purple', command=btn1_click)
    btn_b1.pack()

    root.mainloop()

    # top_frame = Frame(root)
    # top_frame.pack(side=TOP)
    # bottom_frame = Frame(root)
    # bottom_frame.pack(side=BOTTOM)
    # btn_b1 = Button(top_frame, text='up', fg='red')
    # btn_b2 = Button(top_frame, text='down', fg='green')
    # btn_b3 = Button(top_frame, text='reset', fg='blue')
    # btn_b4 = Button(bottom_frame, text='submit', fg='purple')
    # btn_b1.pack(side=LEFT)
    # btn_b2.pack(side=LEFT)
    # btn_b3.pack(side=LEFT)
    # btn_b4.pack(side=BOTTOM)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

