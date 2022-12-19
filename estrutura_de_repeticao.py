#Faça um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
import sys

# nota1 = int(input("Digite a nota:"))
#
# while nota1 > 10:
#     nota1 = int(input("Nota inválida. Tente novamente: "))
# else:
#     print("Obrigado!")

#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#mostrando uma mensagem de erro e voltando a pedir as informações.

# nome_usuario = input("Digite seu usuário: ")
# senha = input("Digite sua senha: ")
#
# while nome_usuario == senha:
#     nome_usuario = input("Seu login não pode ser igual ao senha. Insira a senha novamente:")
# else:
#     print("Login feito com sucesso!")

# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

# nome = input("Digite seu nome: ")
#     while len(nome)<4:
#     nome = input("Digite um nome com mais de 3 letras: ")
#
#     idade = int(input('Digite sua idade: '))
#     if idade>=0 and idade<=150:
#         print('A idade está correta.')
#     else:
#         print('A idade está fora dos padrões.')
#
#     salario = float(input("Digite seu salario: "))
#     while salario<=0:
#         salario = input("Digite um salário válido: ")
#
#     sexo = input("Digite seu sexo"
#                  "\nM ou F:").upper()
#     if sexo == "M":
#         print("Sexo masculino")
#     elif sexo == "F":
#         print("Sexo feminino")
#     else:
#         print("Sexo inválido")
#
#     def menu():
#         estado_civil = input("""Selecione seu estado civil:
#         S - solteiro
#         C - casado
#         V - viúvo
#         D - divorciado
#         Digite seu estado civil:""").upper()
#
#         if estado_civil == "S":
#             print("Você é solteiro")
#         elif estado_civil == "C":
#             print("Meus pesâmes, você é casado!")
#         elif estado_civil== "V":
#             print("Você é viúvo.")
#         elif estado_civil == "D":
#             print("Você é divorciado!")
#         else:
#             print("Inválido!")
#             menu()
# menu()

# Supondo que a população de um país A seja da ordem de 80000 habitantes
# com uma taxa anual de crescimento de 3% e que a população de B seja 200000
# habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule
# e escreva o número de anos necessários para que a população do país A ultrapasse
# ou iguale a população do país B, mantidas as taxas de crescimento.

# def populacao():
#     tempo = 0
#     pais_a = float(input("Digite o número de habitantes do país A: "))
#     pais_b = float(input("Digite o número de habitantes do país B: "))
#     crescimento_anual_a =  float(input("Digite a taxa de crescimento anual do país A: "))
#     crescimento_anual_b =  float(input("Digite a taxa de crescimento anual do país B: "))
#
#     while pais_a<pais_b:
#         tempo += 1
#         pais_a = (pais_a)  + (pais_a * crescimento_anual_a)
#         pais_b = (pais_b)  + (pais_b * crescimento_anual_b)
#     print("Após " + str(tempo) + " anos o país a ultrapassou o país b em número de habitantes.")
#     print("quantidade da populacao A é ",  int(pais_a) )
#     print("quantidade da populacao B é ",  int(pais_b) )
#     populacao()
#
# populacao()

# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

# for x in range(0,21):
#     print(x, end=" ")

#Faça um programa que leia 5 números e informe o maior número.

# numero = [1, 2, 3, 5, 8]
# maior = numero[0]
#
# for i in numero:
#     if i > maior:
#         maior = i
#
# print("o maior é :", maior)

#Faça um programa que leia 5 números e informe a soma e a média dos números.

# maior = 0
# soma = 0
# media = 0
#
# for x in range (1,5):
#     n1 = int(input("Digite um número: "))
#     soma = soma + n1
#     media = soma / n1
#     if n1> maior:
#         maior = n1
# print("O maior é:", str(maior))
# print("a soma é : " ,str(soma))
# print ("a media é :" ,str(media))


# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

# impar = 0
# numero = 0
# for i in range (1,51):
#     numero = i%2
#     if numero == 1:
#         impar = i
#         print(impar)

# Faça um programa que receba dois números inteiros e gere os números inteiros que estão
# no intervalo compreendido por eles.
#Altere o programa anterior para mostrar no final a soma dos números.

# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite um número: "))
# soma = 0
#
# for x in range((num1+1),num2):
#     if num1 < num2:
#         print(x)
#         soma = soma + x
# else:
#     for x in range((num2+1),num1):
#         print(x)
#         soma = soma + x
#
# print("A somatória é:",soma)

# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro
# entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.
# A saída deve ser conforme o exemplo abaixo:

# numero = int(input("Digite o número desejado para tabuada: "))
# for x in range (1,11):
#     tabuada = (x * numero)
#     print((str(numero) + " " + "X" + " " + str(x) + " " + "=" + " " + str(tabuada)))

#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número
# elevado ao segundo número. Não utilize a função de potência da linguagem.

# base = int(input("Digite o número base do cálculo:"))
# expoente = int(input("Digite o expoente do cálculo:"))
# resultado = 1
#
# for x in range(expoente+1):
#     resultado = resultado * base
# print(resultado)

# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares
# e a quantidade de números ímpares.

# impar = 0
# par = 0






































































