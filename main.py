import json

# Arquivo onde os dados serão salvos
ARQUIVO_DADOS = "dados_colheita.json"

# Função para calcular perdas e prejuízo
def calcular_perda(tipo_colheita, area_ha, preco_por_ton):
    produtividade_media = 100  # t/ha
    if tipo_colheita == 'manual':
        perda_percentual = 0.05
    else:
        perda_percentual = 0.15

    perda_total_ton = area_ha * produtividade_media * perda_percentual
    prejuizo = perda_total_ton * preco_por_ton
    return round(perda_total_ton, 2), round(prejuizo, 2)

# Função para salvar dados em JSON
def salvar_dados(dados):
    try:
        with open(ARQUIVO_DADOS, 'r') as f:
            registros = json.load(f)
    except FileNotFoundError:
        registros = []

    registros.append(dados)

    with open(ARQUIVO_DADOS, 'w') as f:
        json.dump(registros, f, indent=4)

# Função para visualizar registros salvos
def mostrar_registros():
    try:
        with open(ARQUIVO_DADOS, 'r') as f:
            registros = json.load(f)
            for i, reg in enumerate(registros, 1):
                print(f"\nRegistro {i}:")
                for k, v in reg.items():
                    print(f"  {k}: {v}")
    except FileNotFoundError:
        print("Nenhum registro encontrado.")

# Função principal
def menu():
    while True:
        print("\n=== SISTEMA DE SIMULAÇÃO DE PERDAS NA COLHEITA DE CANA ===")
        print("1. Registrar nova simulação")
        print("2. Ver registros salvos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do produtor: ")
            area = float(input("Área colhida (em hectares): "))
            preco = float(input("Preço por tonelada (R$): "))
            tipo = input("Tipo de colheita (manual/mecanica): ").lower()

            if tipo not in ['manual', 'mecanica']:
                print("Tipo inválido. Digite manual ou mecanica.")
                continue

            perda, prejuizo = calcular_perda(tipo, area, preco)

            dados = {
                "produtor": nome,
                "area_colhida_ha": area,
                "preco_ton": preco,
                "tipo_colheita": tipo,
                "perda_total_t": perda,
                "prejuizo_R$": prejuizo
            }

            salvar_dados(dados)
            print(f"\nPerda estimada: {perda} toneladas")
            print(f"Prejuízo estimado: R$ {prejuizo}")

        elif opcao == '2':
            mostrar_registros()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == '__main__':
    menu()
