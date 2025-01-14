import tkinter as tk
from tkinter import messagebox


class Empleado:
   def __init__(self, codigo, nombre, horas_trabajadas_mes, valor_hora, retencion_fuente):
       self.codigo = codigo
       self.nombre = nombre
       self.horas_trabajadas_mes = horas_trabajadas_mes
       self.valor_hora = valor_hora
       self.retencion_fuente = retencion_fuente


   def salario(self):
       retencion_fuente = self.retencion_fuente / 100
       salario_bruto = self.horas_trabajadas_mes * self.valor_hora
       salario_neto = salario_bruto * (1 - retencion_fuente)
       return salario_bruto, salario_neto


def calcular_salario():
   try:
       codigo = int(entry_codigo.get())
       nombre = entry_nombre.get()
       horas_trabajadas_mes = float(entry_horas.get())
       valor_hora = float(entry_valor_hora.get())
       retencion_fuente = float(entry_retencion.get())


       empleado = Empleado(codigo, nombre, horas_trabajadas_mes, valor_hora, retencion_fuente)
       salario_bruto, salario_neto = empleado.salario()


       messagebox.showinfo("Resultados", f"Código: {empleado.codigo}\n"
                                      f"Nombre: {empleado.nombre}\n"
                                      f"Salario Bruto: {salario_bruto:.2f}\n"
                                      f"Salario Neto: {salario_neto:.2f}")
   except ValueError:
       messagebox.showerror("Error", "Por favor, ingresa valores válidos en todos los campos.")


root = tk.Tk()
root.title("Cálculo de Salario de Empleados")


label_codigo = tk.Label(root, text="Código del empleado:")
label_codigo.grid(row=0, column=0, padx=10, pady=5)
entry_codigo = tk.Entry(root)
entry_codigo.grid(row=0, column=1, padx=10, pady=5)


label_nombre = tk.Label(root, text="Nombre del empleado:")
label_nombre.grid(row=1, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=1, column=1, padx=10, pady=5)


label_horas = tk.Label(root, text="Horas trabajadas al mes:")
label_horas.grid(row=2, column=0, padx=10, pady=5)
entry_horas = tk.Entry(root)
entry_horas.grid(row=2, column=1, padx=10, pady=5)


label_valor_hora = tk.Label(root, text="Valor por hora:")
label_valor_hora.grid(row=3, column=0, padx=10, pady=5)
entry_valor_hora = tk.Entry(root)
entry_valor_hora.grid(row=3, column=1, padx=10, pady=5)


label_retencion = tk.Label(root, text="Retención en la fuente (%):")
label_retencion.grid(row=4, column=0, padx=10, pady=5)
entry_retencion = tk.Entry(root)
entry_retencion.grid(row=4, column=1, padx=10, pady=5)


btn_calcular = tk.Button(root, text="Calcular Salario", command=calcular_salario)
btn_calcular.grid(row=5, column=0, columnspan=2, pady=10)


root.mainloop()
