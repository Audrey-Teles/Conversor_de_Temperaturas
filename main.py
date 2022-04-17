from tkinter import *
from tkinter import ttk

# Instancia o objeto
janela = Tk()

# Define o título da janela
janela.title("Conversor")
janela.geometry("250x350")

# Define um texto de cabeçalho e a sua posição na janela
Label(janela, text="Selecione as escalas para conversão: ").grid(column=2, row=2)

# Define os dados de uma caixa de combinação não editável e sua posição na janela
ttk.Combobox(janela, state="readonly", values=["Celsius", "Fahrenheit", "Kelvin"]).grid(column=2, row=3, padx=4, pady=4)

# Define um texto e a sua posição na janela
Label(janela, text="para").grid(column=2, row=4)

# Define os dados de uma caixa de combinação não editável e sua posição na janela
ttk.Combobox(janela, state="readonly", values=["Celsius", "Fahrenheit", "Kelvin"]).grid(column=2, row=5, padx=4, pady=4)

# Define um texto e a sua posição na janela
Label(janela, text="Informe a temperatura: ").grid(column=2, row=6,padx=15, pady=15)

Text(height=1, width=17).grid(column=2, row=7, padx=4, pady=4)

# Define as características de um botão e sua posição na janela
Button(janela, text="Converter").grid(column=2, row=8, padx=15, pady=15)

# Define um texto e a sua posição na janela
Label(janela, text="Temperatura convertida: ").grid(column=2, row=9)

convertido = Text(height=1, width=17)
convertido.grid(column=2, row=10, padx=2, pady=15)
convertido.insert(1.0, "")

# Faz com que a janela permaneça aparecendo até que eu a feche
janela.mainloop()
