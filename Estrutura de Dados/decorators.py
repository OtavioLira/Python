def simple_decorator(func):
    def wrapper():
        print("Antes da função ser chamada.")
        func() #minha_funcao()
        print("Depois da função ser chamada.")
    return wrapper

@simple_decorator
def minha_funcao():
    print("Executando a função principal.")

# Chamando a função decorada
minha_funcao()