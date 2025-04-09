import json

with open('faturamento.json') as file:
    dados = json.load(file)

valores = [dia['valor'] for dia in dados if dia['valor'] > 0]
media = sum(valores) / len(valores)

menor = min(valores)
maior = max(valores)
dias_acima_media = sum(1 for v in valores if v > media)

print(f"Menor faturamento: R${menor:.2f}")
print(f"Maior faturamento: R${maior:.2f}")
print(f"Dias acima da média: {dias_acima_media}")
