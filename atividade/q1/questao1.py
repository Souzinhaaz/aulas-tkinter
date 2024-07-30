import tkinter as tk


class Aplicativo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.janela_principal()
        self.tela_principal()

    def janela_principal(self):
        self.title("Atividade 1")
        self.geometry("500x600+700+200")
        self.resizable(False, False)
        self.minsize(500, 600)
        self.maxsize(500, 600)

    def tela_principal(self):
        def mudar_cor_vermelho():
            self.frame1.configure(bg="red")

        def mudar_cor_verde():
            self.frame1.configure(bg="green")

        def mudar_cor_azul():
            self.frame1.configure(bg="blue")

        self.frame1 = tk.Frame(self, width=400, height=400)
        self.frame1.pack(fill="both", expand=True)

        botao_vermelho = tk.Button(self.frame1, text="Entrar", relief="solid", border=2)
        botao_vermelho.config(font="Arial 12 bold", foreground="white", bg="red", command=mudar_cor_vermelho)
        botao_vermelho.pack(pady=30, ipadx=5, ipady=5)
        
        botao_verde = tk.Button(self.frame1, text="Entrar", relief="solid", border=2)
        botao_verde.config(font="Arial 12 bold", foreground="white", bg="green", command=mudar_cor_verde)
        botao_verde.pack(pady=30, ipadx=5, ipady=5)

        botao_azul = tk.Button(self.frame1, text="Entrar", relief="solid", border=2)
        botao_azul.config(font="Arial 12 bold", foreground="white", bg="blue", command=mudar_cor_azul)
        botao_azul.pack(pady=30, ipadx=5, ipady=5)



# Principal
if __name__ == '__main__':
    app = Aplicativo()
    app.mainloop()
