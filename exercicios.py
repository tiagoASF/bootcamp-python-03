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
temperatura_atual = float(input("Temperatura: "))
if temperatura_atual < 18:
    print(f"{temperatura_atual}o é BAIXA")
elif temperatura_atual >= 18 and temperatura_atual <= 26:
    print(f"{temperatura_atual} é NORMAL")
else:
    print(f"{temperatura_atual} é ALTA")