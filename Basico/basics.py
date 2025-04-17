print("\n=-=-=Variaveis e Tipos=-=-=")

""" O Python tem os seguintes tipos de dados incorporados por padrão, nestas categorias:

Tipo de texto:	str
Tipos numéricos:	int, float, complex
Tipos de sequência:	list, tuple, range
Tipo de mapeamento:	dict
Tipos de conjuntos:	set,frozenset
Tipo booleano:	bool
Tipos binários:	bytes, bytearray, memoryview
Nenhum Tipo:	NoneType

"""

texto = "Hello World!" # String
numeros_inteiros = 10 # int
numeros_flutuantes = 2.7 # float
boolean = True # or fals

# Atribuir valores a várias variáveis ​​em uma linha 
maça, banana, abacaxi = "maçã", "banana", "abacaxi"

# Exibindo resultados no console
print(texto)
print(numeros_inteiros)
print(numeros_flutuantes)
print(boolean)
print(maça, banana, abacaxi)

# para saber um tipo de uma variavel
print(type(boolean))


print("\n=-=-=Condicionais=-=-=")

# If
a = 33
b = 200
if b > a:
    print("B é maior que A")
# If Else
if b > a:
    print("B é maior que A")
else:
    print("B é menor ou igual a A")

# Elif 
if b > a:
    print("B é maior que A")
elif b == a:
    print("B é igual a A")
else:
    print("B é menor a A")

# Escrevendo de forma curta
if a > b: print("A é maior que B") # If curto
print ("a") if a > b else print("b") # If else curto
print ("A") if a > b else print("=") if a == b else print("B") # Escrevendo com 3 condições

# Operadores logico
# AND (E)
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Ambas as condições são verdadeiras")

#OR (Ou)
if a > b or a > c:
    print("Pelo menos uma das condições são verdadeiras")

# Not (não)
if not a > b:
    print("a NÃO é maior que B")


print("\n=-=-=Loops=-=-=")

# While Loop - execute enquanto (condição) for verdadeira
i = 1
while i < 6:
    print(i)
    i += 1
# Resultado: 1 2 3 4 5
print() # Para apenas pular linha

i = 1
while i < 6:
  print(i)
  if i == 3:
    break # Para a iteração do loop
  i += 1
# Resultado: 1 2 3
print() # Para apenas pular linha

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue # Continua a iteração do loop
  print(i)
print() # Para apenas pular linha

# Com a declaração "ELSE"
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i não é mais menor que 6")

print() # Para apenas pular linha


# For - execute até chegar no resultado final ou cumprir com a condição
frutas = ["maça", "banana", "cereja"]
for fruta in frutas:
   print(fruta) 

print() # Para apenas pular linha

# Loop para percorer uma string
for x in "banana":
   print(x)
print()

# Com o parametro Break
frutas = ["maça", "banana", "cereja"]
for fruta in frutas:
   print(fruta) 
   if fruta == "banana":
      break # Caso troque o Continue ele vai contiuar (é mesmo é?) o loop caso tenho a fruta banana 

print("\n=-=-=Tratamento de Exceções=-=-=")

# O bloco try gerará uma exceção, porque x não está definido:
try:
    print(x)
except:
    print("Um erro ocorreu")

# Com varias exeções
try:
   print(x)
except NameError:
   print("Variavel x não está definida")
except:
   print("Alguma coisa deu errado")

# Você pode usar a palavra-chave else para definir um bloco de código a ser executado se nenhum erro for gerado
try:
   print("Olá")
except:
   print("Alguma coisa deu errado")
else:
   print("Nada deu errado")

# declaração Finally, é executado mesmo que o bloco try gere um erro ou não
try:
   print(x)
except:
   print("Alguma coisa deu errado")
finally:
   print("O bloco 'Try Except' foi finalizado")

# Aqui você Gera um erro e interrompe o programa se x for menor que 0:
# Exemplo 1
#x = -1

#if x < 0:
#   raise Exception("Desculpe, nenhum numero abaixo de 0")

# Exemplo 2
#x = "hello"

#if not type(x) is int:
#   raise TypeError("Apenas numeros inteiros são permitidos")

print("\n=-=-=Funções=-=-=")

# Criando uma função
def minha_funcao():
   print("Ola mundo da função")

# Chamando uma função
minha_funcao()

# Função com argumentos
def minha_funcao_com_argumentos(fnome):
   print(fnome, "Santos")

minha_funcao_com_argumentos("Gustavo")
minha_funcao_com_argumentos("Jessica")
minha_funcao_com_argumentos("Ariel")

# O Python tem um conjunto de funções integradas.
print(len("palavra")) # retorna o tamanho de um objeto
print(round(2.75)) # arredonda o numer
print(str(2), type(str(2))) # Converte numeros em strings

print("\n=-=-=Listas, Tuplas, Sets e Dicionarios=-=-=")

# List
minha_lista = ["laranja", "pessego","manga"]
print(minha_lista)

# Tuples
minha_tupla = ("laranja", "pessego", "manga")
print(minha_tupla)

# Sets
meu_conjunto = {"laranja", "pessego", "manga"}
print(meu_conjunto)

# Dicionary
meu_dicionario = {
   "nome": "Otávio",
   "email" : "otavioliraneves@gmail.com",
   "idade": "21"
}
print(meu_dicionario)
print(meu_dicionario["nome"])

""" Diferenças
Listas: os items da lista são ordenadas, alteráveis e permitem valores duplicados.
Os items da lista são indexados, o primeiro item tem o índice [0], 
o segundo item tem indíce [1] e assim por diante.

Tuplas: os items da tupla são ordenadas, imutáveis e permitem valores duplicados.
Os items da tupla são indexados, o primeiro item tem o índice [0], 
o segundo item tem indíce [1] e assim por diante.

Sets: Conjunto é uma coleção que não é ordenada, imutável e não indexada. 
Mas você pode remover itens e adicionar novos 

Dicionarios: são usados ​​para armazenar valores de dados em pares chave:valor.
Um dicionário é uma coleção ordenada*, mutável e não permite duplicatas.

* A partir da versão 3.7 do Python, os dicionários são ordenados . No Python 3.6 e versões anteriores, os dicionários são desordenados .

"""


