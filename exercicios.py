# EXERCICIO 01
# quantidade = int(input("Quantidade: "))
# preco = float(input("preco: "))

# if quantidade > 0 and preco >= 0:
#     print("Dados válidos!")
# else:
#     print("Dados inválidos")

# EXERCICIO 02
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'
# temperatura_atual = float(input("Temperatura: "))

# if temperatura_atual < 18:
#     print(f"{temperatura_atual}o é BAIXA")
# elif temperatura_atual >= 18 and temperatura_atual <= 26:
#     print(f"{temperatura_atual} é NORMAL")
# else:
#     print(f"{temperatura_atual} é ALTA")

# EXERCICIO 03
# Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. Dado um registro de log em formato de dicionário como log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log = {
#     'timestamp': '2021-06-23 10:00:00', 
#     'level': 'ERROR',
#     'message': 'Falha na conexão'
# }

# lista_logs = [
#     {
#         'timestamp': '2021-06-23 10:00:00', 
#         'level': 'ERROR',
#         'message': 'Falha na conexão'
#     },
#     {
#         'timestamp': '2021-06-23 10:00:00', 
#         'level': 'NORMAL',
#         'message': 'Conexão estabelecida'
#     },
#     {
#         'timestamp': '2021-06-23 11:00:00', 
#         'level': 'ERROR',
#         'message': 'Banco de dados inválido'
#     },
#     {
#         'timestamp': '2021-06-23 10:00:00', 
#         'level': 'ERROR',
#         'message': 'Falha na conexão'
#     }
# ]

# # if log['level'] == 'ERROR':
# #     print(log['message'])

# contador_erros = 0

# for log in lista_logs:
#     if log['level'] == 'ERROR':
#         contador_erros +=1
#         print(f"Em {log['timestamp']}: {log['message']}")

# print(f"O total de erros encontrados foi de {contador_erros}.")


# EXERCICIO 04
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# idade = int(input("Idade: "))
# email = input("E-mail: ").strip().lower()

# if idade < 18 or idade > 65:
#     print("Faixa etária não admitida")
# elif "@" not in email or "." not in email:
#     print("E-mail inválido")
# else:
#     print("Dados válidos!")

# EXERCICIO 05
# Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

# transacao = {'valor': 12000, 'hora': 20}
# transacao_suspeita = 0

# if transacao['valor'] > 10000:
#     print("Valor suspeito.")
#     transacao_suspeita = 1
# elif transacao['hora'] > 18 or transacao['hora'] < 9:
#     print("Horário suspeito.")
#     transacao_suspeita = 1

# if not transacao_suspeita:
#     print("Transação regular.")

# EXERCICIO 06
# Dado um texto, contar quantas vezes cada palavra única aparece nele.

import re

texto = "A raposa marrom, salta sobre o cachorro marrom preguiçoso. Mas o rato roeu a roupa do rei de Roma - exceto as meias."
palavras = texto.lower().split(" ")
palavras_selecionadas = []
palavras_unicas = {}

for palavra in palavras:
    palavra = re.sub(r'[.,!?-_]', "", palavra)
    if len(palavra) > 1:
        palavras_selecionadas.append(palavra)

for palavra in palavras_selecionadas:
    if palavra in palavras_unicas:
        palavras_unicas[palavra] += 1
    else:
        palavras_unicas[palavra] = 1

print(texto)
print(palavras_unicas)
