import tkinter as tk
from tkinter import messagebox
import math


def calcular():
   try:
       A = float(entry_A.get())
       B = float(entry_B.get())
       C = float(entry_C.get())


       if A == 0:
           raise ValueError("El valor de A no puede ser 0. Esto no es una ecuación de segundo grado.")


       discriminante = B**2 - 4*A*C


       if discriminante > 0:
           x1 = (-B + math.sqrt(discriminante)) / (2 * A)
           x2 = (-B - math.sqrt(discriminante)) / (2 * A)
           messagebox.showinfo("Resultado", f"Las soluciones son reales y distintas:\n x1 = {x1:.2f}, x2 = {x2:.2f}")
       elif discriminante == 0:
           x = -B / (2 * A)
           messagebox.showinfo("Resultado", f"Las soluciones son reales e iguales:\n x1 = x2 = {x:.2f}")
       else:
           real = -B / (2 * A)
           imaginaria = math.sqrt(abs(discriminante)) / (2 * A)
           messagebox.showinfo("Resultado", f"Las soluciones son complejas:\n x1 = {real:.2f} + {imaginaria:.2f}i\n x2 = {real:.2f} - {imaginaria:.2f}i")


   except ValueError as e:
       messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Ecuación de Segundo Grado")
