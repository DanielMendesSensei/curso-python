"""
lista = ["Nome", 23]
dicionario = {
              "Título":"Star Wars IV",
              "Nome-da-chave":"valor da chave",
              }

print(type(dicionario.keys())) #Imprime todas as chaves
print(type(dicionario.values())) #Imprime todos os valores do dicionário
print(type(dicionario.items())) #Imprime tudo que estiver em dincionário


user = "Joãoasdas"
password = 123
lista = [1,2,3,4]

print(len(lista)) len retorna quantidade de elemento
print(len(user))
print("\n")

if user == "Daniel" and password == 123:
    print("Bem vindo ao sistema")
elif user == "João":
    print("Bem vindo João")
else:
    print("---")

for v in lista:
    print(v)
print(f"Os valores são: {lista}")
"""
"""print("Bem vindo ao sistema, faça seu login:")
user = input("Insira seu usuário: ") #Função input retorna string
password = int(input("Insira sua senha: "))

if user == "Daniel" and password == 123:
    print("Acesso liberado....")

print(user)
print(type(user))
print(password)
print(type(password))

tentativas = 3
controle = 0
while controle < tentativas:
    print("Faça seu login")
    user = input("Login: ")
    password = int(input("Senha: "))
    if user == "Daniel" and password == 123:
        print("Acesso liberado\nBem vindo ao sistema!")
        break
    else:
        print("Senha ou usuário incorreto")
    controle += 1
    if controle == 2:
        print("Senha incorreta, atenção apenas mais uma tentativa.")
    if controle == 3:
        print("Vou foi bloqueado")

petiscos = ("Torresmo", "Cerveja", "Salaminho", "Chorume Captalista")
enderc = "C:\Video-1.mp4"
print(enderc[-4],enderc[-3], enderc[-2], enderc[-1])

print(petiscos)
print(type(petiscos))
print(petiscos[0:2]) # Mostra do 1º ao 2º item
print(petiscos[1:])
print(petiscos[-2])
#print(type(petiscos[-1]))


#Incremente com exceção para valores fora do intervalo
nums = ["Zero", "Um", "Dois", "Três", "Quatro"]
print(nums)
nums.append("Cinco") #Adiciona valores no array
print(nums)
nums.insert(0, "Menos Um") #Adiciona valores no array, só vc escolhe em qual índice.
print(nums)
#del nums[2]
#nums.pop(2)
#Removendo pelo valor escrito na lista:
nums.remove("Dois") #Remove pelo valor da lista
print(nums)

if "Três" in nums:
    nums.remove("Três")

for indices, valores in enumerate(nums):
    print(f"Na posição {indices} encontrei o valor {valores}")
""""""

while True:
    num_user = int(input("Digite um número de 0 a 4: "))
    if 0 <= num_user <= 4:
        print(f"Você digitou o número {nums[num_user]}")
        break
    else:
        print("Fora do intervalo")
    print("Tente novamente.")


valores = list()
for v in range(0, 4):
    valores.append(int(input("Digite um valor: ")))
print(valores)

pessoas = [["Daniel", 25], ["João", 16]]
print(pessoas[0][0])
"""

lista_1 = list()
lista_1.append("Daniel")
lista_1.append(25)
print(lista_1)
galera = list()
galera.append(lista_1[:])
print(galera)
lista_1[0] = "Maria"











































lista_1[1] = 22
galera.append(lista_1[:])
print(galera)

"""
1.	Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a.	Quantas pessoas foram cadastradas;
b.	Uma listagem com as pessoas mais pesadas;
c.	Uma listagem com as pessoas mais leves.

$ 

2.	Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

$

3.	Crie um programa que crie uma matriz de dimensão 3x3 e preencha com os valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
$

4.	Aprimore o desafio anterior, mostrando no final:
a.	A soma de todos os valores pares digitados;
b.	A soma dos valores da terceira coluna;
c.	O maior valor da segunda linha.

$

5.	Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrado tudo em uma lista composta.

$

6.	Cria um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente. 
"""
