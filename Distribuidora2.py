data = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento = sum(data.values())

percentual = {estado: (valor / faturamento) * 100 for estado, valor in data.items()}

for estado, perc in percentual.items():
    print(f'{estado}: {perc:.2f}% do faturamento total')