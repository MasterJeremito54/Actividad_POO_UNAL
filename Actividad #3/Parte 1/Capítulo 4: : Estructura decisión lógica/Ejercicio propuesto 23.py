import tkinter as tk
from tkinter import messagebox
import math

def calcular():
    try:
        A = float(entrada_A.get())
        B = float(entrada_B.get())
        C = float(entrada_C.get())


        if A == 0:
            raise ValueError("El valor de A no puede ser 0. Esto no es una ecuacion de segundo grado.")


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


ventana = tk.Tk()
ventana.title("Ecuacion de Segundo Grado")

tk.Label(ventana, text="Coeficiente A:").grid(row=0, column=0, padx=10, pady=10)
entrada_A = tk.Entry(ventana)
entrada_A.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Coeficiente B:").grid(row=1, column=0, padx=10, pady=10)
entrada_B = tk.Entry(ventana)
entrada_B.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="Coeficiente C:").grid(row=2, column=0, padx=10, pady=10)
entrada_C = tk.Entry(ventana)
entrada_C.grid(row=2, column=1, padx=10, pady=10)

tk.Button(ventana, text="Calcular", command=calcular).grid(row=3, column=0, columnspan=2, pady=10)

ventana.mainloop()
