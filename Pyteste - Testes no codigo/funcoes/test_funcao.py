from funcao import get_formatted_name

# Exemplo de teste unitário com Pytest
def test_first_name():
    #formatted_name = get_fromatted_name('otavio', 'lira')
    formatted_name = get_formatted_name('otavio', 'lira')
    assert formatted_name == "Otavio Lira"

def test_first_middle_last_name():
    #formatted_name = get_fromatted_name('otavio', 'lira', 'silva')
    formatted_name = get_formatted_name(first_name='otavio', middle_name='lira', last_name='neves')
    assert formatted_name == "Otavio Lira Neves"

# Comando para testar todos os testes: pytest
# Comando para testar um arquivo específico: pytest '.\Pyteste - Testes no codigo\test_funcao.py'