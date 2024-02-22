import pandas as pd
def totais():
    tabela_user= pd.read_excel(r"C:\Users\Public\apis\clientes\dados_clientes.xlsx")
    total_pessoas= len(tabela_user.index)
    contagem_idades= tabela_user['idade'].value_counts()
    contagem_local= tabela_user['local'].value_counts()
    contagem_genero=tabela_user['genero'].value_counts()


area_interesse=pd.read_excel(r"C:\Users\Public\apis\produtos\produtos.xlsx")
print(area_interesse)

totais()

def escolha():
    tabela=pd.read_excel(r"C:\Users\Public\apis\produtos\produtos.xlsx")
    botoes_id= tabela.shape[1]
    categorias = tabela.columns
    btm=customtkinter.CTkButton(janela_cliente,text='tabela.columns',)
    btm.pack(padx=10,pady=10)
    for categoria  in categorias:
        botao = customtkinter.CTkButton(janela_cliente, text=coluna)
        botao.pack(padx=10, pady=10)
        botoes.append(botao)




# produto # produtos
#
# cat #todas as categorias
#
# usr #contagem de usuarios, recebe o indice de usuarios

# like #escolha no inicio do curso

def leitura():
    dados_excel = pd.read_excel(r"C:\Users\Public\apis\clientes\dados_clientes.xlsx")

    quantidade_de_linhas = dados_excel.shape[0]
    print(quantidade_de_linhas)
    return quantidade_de_linhas



usrs=leitura()
print(leitura)


from main import cadastro


usuario=