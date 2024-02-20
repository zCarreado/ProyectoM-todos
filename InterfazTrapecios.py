import tkinter as tk
import Trapecios as T

raiz = tk.Tk()
raiz.resizable(False, False)
raiz.geometry("650x350")

label_raiz = tk.Label(raiz, text="Aquí aparecerá el valor de la raiz")
label_raiz.pack()

def mostrar_raiz():
    try:
        valor_f = entry_f.get()
        valor_a = int(entry_s.get())
        valor_b = int(entry_o.get())
        valor_n = int(entry_i.get())
        
        label_raiz.config(text="El valor de la raiz es: "+ str(T.trapezoidal(valor_f, valor_a, valor_b, valor_n)))
        return T.trapezoidal(valor_f, valor_a, valor_b, valor_n)
    except ValueError:
        label_raiz.config(text="Error: Formato de datos incorrectos")
        return "Error: Ingresa números enteros válidos" + str(valor_f)

# Campo de entrada para función
label_f = tk.Label(raiz, text="Función")
label_f.pack()
entry_f = tk.Entry(raiz)
entry_f.pack()

# Campo de entrada para a
label_s = tk.Label(raiz, text="Valor a:")
label_s.pack()
entry_s = tk.Entry(raiz)
entry_s.pack()

# Campo de entrada b
label_o = tk.Label(raiz, text="Valor b:")
label_o.pack()
entry_o = tk.Entry(raiz)
entry_o.pack()

# Campo de entrada para iteraciones
label_i = tk.Label(raiz, text="Número de iteraciones")
label_i.pack()
entry_i = tk.Entry(raiz)
entry_i.pack()

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
