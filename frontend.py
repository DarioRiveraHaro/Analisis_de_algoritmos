import tkinter as tk

root = tk.Tk()

root.title("Visualizador de Resultados")
root.geometry("1060x500")  # Tamaño de la ventana

# Botón para abrir el archivo
btn_abrir = tk.Button(root, text="Abrir archivo CSV")
btn_abrir.place(x=570, y=450)

# Botón para mostrar los resultados
btn_mostrar = tk.Button(root, text="Mostrar resultados")
btn_mostrar.place(x=450, y=450)

# Etiqueta para mostrar la cadena original
lbl_cadena_original = tk.Label(root, text="Cadena Original:")
lbl_cadena_original.place(x=10, y=10)
txt_cadena_original = tk.Text(root, height=2, width=130, state="disabled")
txt_cadena_original.place(x=10, y=30)

# Mostrar cadenas
txt_cadenas_modificadas = tk.Text(root, height=10, width=130, state="disabled")
txt_cadenas_modificadas.place(x=10, y=140)

# Campo de entrada para el número de chunk
lbl_chunk = tk.Label(root, text="Número de chunk:")
lbl_chunk.place(x=10, y=90)
entry_chunk = tk.Entry(root)
entry_chunk.place(x=10, y=110)

# Botón para mostrar el chunk seleccionado
btn_mostrar_chunk = tk.Button(root, text="Mostrar Chunk Modificado")
btn_mostrar_chunk.place(x=150, y=105)

root.mainloop()