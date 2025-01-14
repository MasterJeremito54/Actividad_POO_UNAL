import tkinter as tk
from tkinter import messagebox


class Empleado:
   def __init__(self, nombre, salario_hora, horas_trabajadas):
       self.nombre = nombre
       self.salario_hora = salario_hora
       self.horas_trabajadas = horas_trabajadas


   def calcular_salario_mensual(self):
       return self.salario_hora * self.horas_trabajadas


def calcular():
   try:
       nombre = entry_nombre.get()
       salario_hora = float(entry_salario_hora.get())
       horas_trabajadas = int(entry_horas_trabajadas.get())


       if salario_hora < 0 or horas_trabajadas < 0:
           raise ValueError("El salario por hora y las horas trabajadas deben ser valores positivos.")


       empleado = Empleado(nombre, salario_hora, horas_trabajadas)
       salario_mensual = empleado.calcular_salario_mensual()


       if salario_mensual > 450000:
           messagebox.showinfo("Resultado", f"Empleado: {nombre}\nSalario Mensual: ${salario_mensual:.2f}")
       else:
           messagebox.showinfo("Resultado", f"Empleado: {nombre}")


   except ValueError as e:
       messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Cálculo Salario Mensual")


tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)


tk.Label(root, text="Salario por Hora:").grid(row=1, column=0, padx=10, pady=10)
entry_salario_hora = tk.Entry(root)
entry_salario_hora.grid(row=1, column=1, padx=10, pady=10)


tk.Label(root, text="Horas Trabajadas:").grid(row=2, column=0, padx=10, pady=10)
entry_horas_trabajadas = tk.Entry(root)
entry_horas_trabajadas.grid(row=2, column=1, padx=10, pady=10)


tk.Button(root, text="Calcular", command=calcular).grid(row=3, column=0, columnspan=2, pady=10)


root.mainloop()
