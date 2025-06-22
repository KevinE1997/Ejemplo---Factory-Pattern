import tkinter as tk

class ButtonFactory:
    def create_button(self, type, parent, text, command):
        if type == "primary":
            return tk.Button(parent, text=text, bg='blue', fg='white', command=command)
        elif type == "danger":
            return tk.Button(parent, text=text, bg='red', fg='white', command=command)
        else:
            return tk.Button(parent, text=text, command=command)

def show_message(msg):
    label.config(text=msg)

root = tk.Tk()
root.title("Factory Pattern Demo")

factory = ButtonFactory()

btn1 = factory.create_button("primary", root, "Botón Azul", lambda: show_message("Botón Azul"))
btn1.pack()

btn2 = factory.create_button("danger", root, "Botón Rojo", lambda: show_message("Botón Rojo"))
btn2.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
