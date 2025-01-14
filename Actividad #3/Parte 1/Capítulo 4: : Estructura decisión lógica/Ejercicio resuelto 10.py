import tkinter as tk
from tkinter import messagebox


class Matricula:
   def __init__(self, inscripcion, nombre, patrimonio, estrato):
       self.inscripcion = inscripcion
       self.nombre = nombre
       self.patrimonio = patrimonio
       self.estrato = estrato


   def pago(self):
       pago_base = 50000
       if self.patrimonio > 2000000 and self.estrato > 3:
           pago_base += 0.03 * self.patrimonio
       return pago_base


def calcular():
   try:
       inscripcion = entry_inscripcion.get()
       nombre = entry_nombre.get()
       patrimonio = float(entry_patrimonio.get())
       estrato = int(entry_estrato.get())


       if patrimonio < 0 or estrato < 0:
           raise ValueError("El patrimonio y el estrato deben ser valores positivos.")


       estudiante = Matricula(inscripcion, nombre, patrimonio, estrato)
       pago = estudiante.pago()


       messagebox.showinfo("Resultado", f"Número de Inscripción: {inscripcion}\nNombre: {nombre}\nPago de Matrícula: ${pago:.2f}")
   except ValueError as e:
       messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Cálculo Pago Matrícula")


tk.Label(root, text="Número de Inscripción:").grid(row=0, column=0, padx=10, pady=10)
entry_inscripcion = tk.Entry(root)
entry_inscripcion.grid(row=0, column=1, padx=10, pady=10)


tk.Label(root, text="Nombre:").grid(row=1, column=0, padx=10, pady=10)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=1, column=1, padx=10, pady=10)


tk.Label(root, text="Patrimonio:").grid(row=2, column=0, padx=10, pady=10)
entry_patrimonio = tk.Entry(root)
entry_patrimonio.grid(row=2, column=1, padx=10, pady=10)


tk.Label(root, text="Estrato:").grid(row=3, column=0, padx=10, pady=10)
entry_estrato = tk.Entry(root)
entry_estrato.grid(row=3, column=1, padx=10, pady=10)


tk.Button(root, text="Calcular", command=calcular).grid(row=4, column=0, columnspan=2, pady=10)


root.mainloop()
