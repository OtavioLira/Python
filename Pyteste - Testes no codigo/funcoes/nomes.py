from funcao import get_fromatted_name

print("Digite 'q' a qualquer momento para sair.")
while True:
    first_name = input("Digite seu primeiro nome: ")
    if first_name == 'q':
        break
    last_name = input("Digite seu sobrenome: ")
    if last_name == 'q':
        break

    formatted_name = get_fromatted_name(first_name, last_name)
    print(f"\nNome formatado: {formatted_name}\n")