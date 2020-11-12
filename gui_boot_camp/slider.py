from tkinter import *


def main():

    def slider_show():
        nonlocal lbl_value
        nonlocal sld_horiz
        lbl_value.configure(text=str(sld_horiz.get()))

    root = Tk()
    root.title('tkinter bootcamp')
    root.iconbitmap('images/cam.ico')

    sld_horiz = Scale(root, from_=0, to=200, orient=HORIZONTAL)
    lbl_value = Label(root, text='...', font='arial 8 bold', fg='red')
    btn_update = Button(root, text='update', command=slider_show)

    sld_horiz.grid(row=0, column=0, columnspan=5, sticky=W+E)
    btn_update.grid(row=1, column=0, columnspan=5, sticky=W+E)
    lbl_value.grid(row=2, column=0)

    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

