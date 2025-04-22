 🌾 Simulador de Perdas na Colheita de Cana-de-Açúcar

Este projeto foi desenvolvido, propondo uma solução real e funcional voltada ao setor de produção do agronegócio — mais especificamente ao problema das perdas durante a colheita mecanizada de cana-de-açúcar.
🎯 Objetivo

Reduzir prejuízos na colheita da cana-de-açúcar começa com a compreensão dos impactos econômicos das perdas. Este simulador permite que o produtor:

    Registre simulações de colheita manual ou mecanizada

    Estime automaticamente a quantidade perdida e o prejuízo financeiro

    Armazene os registros em arquivos .json

    Acesse o histórico de simulações de forma prática

🧱 Conteúdo técnico aplicado

A proposta contempla os conceitos estudados nos capítulos 3 a 6:
✅ Subalgoritmos

    Funções com passagem de parâmetros: calcular_perda(), salvar_dados(), mostrar_registros()

✅ Estruturas de dados

    Uso de listas, dicionários e tuplas para organizar os dados do produtor

✅ Manipulação de arquivos

    Leitura e escrita de dados persistentes via arquivo .json

✅ Usabilidade

    Interface em menu de terminal com mensagens amigáveis e estrutura clara

🔄 Conexão com banco Oracle

    Observação: Embora a proposta suporte integração futura com banco de dados Oracle, optamos por usar arquivos .json como base persistente, por atender plenamente os objetivos da simulação e garantir agilidade e simplicidade no processo.

📌 Como usar
1. Execute o script:

python main.py

2. Menu principal:

1. Registrar nova simulação
2. Ver registros salvos
3. Sair

3. Exemplo de entrada:

    Nome do produtor: João

    Área colhida: 100 hectares

    Preço por tonelada: R$ 90

    Tipo de colheita: mecanica

4. Saída esperada:

Perda estimada: 1500.0 toneladas
Prejuízo estimado: R$ 135000.0

🗂 Estrutura do projeto
Arquivo 	Descrição
main.py	Código-fonte do simulador
dados_colheita.json	Registros das simulações salvas (gerado automaticamente ao executar)
README.md	Documentação do projeto

    Observação: o arquivo dados_colheita.json será gerado automaticamente após a execução do programa, armazenando os registros inseridos pelo usuário.

🧠 Relevância do problema

O Brasil lidera a produção mundial de cana-de-açúcar, mas enfrenta perdas de até 15% na colheita mecanizada. Este simulador fornece um instrumento simples e eficiente de apoio à decisão do produtor rural, evidenciando os impactos e incentivando ações para otimizar sua colheita.
