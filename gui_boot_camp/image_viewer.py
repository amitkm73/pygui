from tkinter import *
from PIL import ImageTk, Image


def main():

    def read_images():
        image = Image.open('/images/c.png')
        image = image.resize((80, 80). Image.ANTIALIAS)
        # img_c = ImageTk.PhotoImage(Image.open('images/c.png'))
        img_code = ImageTk.PhotoImage(Image.open('images/code.png'))
        img_dl = ImageTk.PhotoImage(Image.open('images/deep-learning.png'))
        img_developer = ImageTk.PhotoImage(Image.open('images/developer.png'))
        img_docker = ImageTk.PhotoImage(Image.open('images/docker.png'))
        img_linux = ImageTk.PhotoImage(Image.open('images/linux.png'))
        img_programmer = ImageTk.PhotoImage(Image.open('images/programmer.png'))
        img_python = ImageTk.PhotoImage(Image.open('images/python.png'))
        img_list_tmp = [img_c, img_code, img_dl, img_developer, img_docker, img_linux, img_programmer, img_python]
        return img_list_tmp

    def update_image():
        nonlocal img_list
        nonlocal current_image
        nonlocal lbl_image
        nonlocal lbl_status
        lbl_image.configure(image=img_list[current_image])
        lbl_image.grid_forget()
        lbl_image.grid(row=0, column=0, columnspan=5)
        lbl_status.configure(text=f'image {current_image+1} of {len(img_list)}')
        lbl_status.grid_forget()
        lbl_status.grid(row=2, column=0, columnspan=5, sticky=W+E)

    def cmd_move(direction):
        nonlocal current_image
        nonlocal num_images
        current_image = (current_image + direction) % num_images
        update_image()
        return

    root = Tk()
    root.iconbitmap('images/cam.ico')
    root.title('image viewer')

    img_list = read_images()
    num_images = len(img_list)
    current_image = 0

    lbl_image = Label(root)
    font = "arial 10 bold"
    btn_back = Button(root, text="<<", fg="red", font=font, padx=32, pady=16, bd=2, command=lambda: cmd_move(-1))
    btn_exit = Button(root, text="exit", font=font, padx=32, pady=16, bd=2, command=root.quit)
    btn_forward = Button(root, text=">>", fg="green", font=font, padx=32, pady=16, bd=2, command=lambda: cmd_move(1))
    lbl_status = Label(root, font="arial 8 bold", pady=4, relief=SUNKEN, anchor=E)

    update_image()
    btn_back.grid(row=1, column=0)
    btn_exit.grid(row=1, column=2)
    btn_forward.grid(row=1, column=4)

    root.mainloop()


if __name__ == '__main__':
    main()
