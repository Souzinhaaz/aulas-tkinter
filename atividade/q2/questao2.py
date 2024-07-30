import tkinter as tk


class Aplicativo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.janela_principal()
        self.tela_principal()

    def janela_principal(self):
        self.title("Atividade 2")
        self.geometry("500x600+700+200")
        self.resizable(False, False)
        self.minsize(500, 600)
        self.maxsize(500, 600)

    def tela_principal(self):

        def somar():
            try:
                n1 = float(num1.get())
                n2 = float(num2.get())

                soma = n1 + n2

                resultado = tk.Label(self.frame1, text=f"A soma dos valores é {soma:.2f}", font="Arial 16 bold", foreground="green")
                resultado.pack(pady=20)
            except:
                erro = tk.Label(self.frame1, text="Os valores inseridos são inválidos!", font="Arial 16 bold", foreground="red")
                erro.pack(pady=20)

        self.frame1 = tk.Frame(self, width=400, height=400)
        self.frame1.pack(fill="both", expand=True)

        texto = tk.Label(self.frame1, text="Informe dois números para realizar a soma!")
        texto.config(font="Arial 14 bold")
        texto.pack(padx=5, pady=30)

        num1 = tk.Entry(self.frame1, font="Arial 14")
        num1.pack(pady=20, ipadx=20, ipady=10)

        sinal = tk.Label(self.frame1, text="+", font="Arial 18")
        sinal.pack()

        num2 = tk.Entry(self.frame1, font="Arial 14")
        num2.pack(pady=20, ipadx=20, ipady=10)

        botao_somar = tk.Button(self.frame1, text="Somar", relief="solid", border=2)
        botao_somar.config(font="Arial 12 bold", foreground="white", bg="red", command=somar)
        botao_somar.pack(ipadx=5, ipady=5)
        
        

# Principal
if __name__ == '__main__':
    app = Aplicativo()
    app.mainloop()
