import tkinter as tk
from tkinter import messagebox

class Aplicativo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.janela_principal()

    def janela_principal(self):
        def clique():
            print("Usuário:", entrada_usuario.get())
            print("Senha:", entrada_senha.get())
            entrada_usuario.delete(0, 'end')
            entrada_senha.delete(0, 'end')
            messagebox.showinfo("Login", "Login realizado com sucesso!")

        cor_bg = "#10AAB0"
        cor_botao = "#0F7"
        self.geometry("400x400")
        self.title("Meu APP")
        self.maxsize(600, 0)
        self.minsize(300, 0)
        self.wm_attributes('-toolwindow', 'True')
        self.configure(
            bg=cor_bg,
        )
        self.resizable(True, False)

        # Header
        login = tk.Label(self, text="Login")
        login.configure(bg="#000", 
                        fg="#fff",
                        font="Arial 18")
        login.pack(fill="x", ipady=20)

        lbl_usuario = tk.Label(self, text="Usuário")
        lbl_usuario.configure(bg=cor_bg, fg="#000", font="Arial 17 bold")
        lbl_usuario.pack(ipady=10)

        entrada_usuario = tk.Entry(self,
            font="Arial 14"
        )
        entrada_usuario.pack()

        label_senha = tk.Label(self, text="Senha")
        label_senha.configure(bg=cor_bg, fg="#000", font="Arial 17 bold")
        label_senha.pack(ipady=10)

        entrada_senha = tk.Entry(self,
            font="Arial 14",
            show="*"
        )
        entrada_senha.pack()

        botao = tk.Button(self, text="Entrar")
        botao.configure(bg=cor_botao, fg="#000", font="Arial 17 bold", relief="solid", border=2, command=clique)
        botao.pack(pady=25, ipady=5, ipadx=5)

# Principal
app1 = Aplicativo()
app1.mainloop()