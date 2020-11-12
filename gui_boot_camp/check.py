from tkinter import *


def main():

    def checkbox_show(value):
        nonlocal lbl_value
        lbl_value.configure(text=str(value))

    root = Tk()
    root.title('tkinter bootcamp')
    root.iconbitmap('images/cam.ico')
    turbo = IntVar()
    chk_turbo = Checkbutton(root, text='turbo mode', variable=turbo)
    lbl_value = Label(root, text='...', font='arial 8 bold', fg='red')
    btn_update = Button(root, text='update', command=lambda: checkbox_show(turbo.get()))

    chk_turbo.grid(row=0, column=0, columnspan=5, sticky=W+E)
    btn_update.grid(row=1, column=0, columnspan=5, sticky=W+E)
    lbl_value.grid(row=2, column=0)

    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

