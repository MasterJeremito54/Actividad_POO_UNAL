import tkinter as tk
from tkinter import messagebox


def comparar_numeros():
    try:
        A = int(entrada_a.get())
        B = int(entrada_b.get())

        if A > B:
            resultado = "A es mayor que B"
        elif A == B:
            resultado = "A es igual a B"
        else:
            resultado = "A es menor que B"

        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")


ventana = tk.Tk()
ventana.title("Comparador de Números")

etiqueta_a = tk.Label(ventana, text="Ingrese el número A:")
etiqueta_a.grid(row=0, column=0, padx=10, pady=10)
entrada_a = tk.Entry(ventana)
entrada_a.grid(row=0, column=1, padx=10, pady=10)

etiqueta_b = tk.Label(ventana, text="Ingrese el número B:")
etiqueta_b.grid(row=1, column=0, padx=10, pady=10)
entrada_b = tk.Entry(ventana)
entrada_b.grid(row=1, column=1, padx=10, pady=10)

boton_comparar = tk.Button(ventana, text="Comparar", command=comparar_numeros)
boton_comparar.grid(row=2, column=0, columnspan=2, pady=20)

ventana.mainloop()
