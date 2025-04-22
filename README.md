 Simulador de Perdas na Colheita de Cana-de-Açúcar

Este projeto foi desenvolvido, propondo uma solução real e funcional voltada ao **setor de produção do agronegócio** — mais especificamente ao problema das perdas durante a colheita mecanizada de cana-de-açúcar.

## 🎯 Objetivo

Reduzir prejuízos na colheita da cana-de-açúcar começa com a **compreensão dos impactos econômicos** das perdas. Este simulador permite que o produtor:

- Registre simulações de colheita manual ou mecanizada
- Estime automaticamente a quantidade perdida e o prejuízo financeiro
- Armazene os registros em arquivos `.json`
- Acesse o histórico de simulações de forma prática

---

## 🧱 Conteúdo técnico aplicado

A proposta contempla os conceitos estudados nos capítulos 3 a 6:

### ✅ Subalgoritmos
- Funções com passagem de parâmetros: `calcular_perda()`, `salvar_dados()`, `mostrar_registros()`

### ✅ Estruturas de dados
- Uso de `listas`, `dicionários` e `tuplas` para organizar os dados do produtor

### ✅ Manipulação de arquivos
- Leitura e escrita de dados persistentes via arquivo `.json`

### ✅ Usabilidade
- Interface em menu de terminal com mensagens amigáveis e estrutura clara


## 📌 Como usar

### 1. Execute o script:
```bash
python main.py
olheita-cana
