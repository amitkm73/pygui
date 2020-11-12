from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


def main():
    def info():
        messagebox.showinfo('tkinter bootcamp', 'some information !')

    def warn():
        messagebox.showwarning('tkinter bootcamp', 'some warning !')

    def err():
        messagebox.showerror('tkinter bootcamp', 'some error !')

    def question():
        response = messagebox.askquestion('tkinter bootcamp', 'some question ?')
        nonlocal lbl_response
        lbl_response.configure(text=f'response = {str(response)}')

    def ok_cancel():
        response = messagebox.askokcancel('tkinter bootcamp', 'ok or cancel ?')
        nonlocal lbl_response
        lbl_response.configure(text=f'response = {str(response)}')

    def yes_no():
        response = messagebox.askyesno('tkinter bootcamp', 'yes or no ?')
        nonlocal lbl_response
        lbl_response.configure(text=f'response = {str(response)}')

    def select_file():
        response = filedialog.askopenfilename(initialdir='/', title='select a file', filetypes=(("text files", "*.txt"), ("png files", "*.png"), ("all files", "*.*")))
        nonlocal lbl_response
        lbl_response.configure(text=f'response = {str(response)}')

    root = Tk()
    root.iconbitmap('images/calc.ico')
    root.title('message boxes')
    btn_info = Button(root, text='info', font='arial 8 bold', padx=32, command=info)
    btn_warn = Button(root, text='warning', font='arial 8 bold', padx=32, command=warn)
    btn_err = Button(root, text='error', font='arial 8 bold', padx=32, command=err)
    btn_question = Button(root, text='question', font='arial 8 bold', padx=19, command=question)
    btn_ok_cancel = Button(root, text='ok or cancel', font='arial 8 bold', padx=19, command=ok_cancel)
    btn_yes_no = Button(root, text='yes or no', font='arial 8 bold', padx=19, command=yes_no)
    btn_file = Button(root, text='file selection', font='arial 8 bold', padx=19, command=select_file)
    lbl_response = Label(text='...', font='arial 8 bold', fg='blue', relief=SUNKEN, anchor=W)

    btn_info.grid(row=0, column=0)
    btn_warn.grid(row=0, column=1)
    btn_err.grid(row=0, column=2)
    btn_question.grid(row=1, column=0)
    btn_ok_cancel.grid(row=1, column=1)
    btn_yes_no.grid(row=1, column=2)
    btn_file.grid(row=2, column=0, columnspan=2, sticky=W+E)
    lbl_response.grid(row=3, column=0, columnspan=3, sticky=W+E)

    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

