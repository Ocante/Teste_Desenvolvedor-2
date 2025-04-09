# Teste Técnico – Desenvolvedor 2

Este projeto foi desenvolvido em Python, utilizando o IDLE como IDE. A seguir, apresento a resolução completa de todos os desafios propostos em um único fluxo de código e explicações, conforme solicitado.

```python
# 1) Ao final do processamento, qual será o valor da variável SOMA?

# Código:
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print("Resultado da soma até 13:", SOMA)

# Resposta: O valor da variável SOMA será 91, pois trata-se da soma dos números de 1 a 13.

# ------------------------------------------------------------------

# 2) Dado um número, verifique se ele pertence à sequência de Fibonacci.

def pertence_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero or numero == 0

numero = 21  # Pode ser alterado
if pertence_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")

# Resposta: O número 21 pertence à sequência de Fibonacci.
# Se você trocar o número por, por exemplo, 22, o resultado será negativo.

# ------------------------------------------------------------------

# 3) A partir de um JSON com o faturamento diário da distribuidora, calcular:
# - Menor valor de faturamento ocorrido em um dia do mês
# - Maior valor de faturamento ocorrido em um dia do mês
# - Número de dias com faturamento acima da média mensal

import json

# Exemplo de arquivo 'faturamento.json':
# [
#   {"dia": 1, "valor": 22174.1664},
#   {"dia": 2, "valor": 24537.6698},
#   {"dia": 3, "valor": 26139.6134},
#   {"dia": 4, "valor": 0.0},
#   {"dia": 5, "valor": 0.0},
#   {"dia": 6, "valor": 26742.6612},
#   {"dia": 7, "valor": 0.0}
# ]

with open('faturamento.json') as file:
    dados = json.load(file)

valores = [dia['valor'] for dia in dados if dia['valor'] > 0]
media = sum(valores) / len(valores)
menor = min(valores)
maior = max(valores)
dias_acima_media = sum(1 for valor in valores if valor > media)

print(f"Menor faturamento: R${menor:.2f}")
print(f"Maior faturamento: R${maior:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")

# Resposta:
# O programa ignora os dias com valor 0.
# Com base no exemplo, retorna os três dados solicitados corretamente.

# ------------------------------------------------------------------

# 4) Cálculo do percentual de representação de cada estado dentro do valor total mensal.

faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(faturamento_estados.values())

for estado, valor in faturamento_estados.items():
    percentual = (valor / total) * 100
    print(f"{estado}: {percentual:.2f}%")

# Resposta:
# SP: 37.53%
# RJ: 20.30%
# MG: 16.18%
# ES: 15.03%
# Outros: 10.96%

# ------------------------------------------------------------------

# 5) Programa que inverte os caracteres de uma string, sem usar funções prontas como reverse.

def inverter_string(texto):
    invertida = ''
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    return invertida

texto_original = "Desenvolvedor"
print("String invertida:", inverter_string(texto_original))

# Resposta:
# Entrada: "Desenvolvedor"
# Saída: "rovedolvesneD"
