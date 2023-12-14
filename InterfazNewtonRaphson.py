import tkinter as tk
import NewtonRaphson as NR

raiz = tk.Tk()
raiz.resizable(False, False)
raiz.geometry("650x350")

label_raiz = tk.Label(raiz, text="Aquí aparecerá el valor de la raiz")
label_raiz.pack()

def mostrar_raiz():
    try:
        valor_i = int(entry_i.get())
        valor_s = int(entry_s.get())
        valor_o = int(entry_o.get())
        
        label_raiz.config(text="El valor de la raiz es: "+ str(NR.NewtonRaphson(NR.funcion_cuadratica, NR.derivada_cuadratica, 1, 100, 0.0001)))
        return NR.NewtonRaphson(NR.funcion_cuadratica, NR.derivada_cuadratica, 1, 100, 0.0001)
    except ValueError:
        return "Error: Ingresa números enteros válidos"

# Campo de entrada para X1
label_s = tk.Label(raiz, text="Valor X1:")
label_s.pack()
entry_s = tk.Entry(raiz)
entry_s.pack()

# Campo de entrada para iteraciones
label_i = tk.Label(raiz, text="Número de iteraciones")
label_i.pack()
entry_i = tk.Entry(raiz)
entry_i.pack()

# Campo de entrada para error
label_o = tk.Label(raiz, text="Error tolerable")
label_o.pack()
entry_o = tk.Entry(raiz)
entry_o.pack()

# Botón para mostrar mensaje
btn_mostrar = tk.Button(raiz, text="Raíz", command=mostrar_raiz)
btn_mostrar.pack()

def graficar():
    valor_i = int(entry_i.get())
    valor_s = int(entry_s.get())
    valor_o = int(entry_o.get())
    pass



btn_graficar = tk.Button(raiz, text="Graficar", command=graficar)
btn_graficar.pack()

raiz.mainloop()
