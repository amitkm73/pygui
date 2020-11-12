from tkinter import *


def main():

    def selected():
        nonlocal rb1
        lbl_selection.configure(text='selection = ' + str(rb1.get()))
        lbl_selection.pack_forget()
        lbl_selection.pack()

    root = Tk()
    root.iconbitmap('images/calc.ico')
    root.title('radio buttons')
    rb1 = IntVar()
    for x in range(1, 11):
        rb_multi_tmp = Radiobutton(root, text=f'option {x}', variable=rb1, value=x, command=selected)
        rb_multi_tmp.pack()
    lbl_selection = Label(root, font='arial 8 bold')
    rb1.set(1)
    selected()

    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

