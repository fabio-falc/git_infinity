"""
[PYIA-A03] Crie um dicionário para armazenar o nome e o preço de cinco produtos. Peça ao usuário para inserir o nome de cada produto e o respectivo preço. À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. Por fim, exiba o valor total da compra.
"""
# Criação di dicionário para armazenar produtos e preço.
produtos = {}


# Coleta de dados dos produtos
print("----- Cadastro de produtos -----")

qtd_produtos = int(input("Digite a quantidade de produtos para cadastrar: "))
for produto in range(qtd_produtos):
    nome = input(f"\nDigite o nome do produto {produto + 1}: ").strip().lower()
    preco = float(input(f"Digite o preço de {nome}: "))

    produtos[nome] = preco

# Cálculo  do valor de total da compra
total_compra = sum(produtos.values())

# Exibição de resultado
print("\nProdutos cadastrados: ")

for nome, preco in produtos.items():
    print(f"- {nome}: R$ {preco:.2f}")


print(f"\nValor total da compra: R${total_compra}")    
    