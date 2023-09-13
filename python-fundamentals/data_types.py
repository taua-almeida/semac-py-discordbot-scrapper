

# Indentation in Python is mandatory and replaces the braces {}
if True:
    print("Python uses Indentation to define code blocks")

# Variables
nome = "Python"
idade = 30

# Python is a dynamic language, so you don't need to specify the type of a variable
a = 10      # int
b = 20.5    # float
c = "Olá"   # string
lista = [1, 2, 3]      # list
tupla = (1, 2, 3)      # tuple
conjunto = {1, 2, 3}   # set
dicionario = {"um": 1, "dois": 2}   # dictionary

# Changing a variable type
a = "Olá"
type(a)     # <class 'str'>
a = 10
type(a)     # <class 'int'>

# Conditional statements

# if else elif
if idade > 20:
    print("Maior que 20")
elif idade == 20:
    print("Igual a 20")
else:
    print("Menor que 20")

# loops
for i in range(5):
    print(i)

contador = 0
while contador < 5:
    print(contador)
    contador += 1

# loops control
for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

if True:
    pass

# Classes
class Bolo:
    sabor = "chocolate"  # Atributo

    def assar(self):  # Método
        return "Bolo assando!"

meu_bolo = Bolo()  # Preparando um bolo seguindo a receita Bolo

print(meu_bolo.sabor)     # Saída: chocolate
print(meu_bolo.assar())   # Saída: Bolo assando!

class Bolo:
    def __init__(self, sabor):
        self.sabor = sabor

    def assar(self):  # Método
        return f"Bolo de {self.sabor} assando!"


meu_bolo = Bolo("baunilha")
print(meu_bolo.sabor)  
print(meu_bolo.assar())