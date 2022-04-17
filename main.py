from tkinter import *
from tkinter import ttk

# Instancia o objeto
janela = Tk()

# Define o título da janela
janela.title("Conversor")
# janela.geometry("200x320")

# Define um texto de cabeçalho e a sua posição na janela
lblAviso = Label(janela, text="Selecione as escalas para conversão: ")
# lblAviso.grid(column=2, row=2)
lblAviso.pack()

# Define os dados de uma caixa de combinação não editável e sua posição na janela
cbEscalas1 = ttk.Combobox(janela, state="readonly", values=["Celsius", "Fahrenheit", "Kelvin"])
# cbEscalas1.grid(column=2, row=3, padx=4, pady=4)
cbEscalas1.pack()

# Define um texto e a sua posição na janela
lblPara = Label(janela, text="para")
# lblPara.grid(column=2, row=4)
lblPara.pack()

# Define os dados de uma caixa de combinação não editável e sua posição na janela
cbEscalas2 = ttk.Combobox(janela, state="readonly", values=["Celsius", "Fahrenheit", "Kelvin"])
# cbEscalas2.grid(column=2, row=5, padx=4, pady=4)
cbEscalas2.pack()

# Define um texto e a sua posição na janela
lblEntradaTemperatura = Label(janela, text="Informe a temperatura: ")
# lblEntradaTemperatura.grid(column=2, row=6,padx=15, pady=15)
lblEntradaTemperatura.pack()

txtEntradaTemperatura = Text(height=1, width=17)
# txtEntradaTemperatura.grid(column=2, row=7, padx=4, pady=4)
txtEntradaTemperatura.pack()

# Define as características de um botão e sua posição na janela
btnConverter = Button(janela, text="Converter")
# btnConverter.grid(column=2, row=8, padx=15, pady=15)
btnConverter.pack()
# Define um texto e a sua posição na janela
lblConvertida = Label(janela, text="Temperatura convertida: ")
# lblConvertida.grid(column=2, row=9)
lblConvertida.pack()

txtConvertido = Text(height=1, width=17)
# txtConvertido.grid(column=2, row=10, padx=2, pady=15)
txtConvertido.insert(1.0, "")
txtConvertido.pack()

# Faz com que a janela permaneça aparecendo até que eu a feche
janela.mainloop()
