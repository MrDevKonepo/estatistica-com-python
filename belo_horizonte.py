import numpy as np
from statistics import median
from collections import Counter
from scipy.stats import skew, kurtosis

qtd_vendida = [2, 1, 5, 5]
qtd_vendida_ordenada = sorted(qtd_vendida)

preco_unitario_ordenado = [2500.00, 2500.00, 5300.00, 5300.00]

### Medidas por Quantidade Vendida ###
contador      = Counter(qtd_vendida_ordenada)
moda          = contador.most_common(1)[0][0]
media         = np.mean(qtd_vendida_ordenada)
mediana       = median(qtd_vendida_ordenada)
percentil_94  = np.percentile(qtd_vendida_ordenada, 94)
desvio_padrao = np.std(qtd_vendida_ordenada)
assimetria    = skew(qtd_vendida_ordenada)
curtose       = kurtosis(qtd_vendida_ordenada)

print("\n ### Quantidade Vendida Belo Horizonte ### ")
print(f"Moda: {moda}")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Percentil 94: {percentil_94}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print(f"Assimetria: {assimetria:.2f}")
print(f"Curtose: {curtose:.2f}")

### Medidas por Preço Unitário ###
contador      = Counter(preco_unitario_ordenado)
moda          = contador.most_common(1)[0][0]
media         = np.mean(preco_unitario_ordenado)
mediana       = median(preco_unitario_ordenado)
percentil_94  = np.percentile(preco_unitario_ordenado, 94)
desvio_padrao = np.std(preco_unitario_ordenado)
assimetria    = skew(preco_unitario_ordenado)
curtose       = kurtosis(preco_unitario_ordenado)

print("\n ### Preço Unitário Belo Horizonte ### ")
print(f"Moda: {moda}")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Percentil 94: {percentil_94}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print(f"Assimetria: {assimetria:.2f}")
print(f"Curtose: {curtose:.2f}")
