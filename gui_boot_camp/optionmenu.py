from tkinter import *


def main():

    def menu_show(*args):
        nonlocal lbl_value
        nonlocal selection
        lbl_value.configure(text=selection.get())

    root = Tk()
    root.title('tkinter bootcamp')
    root.iconbitmap('images/cam.ico')
    root.geometry("384x384")

    option_list = [
                    "Mazda",
                    "Suzuki",
                    "Volvo",
                    "Jeep",
                    "Toyota",
                    "Audi"
    ]
    selection = StringVar()
    selection.set(option_list[0])
    mnu_cartype = OptionMenu(root, selection, *option_list)
    selection.trace_add("write", menu_show)

    lbl_value = Label(root, text='...', font='arial 8 bold', fg='red')
    btn_update = Button(root, text='update', command=menu_show)

    mnu_cartype.grid(row=0, column=0)
    btn_update.grid(row=1, column=0)
    lbl_value.grid(row=2, column=0)

    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

