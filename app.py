import tkinter as tk
from tkinter import messagebox
import csv

class CadastroClientes:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Clientes")

        # Variáveis para armazenar dados do cliente
        self.nome_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.telefone_var = tk.StringVar()
        self.rua_var = tk.StringVar()
        self.numero_var = tk.StringVar()
        self.bairro_var = tk.StringVar()
        self.cidade_var = tk.StringVar()
        self.cep_var = tk.StringVar()
        self.estado_var = tk.StringVar()
        self.idade_var = tk.StringVar()

        # Layout
        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nome = tk.Entry(root, textvariable=self.nome_var)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)

        self.label_email = tk.Label(root, text="E-mail:")
        self.label_email.grid(row=1, column=0, padx=10, pady=10)
        self.entry_email = tk.Entry(root, textvariable=self.email_var)
        self.entry_email.grid(row=1, column=1, padx=10, pady=10)

        self.label_telefone = tk.Label(root, text="Telefone:")
        self.label_telefone.grid(row=2, column=0, padx=10, pady=10)
        self.entry_telefone = tk.Entry(root, textvariable=self.telefone_var, validate="key", validatecommand=(root.register(self.validar_telefone), "%P"))
        self.entry_telefone.grid(row=2, column=1, padx=10, pady=10)

        self.label_rua = tk.Label(root, text="Rua:")
        self.label_rua.grid(row=3, column=0, padx=10, pady=10)
        self.entry_rua = tk.Entry(root, textvariable=self.rua_var)
        self.entry_rua.grid(row=3, column=1, padx=10, pady=10)

        self.label_numero = tk.Label(root, text="Número:")
        self.label_numero.grid(row=4, column=0, padx=10, pady=10)
        self.entry_numero = tk.Entry(root, textvariable=self.numero_var, validate="key", validatecommand=(root.register(self.validar_numero), "%P"))
        self.entry_numero.grid(row=4, column=1, padx=10, pady=10)

        self.label_bairro = tk.Label(root, text="Bairro:")
        self.label_bairro.grid(row=5, column=0, padx=10, pady=10)
        self.entry_bairro = tk.Entry(root, textvariable=self.bairro_var)
        self.entry_bairro.grid(row=5, column=1, padx=10, pady=10)

        self.label_cidade = tk.Label(root, text="Cidade:")
        self.label_cidade.grid(row=6, column=0, padx=10, pady=10)
        self.entry_cidade = tk.Entry(root, textvariable=self.cidade_var)
        self.entry_cidade.grid(row=6, column=1, padx=10, pady=10)

        self.label_cep = tk.Label(root, text="CEP:")
        self.label_cep.grid(row=7, column=0, padx=10, pady=10)
        self.entry_cep = tk.Entry(root, textvariable=self.cep_var, validate="key", validatecommand=(root.register(self.validar_cep), "%P"))
        self.entry_cep.grid(row=7, column=1, padx=10, pady=10)

        self.label_estado = tk.Label(root, text="Estado:")
        self.label_estado.grid(row=8, column=0, padx=10, pady=10)
        self.entry_estado = tk.Entry(root, textvariable=self.estado_var)
        self.entry_estado.grid(row=8, column=1, padx=10, pady=10)

        self.label_idade = tk.Label(root, text="Idade:")
        self.label_idade.grid(row=9, column=0, padx=10, pady=10)
        self.entry_idade = tk.Entry(root, textvariable=self.idade_var, validate="key", validatecommand=(root.register(self.validar_idade), "%P"))
        self.entry_idade.grid(row=9, column=1, padx=10, pady=10)

        self.botao_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_cliente)
        self.botao_cadastrar.grid(row=10, column=0, columnspan=2, pady=10)

    def validar_telefone(self, valor):
        return valor.isdigit() and len(valor) <= 11

    def validar_numero(self, valor):
        return valor.isdigit()

    def validar_cep(self, valor):
        return valor.isdigit() and len(valor) <= 8

    def validar_idade(self, valor):
        return valor.isdigit()

    def cadastrar_cliente(self):
        # Obter dados do formulário
        nome = self.nome_var.get()
        email = self.email_var.get()
        telefone = self.telefone_var.get()
        rua = self.rua_var.get()
        numero = self.numero_var.get()
        bairro = self.bairro_var.get()
        cidade = self.cidade_var.get()
        cep = self.cep_var.get()
        estado = self.estado_var.get()
        idade = self.idade_var.get()

        # Verificar se todos os campos foram preenchidos
        if nome and email and telefone and rua and numero and bairro and cidade and cep and estado and idade:
            # Formatar o telefone
            telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"

            # Adicionar cliente ao arquivo CSV
            self.adicionar_cliente_csv(nome, email, telefone_formatado, rua, numero, bairro, cidade, cep, estado, idade)

            # Limpar os campos do formulário
            self.nome_var.set('')
            self.email_var.set('')
            self.telefone_var.set('')
            self.rua_var.set('')
            self.numero_var.set('')
            self.bairro_var.set('')
            self.cidade_var.set('')
            self.cep_var.set('')
            self.estado_var.set('')
            self.idade_var.set('')

            messagebox.showinfo("Cadastro", "Cliente cadastrado com sucesso!")
        else:
            messagebox.showwarning("Cadastro", "Por favor, preencha todos os campos.")

    def adicionar_cliente_csv(self, nome, email, telefone, rua, numero, bairro, cidade, cep, estado, idade):
        # Cabeçalho do CSV
        cabecalho = ["Nome", "E-mail", "Telefone", "Rua", "Número", "Bairro", "Cidade", "CEP", "Estado", "Idade"]

        # Abrir o arquivo CSV em modo de escrita (append)
        with open('clientes.csv', 'a', newline='', encoding='utf-8') as arquivo_csv:
            # Criar um escritor CSV
            csv_writer = csv.writer(arquivo_csv)

            # Verificar se o arquivo está vazio e escrever o cabeçalho
            if arquivo_csv.tell() == 0:
                csv_writer.writerow(cabecalho)

            # Escrever os dados do cliente no arquivo
            csv_writer.writerow([nome, email, telefone, rua, numero, bairro, cidade, cep, estado, idade])

if __name__ == "__main__":
    # Criar a janela principal
    root = tk.Tk()
    app = CadastroClientes(root)
    root.mainloop()
