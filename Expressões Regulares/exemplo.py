# Metodo RE
import re

str = "um exemplo de palavra:gato"
math = re.search(r"palavra:\w\w\w\w", str)

if math:
    print("Encontrado:", math.group()) ## 'Encontrado: palavra:gato'
else:
    print("Não encontrado")

"""
O método search() procura a string especificada e retorna um objeto de correspondência.
Se não houver correspondência, ele retorna None.
"""

# Padroes Básicos
# \d - corresponde a qualquer dígito (0-9)
# \D - corresponde a qualquer caractere que não seja um dígito
# \w - corresponde a qualquer caractere alfanumérico (letras e números)
# \W - corresponde a qualquer caractere que não seja alfanumérico
# \s - corresponde a qualquer caractere de espaço em branco (espaço, tabulação, nova linha)
# \S - corresponde a qualquer caractere que não seja um espaço em branco
# . - corresponde a qualquer caractere, exceto nova linha
# ^ - corresponde ao início da string
# $ - corresponde ao final da string
# * - corresponde a zero ou mais ocorrências do padrão anterior
# + - corresponde a uma ou mais ocorrências do padrão anterior
# ? - corresponde a zero ou uma ocorrência do padrão anterior
# {n} - corresponde exatamente a n ocorrências do padrão anterior
# {n,} - corresponde a n ou mais ocorrências do padrão anterior
# {n,m} - corresponde entre n e m ocorrências do padrão anterior

# Referências
# https://docs.python.org/3/library/re.html    
# https://developers.google.com/edu/python/regular-expressions?hl=pt-br

# Outros exemplos

# Exemplo 1: Encontrar todas as ocorrências de uma palavra
texto = "O rato roeu a roupa do rei de Roma"
resultado = re.findall(r"r\w+", texto)
print("Palavras encontradas:", resultado)  # ['rato', 'roeu', 'roupa', 'rei', 'Roma']

# Exemplo 2: Substituir palavras em uma string
texto = "Eu gosto de gatos e cachorros"
novo_texto = re.sub(r"gatos|cachorros", "animais", texto)
print("Texto modificado:", novo_texto)  # 'Eu gosto de animais e animais'

# Exemplo 3: Verificar se uma string começa com um padrão
texto = "Python é incrível"
if re.match(r"Python", texto):
    print("A string começa com 'Python'")  # 'A string começa com 'Python''

# Exemplo 4: Dividir uma string com base em um delimitador
texto = "maçã,banana,laranja"
frutas = re.split(r",", texto)
print("Lista de frutas:", frutas)  # ['maçã', 'banana', 'laranja']

# Exemplo 5: Validar um endereço de e-mail simples
email = "exemplo@dominio.com"
if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
    print("E-mail válido")  # 'E-mail válido'
else:
    print("E-mail inválido")