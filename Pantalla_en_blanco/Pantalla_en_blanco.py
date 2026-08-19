import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Actividad 02 - Pantalla en blanco")
ventana.geometry("450x350")
ventana.configure(bg="Orange")

def enviar_msjbox():
    nombre = tbNombre.get()
    messagebox.showinfo("Programacion Avanzada", "Bienvenido "+nombre)
lbNombre =tk.Label(text="Nombre :")
lbNombre.place(x=60,y=60)
tbNombre =tk.Entry()
tbNombre.place(x=120,y=60)
btnAceptar = tk.Button(ventana, text="Aceptar", command=enviar_msjbox)
btnAceptar.place(x=120,y=120)
btnCancelar= tk.Button(ventana, text="Cancelar", comman= ventana.quit)
btnCancelar.place(x=180,y=120)

ventana.mainloop()
