import tkinter as tk
import biseccion as bi

raiz = tk.Tk()
raiz.resizable(False, False)
raiz.geometry("650x350")

label_raiz = tk.Label(raiz, text="Aquí aparecerá el valor de la raiz")
label_raiz.pack()

def mostrar_mensaje():
    try:
        valor_i = int(entry_i.get())
        valor_s = int(entry_s.get())
        label_raiz.config(text="El valor de la raiz es: "+ str(bi.biseccion(valor_i, valor_s)))
        return bi.biseccion(valor_i, valor_s)
    except ValueError:
        return "Error: Ingresa números enteros válidos"

# Campo de entrada para X
label_s = tk.Label(raiz, text="Valor X:")
label_s.pack()
entry_s = tk.Entry(raiz)
entry_s.pack()

# Campo de entrada para Y
label_i = tk.Label(raiz, text="Valor Y:")
label_i.pack()
entry_i = tk.Entry(raiz)
entry_i.pack()

# Botón para mostrar mensaje
btn_mostrar = tk.Button(raiz, text="Mostrar", command=mostrar_mensaje)
btn_mostrar.pack()

def graficar():
    valor_i = int(entry_i.get())
    valor_s = int(entry_s.get())
    bi.graficar(valor_i, valor_s)
    pass



btn_graficar = tk.Button(raiz, text="Graficar", command=graficar)
btn_graficar.pack()

raiz.mainloop()
