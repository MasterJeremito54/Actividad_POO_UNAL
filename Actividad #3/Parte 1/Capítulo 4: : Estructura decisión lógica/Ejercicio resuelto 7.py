import tkinter as tk
from tkinter import messagebox


def compare_numbers():
   try:
       A = int(entry_a.get())
       B = int(entry_b.get())


       if A > B:
           result = "A es mayor que B"
       elif A == B:
           result = "A es igual a B"
       else:
           result = "A es menor que B"


       messagebox.showinfo("Resultado", result)
   except ValueError:
       messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")


root = tk.Tk()
root.title("Comparador de Números")


label_a = tk.Label(root, text="Ingrese el número A:")
label_a.grid(row=0, column=0, padx=10, pady=10)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=10)


label_b = tk.Label(root, text="Ingrese el número B:")
label_b.grid(row=1, column=0, padx=10, pady=10)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=10, pady=10)


button_compare = tk.Button(root, text="Comparar", command=compare_numbers)
button_compare.grid(row=2, column=0, columnspan=2, pady=20)


root.mainloop()
