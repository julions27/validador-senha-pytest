def ValidaSenha(senha):
    if senha is None:
        return False
    else:
        if len(senha) >= 8 and tem_maiuscula(senha) and tem_minuscula(senha) and tem_numero(senha):
            return True
        else:
            return False
        
        
def tem_maiuscula(senha):
    count = 0
    for i in range (len(senha)):
        if senha[i].isupper():
            count = count+1
    if count > 0:
        return True
    else:
        return False
    
def tem_minuscula(senha):
    count = 0
    for i in range (len(senha)):
        if senha[i].islower():
            count = count+1
    if count > 0:
        return True
    else:
        return False
    
def tem_numero(senha):
    count = 0
    for i in range (len(senha)):
        if senha[i].isdigit():
            count = count+1
    if count > 0:
        return True
    else:
        return False
    
def main():
    x = input("Senha:")
    if ValidaSenha(x):
        print("Deu certo")
    else:
        print("Deu errado")
        
if __name__ == "__main__": main()