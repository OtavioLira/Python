from cidade_funcao import cidade_pais

def test_cidade_pais():
    # Teste com cidade e país
    resultado = cidade_pais('Recife', 'Brasil')
    assert resultado == 'Recife, Brasil'

    # Teste com cidade e país diferentes
    resultado = cidade_pais('Paris', 'França')
    assert resultado == 'Paris, França'