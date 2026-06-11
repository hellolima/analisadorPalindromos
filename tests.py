
import src

#teste 1: string vazia
def test_string_vazia():
    assert src.eh_palindromo("") == True

#teste 2: string com espacos
def test_string_com_espacos():
    assert src.eh_palindromo("a base do teto desaba") == True
    assert src.eh_palindromo("o lobo ama o bolo") == True

#teste 3: string com numeros
def test_string_com_numeros():
    assert src.eh_palindromo("12321") == True
    assert src.eh_palindromo("123") == False

#teste 4: string com caracteres especiais
def test_string_com_caracteres_especiais():
    assert src.eh_palindromo("socorram-me, subi no onibus em marrocos") == True

#teste 5: string com caixas altas e baixas
def test_string_com_caixas_altas_e_baixas():
    assert src.eh_palindromo("AraRa") == True
    assert src.eh_palindromo("Ana") == True

#teste 6: formato invalido
def test_formato_invalido():
    try:
        assert src.eh_palindromo(12321321) == False
    except TypeError:
        # Se der erro de tipo, também consideramos que passou, já que não é string
        pass

if __name__ == "__main__":
    print("Executando testes...")
    test_string_vazia()
    print("✅ test_string_vazia passou!")
    
    try:
        test_string_com_espacos()
        print("✅ test_string_com_espacos passou!")
    except AssertionError:
        print("❌ test_string_com_espacos falhou!")
        
    test_string_com_numeros()
    print("✅ test_string_com_numeros passou!")
    
    try:
        test_string_com_caracteres_especiais()
        print("✅ test_string_com_caracteres_especiais passou!")
    except AssertionError:
        print("❌ test_string_com_caracteres_especiais falhou!")
        
    test_string_com_caixas_altas_e_baixas()
    print("✅ test_string_com_caixas_altas_e_baixas passou!")
    
    test_formato_invalido()
    print("✅ test_formato_invalido passou!")
    
    print("Fim dos testes.")
