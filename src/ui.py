import tkinter as tk
from tkinter import messagebox
from compiler import analizar


def iniciar_app():

    ventana = tk.Tk()
    ventana.title("TRADUCTOR DE EMOJIS")
    ventana.geometry("900x600")
    ventana.config(bg="#1e1e1e")

    def compilar():
        texto = entrada.get().strip()

        if texto == "":
            messagebox.showwarning("Advertencia", "Debes escribir texto")
            return

        resultado_final = analizar(texto)
        resultado.config(text=resultado_final)

    def limpiar():
        entrada.delete(0, tk.END)
        resultado.config(text="")

    titulo = tk.Label(
        ventana,
        text="TRADUCTOR DE EMOJIS",
        font=("Arial", 24, "bold"),
        bg="#1e1e1e",
        fg="#00ff99"
    )
    titulo.pack(pady=20)

    entrada = tk.Entry(
        ventana,
        width=40,
        font=("Arial", 16)
    )
    entrada.pack(pady=20)

    tk.Button(
        ventana,
        text="COMPILAR",
        command=compilar
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="LIMPIAR",
        command=limpiar
    ).pack(pady=10)

    resultado = tk.Label(
        ventana,
        text="",
        font=("Arial", 30),
        bg="#1e1e1e",
        fg="white"
    )
    resultado.pack(pady=30)

    ventana.mainloop()