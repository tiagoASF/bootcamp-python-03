# Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas

import sys

# controle de fluxo
nome_valido = False
salario_valido = False
bonus_valido = False

while not nome_valido:
    try:
        nome_usuario = input("Informe o seu nome: ").strip().lower()
        #Verifica se nomoe está vazio
        if (len(nome_usuario) == 0):
            raise ValueError("É necessário digitar um nome")
        #Verifica se há números no nome
        elif any(char.isdigit() for char in nome_usuario):
            raise ValueError("O nome não deve conter números")
        else:
            print(f"VALIDAÇÃO OK! {nome_usuario} é um nome válido")
            nome_valido = True
    except ValueError as e:
        print(e)
    
while not salario_valido:
    try:        
        salario = float(input("Agora informe o seu salário mensal: "))
        if (salario <= 0):
            print("O salário informado deve ser maior que ou igual a zero.")
        else:
            salario_valido = True
    except ValueError:
        print("O salário deve ter valor numérico válido. Digite apenas números.")

while not bonus_valido:
    try:
        percentual_bonus = float(input("Qual o percentual do seu bônus anual: "))
        if (percentual_bonus < 0):
            print("O bônus deve ser maior ou igual a zero.")
        else: 
            bonus_valido = True
    except ValueError:
        print("O bônus deve ter valor numérico válido. Digite apenas números.")


kpi = 1000 + (salario * percentual_bonus) / 100
print(f"Olá {nome_usuario.capitalize()}! O valor total do seu bônus foi R$ {kpi:.2f}")