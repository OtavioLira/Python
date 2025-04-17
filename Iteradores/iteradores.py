tupla = ("laranja", "pessego", "manga")
myiter = iter(tupla) # Cria um iterador a partir da tupla

print(next(myiter)) # Imprime o primeiro elemento da tupla
print(next(myiter)) # Imprime o Segundo elemento da tupla
print(next(myiter)) # Imprime o Terceiro elemento da tupla

# Iterando com strings
string = "banana"

myiter = iter(string) # Cria um iterador a partir da string

print(next(myiter)) # Imprime o primeiro elemento da string
print(next(myiter)) # Imprime o segundo elemento da string
print(next(myiter)) # Imprime o terceiro elemento da string
print(next(myiter)) # Imprime o quarto elemento da string
# Assim por diante...

# Também podemos usar o for loop para iterar por um objeto iterável.

for letra in string:
    print(letra) # Imprime cada letra da string

# O for loop na verdade cria um objeto iterador por trás dos panos e executa o next() para cada loop