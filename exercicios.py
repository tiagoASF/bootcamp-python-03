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

log = {
    'timestamp': '2021-06-23 10:00:00', 
    'level': 'ERROR',
    'message': 'Falha na conexão'
}

lista_logs = [
    {
        'timestamp': '2021-06-23 10:00:00', 
        'level': 'ERROR',
        'message': 'Falha na conexão'
    },
    {
        'timestamp': '2021-06-23 10:00:00', 
        'level': 'NORMAL',
        'message': 'Conexão estabelecida'
    },
    {
        'timestamp': '2021-06-23 11:00:00', 
        'level': 'ERROR',
        'message': 'Banco de dados inválido'
    },
    {
        'timestamp': '2021-06-23 10:00:00', 
        'level': 'ERROR',
        'message': 'Falha na conexão'
    }
]

# if log['level'] == 'ERROR':
#     print(log['message'])

contador_erros = 0

for log in lista_logs:
    if log['level'] == 'ERROR':
        contador_erros +=1
        print(f"Em {log['timestamp']}: {log['message']}")

print(f"O total de erros encontrados foi de {contador_erros}.")
