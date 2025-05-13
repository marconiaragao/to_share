# ===============================
# COMANDOS BÁSICOS EM PYTHON 
# ===============================

# PRINT: imprime algo na tela
print("Olá, mundo! Victor passou por aqui e agora vai com assinatura verified!")

# VARIÁVEIS: armazenam valores
nome = "João"
idade = 30

# TIPOS BÁSICOS:
inteiro = 10               # int
decimal = 3.14             # float
texto = "Python"           # str
verdadeiro = True          # bool

# INPUT: entrada de dados pelo usuário
nome_usuario = input("Digite seu nome: ")

# CONVERSÃO DE TIPOS:
numero = int("10")         # converte string para inteiro
altura = float("1.75")     # converte string para float
idade_str = str(30)        # converte inteiro para string

# OPERADORES ARITMÉTICOS:
# + adição, - subtração, * multiplicação, / divisão
# // divisão inteira, % módulo (resto), ** exponenciação
soma = 5 + 3
potencia = 2 ** 3

# CONDICIONAIS:
if idade >= 18:
    print("Maior de idade")
elif idade > 12:
    print("Adolescente")
else:
    print("Criança")

# ESTRUTURAS DE REPETIÇÃO:
# WHILE: enquanto a condição for verdadeira
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# FOR: percorre uma sequência
for i in range(5):  # range(5) vai de 0 até 4
    print("Número:", i)

# LISTAS:
frutas = ["maçã", "banana", "uva"]
frutas.append("laranja")         # adiciona item
frutas.remove("banana")          # remove item
print(frutas[0])                 # acessa o primeiro item

# DICIONÁRIOS:
pessoa = {"nome": "Ana", "idade": 25}
print(pessoa["nome"])           # acessa valor pela chave
pessoa["idade"] = 26            # atualiza valor

# FUNÇÕES:
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Lucas")

# IMPORTAÇÃO DE MÓDULOS:
import math
print(math.sqrt(16))  # raiz quadrada de 16

# EXCEÇÕES (tratamento de erros):
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Não é possível dividir por zero.")

# CRIAÇÃO DE CLASSES (POO):
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Carlos", 40)
p1.apresentar()

# ===============================
# FIM DOS COMANDOS BÁSICOS
# ===============================