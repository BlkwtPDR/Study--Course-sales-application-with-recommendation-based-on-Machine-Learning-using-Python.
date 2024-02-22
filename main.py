import pandas as pd
from hashlib import sha256
import uteis




usuarios={}
usuario=0
cursos={}
categoria={}
produtos={}


def tempcpf_check(cpf, nome):
    cpf_temp = cpf
    temp_nome = nome

    arquivon = pd.read_excel(r'C:\Users\Public\apis\pedro.xlsx')
    excel = pd.DataFrame(arquivon)

    #  coluna 'cpf' para string e aplicando a criptografia
    excel['cpf'] = excel['cpf'].astype(str).apply(uteis.criptografia)


    print('Criptografia do arquivo excel', excel['cpf'],type(excel['cpf']))

    # CPF e o nome correspondentes existem
    nome_cpf = excel[(excel['cpf'] == cpf_temp) & (excel['nome'] == temp_nome)]

    if not nome_cpf.empty:
        print('vendedor')
        return True
    else:
        print('cliente')
        return False

def cadastro_cat(produto, categor):
    global cursos

    # Leitura da tabela de cadastro de produtos
    tabela_cadastro = pd.read_excel("C:\\Users\\Public\\apis\\produtos\\categorias.xlsx")
    cursos=tabela_cadastro
    # Verifica se a categoria já existe em cursos
    if categor in cursos['categor']:
        # Verifica se o produto já existe na categoria
        if produto not in cursos['categor']['produtos']:
            cursos['categor']['produtos'].append(produto)
    else:
        # Se a categoria não existir, cria uma nova entrada
        cursos['categor'] = {'produtos': [produto]}

    # Atualiza a tabela de cadastro com os dados modificados
    tabela_atualizada = pd.DataFrame(cursos)
    tabela_atualizada=pd.concat([tabela_atualizada,tabela_cadastro],ignore_index=True)
    tabela_atualizada.to_excel("C:\\Users\\Public\\apis\\produtos\\categorias.xlsx", index=False)


def cadastrovenda():
    lista=pd.read_excel("C:\\Users\\Public\\apis\\produtos\\categorias.xlsx")
    prdct = pd.read_excel("C:\\Users\\Public\\apis\\produtos\\produtos.xlsx")
    indice=prdct.shape[0]+1
    produto=input('digite o nome do produto')
    categor=input('digite a categoria')
    cadastro_cat(produto, categor)
    nomep={}
    nomep[indice]= {
        'nome_produto':produto,
        'cat': categor,
        'valor':input('preço do Produto'),
        'timeaula':input('digite o tempo medio de aula'),
        'timecurso':input('digite o tempo do curso'),
    }


    produtos_dt=pd.DataFrame(nomep.values())
    prdct=pd.concat([prdct,produtos_dt],ignore_index=True)
    prdct.to_excel(r"C:\\Users\\Public\\apis\\produtos\\produtos.xlsx",index =False )

def acessouzr(mail):
    linha=0
    tabela=pd.read_excel(r"C:\Users\Public\apis\clientes\dados_clientes.xlsx")
    for email in tabela['email']:
        linha+=1
        if email== mail:
            return linha

def emailind(mail):
    tabl=pd.read_excel(r"C:\Users\Public\apis\clientes\dados_clientes.xlsx")
    list_mail=tabl['mail']
    if mail in list_mail:
        return True
    else:
        return False




def cadastro(nome1,idade1,cpf1,genero1,local1,email1,senha1):
    nome = nome1
    cpf =cpf1
    acessotp = tempcpf_check(cpf1,nome1)
    tabela = pd.read_excel(r"C:\Users\Public\apis\clientes\dados_clientes.xlsx")
    linhas=tabela.shape[0]
    usuario=linhas+1
    carrinho=[]
    usuarios[usuario] = {}
    usuarios[usuario] = {
        'nome': nome1,
        'idade': idade1,
        'cpf': cpf1,
        'genero': genero1,
        'local': local1,
        'email': email1,
        'senha': senha1,
        'tipoacesso': acessotp,
        'compras':carrinho
    }

    user_dt=pd.DataFrame(usuarios.values())
    tabela=pd.concat([tabela,user_dt],ignore_index=True)
    tabela.to_excel(r"C:\Users\Public\apis\clientes\dados_clientes.xlsx", index=False)



def logar(acesso):
    print(acesso)
    user = pd.read_excel(r"C:\Users\Public\apis\clientes\dados_clientes.xlsx")
    cklg = pd.DataFrame(user)
    print('email é ',cklg['email'])
    for email in cklg['email']:
        if email == acesso:
            return True
    print("login invalido")
    return False

def chave(acesso2):
    print(acesso2)
    user = pd.read_excel(r"C:\Users\Public\apis\clientes\dados_clientes.xlsx")
    cklg = pd.DataFrame(user)
    print('senha é ',cklg['senha'])
    for senha in cklg['senha']:
        if senha == acesso2:
            print('senha valida')
            return True
    print('senha invalida')
    return False


def log2(acesso, acesso2):
    doc_ck = pd.read_excel(r"C:\Users\Public\apis\clientes\dados_clientes.xlsx")
    dtf = pd.DataFrame(doc_ck)

    if logar(acesso) and chave(acesso2):
        for indice, email in enumerate(dtf['email']):
            if email == acesso:
                tipo_acesso = dtf.at[indice, 'tipoacesso']
                if tipo_acesso:
                    print('vendedor')
                    return True
        print('cliente')
        return False
# def pega_acesso(linha):
#     indice=linha
#
# nome1=input('digite o nome')
# idade1=input('digite idd')
# cpf1=uteis.criptografia(input('digite cpf'))
# genero1=input('digite gnr')
# local1=input('digite local')
# email1=input('email')
# senha1=input('digite senha')
# cadastro(nome1,idade1,cpf1,genero1,local1,email1,senha1)
#
#
#
# nome=input('Digite o nome para a funçao tempcpf')
# cpf=uteis.criptografia(input('digite o cpf pra a funçao tempcpf'))
# print(cpf,type(cpf))
# print(nome,type(nome))
# tempcpf_check(cpf,nome)

