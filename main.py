import tkinter as tk


def click(button):
    current = entry.get()
    if button == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Erro")
    elif button == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button)


root = tk.Tk()
root.title("Calculadora")

# Definindo tamanho base da janela da calculadora

largura_janela = 380
altura_janela = 420

root.geometry(f"{largura_janela}x{altura_janela}")
root.resizable(False, False)

# Visor de números

entry = tk.Entry(root, width=20, font=('Arial', 18),
                 borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Botão C do lado do visor

tk.Button(root, text='C', width=5, height=2, font=('Arial', 18), command=lambda: click('C')
          ).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

# Botões da calculadora

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

# Botões na interface

for button in buttons:
    def action(x=button): return click(x)
    tk.Button(root, text=button, width=5, height=2, font=('Arial', 18),
              command=action).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
