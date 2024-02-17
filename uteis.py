from hashlib import sha256
numerocpf = []
def checknum2(numerocpf):
    acumulador2=0
    resultado2=0
    controle2=11
    for numeros2 in numerocpf[0:10]:
        resultado2 = numeros2 * controle2
        acumulador2 += resultado2
        controle2 = controle2 -1
    acumulador2 = acumulador2 * 10 % 11
    if acumulador2 == 10:
        acumulador2=0
    if acumulador2 == numerocpf[10]:
        print('check2')
        return True
    else:
        print('fcheck2')
        return False
def checknum(numerocpf):
    acumulador=0
    resultado=0
    controle=10
    for numeros in numerocpf[0:9]:
        resultado = numeros * controle
        acumulador += resultado
        controle = controle -1
    acumulador = acumulador * 10 % 11
    if acumulador == 10:
        acumulador=0
    if acumulador == numerocpf[9]:
        print('check')
        return True
    else:
        print('fcheck')
        return False

def tamanho(cpf):
    if len(cpf) < 11 or len(cpf) > 11:
        validacpf()
        return False
    else:
        return True

def numercpf(cpf):
    global numerocpf
    numerocpf=[]
    for a in cpf:
        a = int(a)
        numerocpf.append(a)
def validacpf(cpf):
    cpf = str(cpf).replace('.', '').replace('-', '')
    numercpf(cpf)
    tamanho(numerocpf)
    checknum(numerocpf)
    checknum2(numerocpf)
    if tamanho(numerocpf) == True and checknum(numerocpf) == True and checknum2(numerocpf) == True:
        print('Teste Cpf é valido numerocpf')
        return numerocpf
    else:
        printf("O cpf digitado é invalido")
        return False


def criptografia(x):
    hash_x=sha256(x.encode())
    x_salva = hash_x.digest()
    return x_salva

