import random
import time

# Cria uma lista com os nomes dos pratos e os preços correspondentes
menu = {
    "Arroz de frutos do mar": 40.00,
    "Batata recheada": 15.00,
    "Batatas fritas": 5.00,
    "Bobó de camarão": 30.00,
    "Bolo de cenoura": 12.00,
    "Burritos": 15.00,
    "Cachorro-quente": 8.00,
    "Camarão": 22.00,
    "Carne assada": 25.00,
    "Carne de sol com mandioca": 32.00,
    "Churrasco misto": 40.00,
    "Cupcake": 4.00,
    "Ensopado de carne": 28.00,
    "Espaguete à bolonhesa": 16.00,
    "Feijoada completa": 35.00,
    "Frango à parmegiana": 25.00,
    "Frango à passarinho": 15.00,
    "Frango grelhado": 18.00,
    "Hambúrguer": 10.00,
    "Hot dog": 8.50,
    "Lasanha de carne": 20.00,
    "Lasanha de frango": 18.00,
    "Linguiça acebolada": 18.00,
    "Moqueca de peixe": 30.00,
    "Mousse de chocolate": 8.00,
    "Nachos": 10.00,
    "Omelete": 11.00,
    "Panquecas": 14.00,
    "Peixe frito": 17.00,
    "Peixe grelhado": 25.00,
    "Pizza de calabresa": 22.00,
    "Pizza de frango": 25.00,
    "Pizza de mussarela": 20.00,
    "Refrigerante": 2.00,
    "Risoto de camarão": 35.00,
    "Risoto de cogumelos": 28.00,
    "Salmão grelhado": 30.00,
    "Sanduíche de carne": 9.00,
    "Sanduíche de frango": 8.00,
    "Sanduíche de peito de peru": 12.00,
    "Sanduíche de presunto e queijo": 7.00,
    "Sorvete": 8.00,
    "Strogonoff de carne": 24.00,
    "Strogonoff de frango": 22.00,
    "Tacos": 16.00,
    "Torta": 15.00,
}

gastos = {}

# Define o preço inicial do restaurante e o número de dias de negócio
while True:
    dinheiro_str = input("Digite o dinheiro atual do restaurante no padrão 0.00: ")
    try:
        dinheiro = float(dinheiro_str)
        break
    except ValueError:
        print("Valor inválido. Digite um número no formato 0.00.")

dias = int(input('Você vai deixar o restaurante aberto por quantos dias? '))

# Define a probabilidade de um cliente sair sem pagar
probabilidade_sem_pagar = 0.2

# Loop principal do jogo, que executa por um número definido de dias
for dia in range(1, dias + 1):
    print(f"\nDia {dia}:")

    # Gera um número aleatório de clientes para o dia
    clientes = random.randint(1, 10)
    print(f"{clientes} clientes entraram no restaurante hoje.")

    # Loop interno para atender aos pedidos de cada cliente
    for cliente in range(clientes):
        print(f"\nCliente {cliente+1}:")
        nome = input("Qual é o seu nome? ")
        while True:
          pedido = input("O que você gostaria de pedir? ")
          itens_invalidos = [item for item in pedido.split(",") if item.strip() not in menu]
          if len(itens_invalidos) == 0:
            break
          else:
            print(f"Desculpe, o(s) item(ns) {', '.join(itens_invalidos)} não está(ão) disponível(is) no menu. Por favor, escolha novamente.")
        

        # Verifica se o item do menu está disponível e atualiza o preço total do pedido
        preco_total = 0
        for item in pedido.split(","):
            item = item.strip()
            if item in menu:
                preco_total += menu[item]

        # Verifica se o preço total do pedido é maior do que zero
        if preco_total > 0:
            # Verifica se o restaurante tem dinheiro suficiente para cozinhar o pedido
            if preco_total > dinheiro:
                print("Desculpe, não temos dinheiro suficiente para fazer seu pedido.")
                continue
            else:
                # Espera um tempo aleatório entre 1 e 5 segundos antes de cozinhar o pedido
                tempo_espera = random.randint(1, 5)
                print(f"Seu pedido ficará pronto em {tempo_espera} segundos...")
                time.sleep(tempo_espera)

                # Verifica se o tempo de espera excede um limite máximo
                limite_espera = 3  # em segundos
                if tempo_espera > limite_espera:
                    print(
                        f"Desculpe {nome}, mas seu pedido demorou demais para ser entregue. Esperamos que você não fique chateado(a)."
                    )

                # Cozinha o pedido e atualiza o preço do restaurante e do cliente
                dinheiro -= preco_total
                print(
                    f"Seu pedido de {pedido} está pronto! O preço total é {preco_total:.2f}."
                )

                # Verifica se o cliente irá pagar
                if random.random() < probabilidade_sem_pagar:
                    print(f"{nome} decidiu sair sem pagar...")
                else:
                    print(f"{nome}, seu pedido custa {preco_total:.2f}.")
                    pagamento_str = input("Quanto você gostaria de pagar? ")
                try:
                    pagamento = float(pagamento_str)
                    if pagamento < preco_total:
                        print(
                            f"Desculpe {nome}, você não tem dinheiro suficiente para pagar seu pedido."
                        )
                    else:
                        troco = pagamento - preco_total
                        dinheiro += preco_total
                        print(f"Obrigado {nome}! Seu troco é {troco:.2f}.")
                        if nome in gastos:
                            gastos[nome] += preco_total
                        else:
                            gastos[nome] = preco_total
                except ValueError:
                    print(f"Desculpe {nome}, você inseriu um valor inválido.")

if dia == dias:
  # Exibe o dinheiro final do restaurante e quanto cada cliente gastou
  print(f"\nDinheiro final do restaurante após {dias} dias: {dinheiro:.2f}")
  for nome, gasto in gastos.items():
    print(f'{nome}: {gasto:.2f}')
