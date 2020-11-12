from tkinter import *


def main():
    root = Tk()
    root.iconbitmap('calc.ico')
    root.title('calculator')
    ent_e1 = Entry(root, width=35, borderwidth=5)
    ent_e1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    first_num = 0
    operation = ''

    def btn_numeric(number):
        current = ent_e1.get()
        ent_e1.delete(0, END)
        ent_e1.insert(0, current + str(number))

    def btn_clear_cmd():
        ent_e1.delete(0, END)

    def btn_plus_cmd():
        nonlocal first_num
        nonlocal operation
        first_num = float(ent_e1.get())
        operation = '+'
        ent_e1.delete(0, END)

    def btn_minus_cmd():
        nonlocal first_num
        nonlocal operation
        first_num = float(ent_e1.get())
        operation = '-'
        ent_e1.delete(0, END)

    def btn_multi_cmd():
        nonlocal first_num
        nonlocal operation
        first_num = float(ent_e1.get())
        operation = '*'
        ent_e1.delete(0, END)

    def btn_div_cmd():
        nonlocal first_num
        nonlocal operation
        first_num = float(ent_e1.get())
        operation = 'div'
        ent_e1.delete(0, END)

    def btn_equal_cmd():
        nonlocal first_num
        nonlocal operation

        if operation == '+':
            result = first_num + float(ent_e1.get())
        elif operation == '-':
            result = first_num - float(ent_e1.get())
        elif operation == '*':
            result = first_num * float(ent_e1.get())
        elif operation == 'div':
            result = first_num / float(ent_e1.get())
        ent_e1.delete(0, END)
        ent_e1.insert(0, str(result))

    btn_b1 = Button(root, text="1", padx=40, pady=20, command=lambda: btn_numeric(1))
    btn_b2 = Button(root, text="2", padx=40, pady=20, command=lambda: btn_numeric(2))
    btn_b3 = Button(root, text="3", padx=40, pady=20, command=lambda: btn_numeric(3))
    btn_b4 = Button(root, text="4", padx=40, pady=20, command=lambda: btn_numeric(4))
    btn_b5 = Button(root, text="5", padx=40, pady=20, command=lambda: btn_numeric(5))
    btn_b6 = Button(root, text="6", padx=40, pady=20, command=lambda: btn_numeric(6))
    btn_b7 = Button(root, text="7", padx=40, pady=20, command=lambda: btn_numeric(7))
    btn_b8 = Button(root, text="8", padx=40, pady=20, command=lambda: btn_numeric(8))
    btn_b9 = Button(root, text="9", padx=40, pady=20, command=lambda: btn_numeric(9))
    btn_b0 = Button(root, text="0", padx=40, pady=20, command=lambda: btn_numeric(0))

    btn_plus = Button(root, text="+", padx=39, pady=20, command=btn_plus_cmd)
    btn_minus = Button(root, text="-", padx=41, pady=20, command=btn_minus_cmd)
    btn_multi = Button(root, text="*", padx=41, pady=20, command=btn_multi_cmd)
    btn_div = Button(root, text="/", padx=41, pady=20, command=btn_div_cmd)

    btn_equal = Button(root, text="=", padx=91, pady=20, command=btn_equal_cmd)
    btn_clear = Button(root, text="Clear", padx=79, pady=20, command=btn_clear_cmd)

    btn_b1.grid(row=3, column=0)
    btn_b2.grid(row=3, column=1)
    btn_b3.grid(row=3, column=2)

    btn_b4.grid(row=2, column=0)
    btn_b5.grid(row=2, column=1)
    btn_b6.grid(row=2, column=2)

    btn_b7.grid(row=1, column=0)
    btn_b8.grid(row=1, column=1)
    btn_b9.grid(row=1, column=2)

    btn_b0.grid(row=4, column=0)
    btn_clear.grid(row=4, column=1, columnspan=2)

    btn_plus.grid(row=5, column=0)
    btn_equal.grid(row=5, column=1, columnspan=2)

    btn_minus.grid(row=6, column=0)
    btn_multi.grid(row=6, column=1)
    btn_div.grid(row=6, column=2)

    root.mainloop()


if __name__ == '__main__':
    main()

