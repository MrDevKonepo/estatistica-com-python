import numpy as np
from statistics import median
from collections import Counter
from scipy.stats import skew, kurtosis


### QUANTIDADE VENDIDA ###
# Lista das quantidades vendidas
qtd_vendida = [5, 3, 2, 3, 4, 4, 3, 2, 4, 3, 3, 2, 2, 1, 4, 2, 3, 2, 4, 4, 2, 5, 3, 5, 5, 1, 4, 5, 3, 1, 4, 5, 2, 1, 1, 3, 4, 1, 5, 1, 2, 3, 5, 5, 1, 5, 2, 2, 4, 5, 1, 4, 2, 3, 5, 4, 3, 5, 1]
qtd_vendida_ordenada = sorted(qtd_vendida)

# Moda
contador = Counter(qtd_vendida_ordenada)
moda = contador.most_common(1)[0][0]

# Média
media = np.mean(qtd_vendida_ordenada)

# Mediana
mediana = median(qtd_vendida_ordenada)

# Percentil 94
percentil_94 = np.percentile(qtd_vendida_ordenada, 94)

# Desvio Padrão
desvio_padrao = np.std(qtd_vendida_ordenada)

# Calcular a assimetria
assimetria = skew(qtd_vendida_ordenada)

# Calcular a curtose
curtose = kurtosis(qtd_vendida_ordenada)

print(" ### Quantidade Vendida ### ")
print(f"Moda: {moda}")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Percentil 94: {percentil_94}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print(f"Assimetria: {assimetria:.2f}")
print(f"Curtose: {curtose:.2f}")


### PREÇO UNITÁRIO ###
preco_unitario = [
    2500.00, 2500.00, 2100.00, 5300.00, 3400.00, 5300.00, 1400.00, 1600.00, 2500.00, 2100.00,
    5300.00, 5300.00, 5300.00, 2500.00, 2500.00, 1600.00, 3500.00, 2500.00, 3500.00, 3400.00,
    1400.00, 2500.00, 5300.00, 3500.00, 1600.00, 2500.00, 5300.00, 5300.00, 5300.00, 1600.00,
    2100.00, 5300.00, 5300.00, 1400.00, 2100.00, 5300.00, 1400.00, 1600.00, 3500.00, 3400.00,
    2100.00, 2500.00, 1600.00, 2100.00, 2500.00, 5300.00, 3500.00, 2500.00, 5300.00, 3500.00,
    1400.00, 5300.00, 2500.00, 5300.00, 5300.00, 5300.00, 2100.00, 5300.00, 3400.00
]

preco_unitario_ordenado = sorted(preco_unitario)

contador = Counter(preco_unitario_ordenado)
moda = contador.most_common(1)[0][0]

media = np.mean(preco_unitario_ordenado)

mediana = median(preco_unitario_ordenado)

percentil_94 = np.percentile(preco_unitario_ordenado, 94)

desvio_padrao = np.std(preco_unitario_ordenado)

assimetria = skew(preco_unitario_ordenado)

curtose = kurtosis(preco_unitario_ordenado)

print("\n ### Preço Unitário ### ")
print(f"Moda: {moda}")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Percentil 94: {percentil_94}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print(f"Assimetria: {assimetria:.2f}")
print(f"Curtose: {curtose:.2f}")
