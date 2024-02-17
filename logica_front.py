import customtkinter
import pandas as pd
from PIL import Image, ImageTk

import main
import uteis



imagem= Image.open(r"C:\\Users\\Public\\apis\\fotinha.jpg")
fundo= customtkinter.CTkImage(imagem)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
janela= customtkinter.CTk()
janela.geometry("1920x1080")

tela = customtkinter.CTk()
tela.geometry("500x300")

texto2= customtkinter.CTkLabel(tela,text="Faça seu Login")
texto2.pack(padx=10,pady=15)

cadastro1 = customtkinter.CTk()
tela.geometry("768x1024")

def moverbotao():
    x,y = botao2.winfo_x(), botao2.winfo_y()
    x=20
    novo_y= y+1
    botao2.place(x=x,y=novo_y)
    janela.after(10, moverbotao)
    if novo_y>=80:
        novo_y=80
        botao2.place(x=x, y=80)
def click():
    moverbotao()
def click2():
    print("Abrir aba de categorias")
    botao2.place(x=20,y=80)

def click3():
    print('meu ovo')
    tela.mainloop()
def clickcadastro():
    cadastro1.mainloop()

def envia_cadastro():
    nome1= str(nome_cadastro.get())
    idade1=idade_cadastro.get()
    check=cpf_cadastro.get()
    print('este é o check',check)
    valid= ''.join(map(str,uteis.validacpf(check)))
    print('este é o retorno apos validar ',valid,type(valid))
    cpf1 =uteis.criptografia(valid)
    print('esse é o cpf1',cpf1,type(cpf1))
    genero1= genero_cadastro.get()
    local1 = local_cadastro.get()
    email1 = uteis.criptografia(email_cadastro.get())
    senha1 = uteis.criptografia(senha_cadastro.get())
    main.cadastro(nome1,idade1,cpf1,genero1,local1,email1,senha1)
    print(nome1,senha1,idade1,cpf1,genero1,local1,email1)


def fazerlogin():
    acessop1 = str(uteis.criptografia(email.get()))
    print(acessop1)
    acessop2 = str(uteis.criptografia(senha.get()))
    print(acessop2)
    login_valido = main.logar(acessop1)
    senha_valida = main.chave(acessop2)
    acesso_valido = main.log2(acessop1, acessop2)

    if login_valido and senha_valida and acesso_valido:
        fundo
        janela_vendedor.mainloop()
    elif login_valido and senha_valida:
        janela_cliente.mainloop()
    else:
        return False

texto = customtkinter.CTkLabel(janela, text="Tela principal")
texto.place(x=960,y=20)

pesquisa= customtkinter.CTkEntry(janela,placeholder_text="Pesquisa")
pesquisa.place(x=20,y=20)

botao = customtkinter.CTkButton(janela,text="Categorias",command= click)
botao.place(x=20,y=50)

botao2= customtkinter.CTkButton(janela,text="lista de categorias",command=click2)
botao2.place(x=20,y=50)

botao3= customtkinter.CTkButton(janela,text="Login",command=click3)
botao3.place(x=1600, y=5)



email= customtkinter.CTkEntry(tela,placeholder_text="Insira seu Email")
email.pack(padx=10,pady=5)

senha= customtkinter.CTkEntry(tela,placeholder_text="Insira sua Senha",show="*")
senha.pack(padx=10,pady=5)

checkbox= customtkinter.CTkCheckBox(tela,text="Lembrar senha")
checkbox.pack(padx=5,pady=5)

botaologin= customtkinter.CTkButton(tela,text="Login",command=fazerlogin)
botaologin.pack(padx=10,pady=5)

botaocadastro= customtkinter.CTkButton(tela,text="Cadastre-se",command=clickcadastro)
botaocadastro.pack(padx=10,pady=10)

nome_cadastro=customtkinter.CTkEntry(cadastro1,placeholder_text="Seu nome")
nome_cadastro.pack(padx=10,pady=10)

email_cadastro= customtkinter.CTkEntry(cadastro1,placeholder_text="digite seu email")
email_cadastro.pack(padx=10,pady=5)

senha_cadastro= customtkinter.CTkEntry(cadastro1,placeholder_text="Digite sua senha",show="*")
senha_cadastro.pack(padx=10,pady=10)


genero_cadastro= customtkinter.CTkEntry(cadastro1,placeholder_text="Qual genero você se identifica")
genero_cadastro.pack(padx=10,pady=10)

cpf_cadastro=customtkinter.CTkEntry(cadastro1,placeholder_text="Digite seu cpf")
cpf_cadastro.pack(padx=10,pady=10)

idade_cadastro=customtkinter.CTkEntry(cadastro1,placeholder_text="Quantos anos você tem")
idade_cadastro.pack(padx=10,pady=10)

local_cadastro=customtkinter.CTkEntry(cadastro1,placeholder_text="Digite a sua cidade e seu estado")
local_cadastro.pack(padx=10,pady=10)

botao4=customtkinter.CTkButton(cadastro1,text="concluir cadastro",command=envia_cadastro)
botao4.pack(padx=10,pady=10)




import customtkinter as ctk


janela_vendedor = ctk.CTk()
janela_vendedor.geometry("400x200")

# Definindo uma nova fonte com tamanho muito grande
fonte_maior = ("Helvetica", 36)

# Criando um label com texto muito grande
texto_muito_grande = ctk.CTkLabel(janela_vendedor, text="Bem vindo vendedor", font=fonte_maior)
texto_muito_grande.pack(pady=20)

botao_dash=customtkinter.CTkButton(janela_vendedor,text="Dash-Board")
botao_dash.pack(padx=10,pady=10)

botao_cadastro=customtkinter.CTkButton(janela_vendedor,text="Cadastrar Produto")
botao_cadastro.pack(padx=10,pady=10)

botao_mprodutos=customtkinter.CTkButton(janela_vendedor,text="Meus Produtos")
botao_mprodutos.pack(padx=10,pady=10)

janela.mainloop()

janela_cliente = ctk.CTk()
janela_cliente.geometry("400x200")

#def escolha():
   # tabela=pd.read_excel(r"C:\Users\Public\apis\produtos\produtos.xlsx")
    #botoes_id= tabela.shape[1]
    #categorias = tabela.columns
    #btm=customtkinter.CTkButton(janela_cliente,text='tabela.columns',)
    #btm.pack(padx=10,pady=10)
    #for categoria  in categorias:
      #botao = customtkinter.CTkButton(janela_cliente, text=coluna)
        #botao.pack(padx=10, pady=10)
        #botoes.append(botao)

