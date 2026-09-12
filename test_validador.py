from validador import ValidaSenha

def test_senha_valida():
    assert ValidaSenha("Teste123") == True

def test_senha_7_caracteres():
    assert ValidaSenha("Teste12") == False

def test_senha_8_caracteres_minusculo():
    assert ValidaSenha("teste123") == False

def test_senha_8_caracteres_sem_numero_com_maiuscula():
    assert ValidaSenha("Testedos") == False

def test_senha_8_caracteres_so_maiuscula():
    assert ValidaSenha("TESTEDOS") == False

def test_senha_8_caracteres_maiuscula_e_numero_sem_minuscula():
    assert ValidaSenha("TESTE123") == False

def test_senha_8_caracteres_so_minuscula():
    assert ValidaSenha("testedos") == False

def test_senha_7_caracteres_maiuscula_e_minuscula():
    assert ValidaSenha("Testedo") == False

def test_senha_7_caracteres_so_maiuscula():
    assert ValidaSenha("TESTEDO") == False

def test_senha_7_caracteres_maiuscula_e_numero():
    assert ValidaSenha("TESTE12") == False

def test_senha_7_caracteres_so_minuscula():
    assert ValidaSenha("testedo") == False

def test_senha_vazia():
    assert ValidaSenha("") == False

def test_senha_none():
    assert ValidaSenha(None) == False