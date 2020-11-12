from tkinter import *
import sqlite3


def main():

    def clear():
        nonlocal ent_make
        nonlocal ent_model
        nonlocal ent_year
        nonlocal ent_price
        nonlocal ent_class
        ent_make.delete(0, END)
        ent_model.delete(0, END)
        ent_year.delete(0, END)
        ent_price.delete(0, END)
        ent_class.delete(0, END)

    def add():
        nonlocal ent_make
        nonlocal ent_model
        nonlocal ent_year
        nonlocal ent_price
        nonlocal ent_class
        nonlocal dbconn
        nonlocal c
        c.execute("INSERT INTO cartypes VALUES (:make, :model, :year, :price, :class)",
                  {
                    'make': ent_make.get(),
                    'model': ent_model.get(),
                    'year': ent_year.get(),
                    'price': ent_price.get(),
                    'class': ent_class.get()
                  })
        # commit changes
        dbconn.commit()
        clear()
        read()

    def read():
        nonlocal lbl_cars
        nonlocal dbconn
        nonlocal c
        c.execute("SELECT *,oid FROM cartypes")
        dbconn.commit()
        records = c.fetchall()
        text = ''
        for record in records:
            for item in record:
                text += str(item) + " | "
            text += "\n"
        lbl_cars.configure(text=text)

    def delete():
        nonlocal dbconn
        nonlocal c
        nonlocal ent_select
        c.execute(f"DELETE from cartypes WHERE oid={ent_select.get()}")
        dbconn.commit()
        ent_select.delete(0, END)
        read()

    def select():
        nonlocal dbconn
        nonlocal c
        nonlocal ent_select
        nonlocal ent_make
        nonlocal ent_model
        nonlocal ent_year
        nonlocal ent_price
        nonlocal ent_class
        c.execute(f"SELECT *,oid FROM cartypes WHERE oid={ent_select.get()}")
        dbconn.commit()
        records = c.fetchall()
        clear()
        if len(records) == 0:
            return
        ent_make.insert(0, records[0][0])
        ent_model.insert(0, records[0][1])
        ent_year.insert(0, records[0][2])
        ent_price.insert(0, records[0][3])
        ent_class.insert(0, records[0][4])

    def update():
        nonlocal dbconn
        nonlocal c
        nonlocal ent_select
        nonlocal ent_make
        nonlocal ent_model
        nonlocal ent_year
        nonlocal ent_price
        nonlocal ent_class
        c.execute("""UPDATE cartypes SET
            make = :make,
            model = :model,
            year = :year,
            price = :price,
            class = :class
            
            WHERE oid = :oid""",
                  {
                    'make': ent_make.get(),
                    'model': ent_model.get(),
                    'year': ent_year.get(),
                    'price': ent_price.get(),
                    'class': ent_class.get(),
                    'oid': ent_select.get()
                  })
        dbconn.commit()
        clear()
        ent_select.delete(0, END)
        read()

    # main form window:
    root = Tk()
    root.title('tkinter bootcamp')
    root.iconbitmap('images/cam.ico')
    # data entry controls:
    ent_make = Entry(root, width=30)
    ent_make.grid(row=0, column=1)
    ent_model = Entry(root, width=30)
    ent_model.grid(row=1, column=1)
    ent_year = Entry(root, width=30)
    ent_year.grid(row=2, column=1)
    ent_price = Entry(root, width=30)
    ent_price.grid(row=3, column=1)
    ent_class = Entry(root, width=30)
    ent_class.grid(row=4, column=1)
    lbl_make = Label(root, text="make")
    lbl_make.grid(row=0, column=0)
    lbl_model = Label(root, text="model")
    lbl_model.grid(row=1, column=0)
    lbl_year = Label(root, text="year")
    lbl_year.grid(row=2, column=0)
    lbl_price = Label(root, text="price")
    lbl_price.grid(row=3, column=0)
    lbl_class = Label(root, text="class")
    lbl_class.grid(row=4, column=0)
    # controls to add, delete, select and update records:
    btn_add = Button(root, text='add', font='courier 10 bold', fg='green', command=add)
    btn_add.grid(row=5, column=0, columnspan=2, sticky=W+E)
    btn_read = Button(root, text='read', font='courier 10 bold', fg='blue', command=read)
    btn_read.grid(row=6, column=0, columnspan=2, sticky=W+E)
    lbl_select = Label(root, text='select ID', anchor=W, justify=LEFT)
    lbl_select.grid(row=7, column=0)
    ent_select = Entry(root, width=30, font='courier 10 bold')
    ent_select.grid(row=7, column=1)
    btn_select = Button(root, text='select', font='courier 10 bold', fg='blue', command=select)
    btn_select.grid(row=8, column=0, columnspan=2, sticky=W + E)
    btn_delete = Button(root, text='delete', font='courier 10 bold', fg='red', command=delete)
    btn_delete.grid(row=9, column=0, columnspan=2, sticky=W+E)
    btn_update = Button(root, text='update', font='courier 10 bold', fg='purple', command=update)
    btn_update.grid(row=10, column=0, columnspan=2, sticky=W + E)
    # data viewing control:
    lbl_cars = Label(text='*', anchor=W, justify=LEFT)
    lbl_cars.grid(row=11, column=0, columnspan=2, sticky=W+E)

    # create or connect to a database:
    dbconn = sqlite3.connect('cars.db')
    # create a cursor:
    c = dbconn.cursor()
    # main application loop:
    read()
    root.mainloop()
    # close connection:
    dbconn.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# create a table - this was done just once:
# c.execute("""CREATE TABLE cartypes (
#             make text,
#             model text,
#             year integer,
#             price integer,
#             class integer
#             )""")
