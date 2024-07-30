import tkinter as tk
from tkinter import messagebox
from conexao import ConexaoBD


class Aplicativo(tk.Tk, ConexaoBD):
    def __init__(self):
        super().__init__()
        self.janela_principal()
        self.tela_principal()

    def janela_principal(self):
        self.title("Atividade 3")
        self.geometry("500x600+700+200")
        self.resizable(False, False)
        self.minsize(500, 600)
        self.maxsize(500, 600)

    def tela_principal(self):

        def fazer_login():
            user = entry_usuario.get()
            password = entry_senha.get()
            entry_usuario.delete(0, "end")
            entry_senha.delete(0, "end")
            
            usuario = self.buscar_usuario(user, password)
            if not usuario:
                messagebox.showerror("Login", "Usuário ou senha incorretos")
            else:
                self.tela_sucesso()

        self.frame1 = tk.Frame(self, width=400, height=400)
        self.frame1.pack(fill="both", expand=True)

        texto = tk.Label(self.frame1, text="Fazer login")
        texto.config(font="Arial 18 bold", bg="black", fg="white")
        texto.pack(ipady=30, fill="x")

        lbl_usuario = tk.Label(self.frame1, text="Digite o nome do usuário", font="Arial 14 bold")
        lbl_usuario.pack(pady=10)

        entry_usuario = tk.Entry(self.frame1, font="Arial 14")
        entry_usuario.pack(ipadx=20, ipady=10)

        lbl_senha = tk.Label(self.frame1, text="Digite a senha do usuário", font="Arial 14 bold")
        lbl_senha.pack(pady=5)

        entry_senha = tk.Entry(self.frame1, font="Arial 14", show="*")
        entry_senha.pack(ipadx=20, ipady=10)

        botao_logar = tk.Button(self.frame1, text="Fazer Login", relief="solid", border=2)
        botao_logar.config(font="Arial 12 bold", foreground="white", bg="green", command=fazer_login)
        botao_logar.pack(pady=20, ipadx=5, ipady=5)

    def tela_sucesso(self):

        def voltar_login():
            self.frame2.pack_forget()
            self.tela_principal()

        self.frame1.pack_forget()

        self.frame2 = tk.Frame(self, width=400, height=400)
        self.frame2.pack(fill="both", expand=True)

        texto = tk.Label(self.frame2, text="Login realizado com sucesso")
        texto.config(font="Arial 18 bold", bg="green", fg="white")
        texto.pack(ipady=30, fill="x")

        botao_voltar = tk.Button(self.frame2, text="Voltar para a tela principal", relief="solid", border=2)
        botao_voltar.config(font="Arial 12 bold", foreground="white", bg="green", command=voltar_login)
        botao_voltar.pack(pady=20, ipadx=5, ipady=5)


# Principal
if __name__ == "__main__":
    app = Aplicativo()
    app.mainloop()
