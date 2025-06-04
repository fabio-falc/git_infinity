# Cadastro de informações de contato

# Cria um dicionário vazio para armazenar os dados
informacoes = {}

# Título do formulário

print("=" * 60)
print(" " * 15 + "Cadastro de Contato")
print("=" * 60)

# Coleta de dados do usuário

informacoes["nome"] = input("Digite o seu nome: ").strip().title()
informacoes["telefone"] = input("Digite o número de telefone: ").strip()
informacoes["email"] = input("Digite o email: ").strip().lower()

# Exibição dos dados inseridos

print("\n" + "=" * 60)
print(" " * 15 + "Informações do Contato")
print("=" * 60)
print(f"Nome:      {informacoes['nome']}")
print(f"Telefone:  {informacoes['telefone']}")
print(f"E-mail:    {informacoes['email']}")
print("\n" + "=" * 60)
