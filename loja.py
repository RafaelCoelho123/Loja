# Criar um dicionário de produtos
produtos = {
    "canetas": 1.50,
    "cadernos": 3.00,
    "lápis": 0.80
}

# Função para remover um item
def remover_item(produtos, item):
    produtos.pop(item, None)

# Função para calcular o número de itens
def calcular_numero_itens(produtos):
    return len(produtos)

# Função para adicionar um item com listas dentro de dicionários
def adicionar_item_com_lista(produtos, item, precos):
    produtos[item] = precos

# Função para calcular o valor total dos produtos na loja
def calcular_valor_total(produtos):
    return sum(produtos.values())

# Exemplo de uso das funções
# Remover um item
remover_item(produtos, "lápis")

# Calcular o número de itens
num_itens = calcular_numero_itens(produtos)
print(f"Número de itens: {num_itens}")

# Adicionar um item com lista de preços
adicionar_item_com_lista(produtos, "marcadores", [2.50, 3.00, 2.75])

# Calcular o valor total dos produtos
valor_total = calcular_valor_total({k: v if isinstance(v, (int, float)) else sum(v) for k, v in produtos.items()})
print(f"Valor total na loja: €{valor_total:.2f}")

# Exibir produtos atualizados
print("\nProdutos atualizados:")
for produto, preco in produtos.items():
    print(f"{produto}: {preco}")
