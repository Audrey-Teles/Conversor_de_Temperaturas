from tkinter import messagebox


def celsiusFahrenheit(c):
    try:
        f = (float(c) * 1.8) + 32
        return f
    except:
        messagebox.showerror("Erro", "Informe um valor válido")


def celsiusKelvin(c):
    try:
        k = float(c) + 273
        return k
    except:
        messagebox.showerror("Erro", "Informe um valor válido")


def fahrenheitCelsius(f):
    try:
        c = (float(f) - 32)/1.8
        return c
    except:
        messagebox.showerror("Erro", "Informe um valor válido")


def fahrenheitKelvin(f):
    try:
        k = ((float(f) - 32) * 5/9) + 273
        return k
    except:
        messagebox.showerror("Erro", "Informe um valor válido")


def kelvinFahrenheit(k):
    try:
        f = ((float(k) - 273) * 9/5) + 32
        return f
    except:
        messagebox.showerror("Erro", "Informe um valor válido")


def kelvinCelsius(k):
    try:
        c = float(k) - 273
        return c
    except:
        messagebox.showerror("Erro", "Informe um valor válido")

