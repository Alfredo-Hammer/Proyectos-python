from tkinter import *

root = Tk()
root.title("Radio Buttons")
root.iconbitmap("python.ico")
root.geometry("500x500")

q = IntVar()
q.get()
q.set('2')

def click(value):
    label = Label(root, text = value)
    label.pack()
    
Radiobutton(root, text="Opcion 1 ", padx=10, pady=5, variable=q, value=1).pack(anchor='w')
Radiobutton(root, text="Opcion 2 ",padx=10, pady=5, variable=q, value=2).pack(anchor='w')
Radiobutton(root, text="Opcion 3 ",padx=10, pady=5, variable=q, value=3).pack(anchor='w')
Radiobutton(root, text="Opcion 4 ",padx=10, pady=5, variable=q, value=4).pack(anchor='w')

label = Label(root, text = q.get())
label.pack()

my_button = Button(root, text="Enviar",padx=30, pady=5,bg = "grey", command = lambda: click(q.get()))
my_button.pack()


root.mainloop()
