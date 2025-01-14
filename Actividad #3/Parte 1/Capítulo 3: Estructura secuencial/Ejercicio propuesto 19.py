import math
import tkinter as tk
from tkinter import messagebox


class Triangulo:
   def __init__(self, lado):
       self.lado = lado


   def perimetro(self):
       return 3 * self.lado


   def altura(self):
       return math.sqrt(self.lado**2 - (self.lado / 2)**2)


   def area(self):
       return (self.lado * self.altura()) / 2


def calcular():
   try:
       lado = float(entry_lado.get())
       if lado <= 0:
           raise ValueError("El lado debe ser un valor positivo.")


       triangulo = Triangulo(lado)
       perimetro = triangulo.perimetro()
       altura = triangulo.altura()
       area = triangulo.area()


       messagebox.showinfo("Resultados", f"Perímetro: {perimetro:.2f}\nAltura: {altura:.2f}\nÁrea: {area:.2f}")
   except ValueError as e:
       messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Cálculo Triángulo Equilátero")


tk.Label(root, text="Lado del triángulo:").grid(row=0, column=0, padx=10, pady=10)
entry_lado = tk.Entry(root)
entry_lado.grid(row=0, column=1, padx=10, pady=10)


tk.Button(root, text="Calcular", command=calcular).grid(row=1, column=0, columnspan=2, pady=10)


root.mainloop()
