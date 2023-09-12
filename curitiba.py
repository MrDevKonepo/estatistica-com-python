import numpy as np
from statistics import median
from collections import Counter
from scipy.stats import skew, kurtosis

qtd_vendida = [2, 3, 3, 5]

preco_unitario = [1600.00, 2500.00, 5300.00, 5300.00]

### Medidas por Quantidade Vendida ###
contador      = Counter(qtd_vendida)
moda          = contador.most_common(1)[0][0]
media         = np.mean(qtd_vendida)
mediana       = median(qtd_vendida)
percentil_94  = np.percentile(qtd_vendida, 94)
desvio_padrao = np.std(qtd_vendida)
assimetria    = skew(qtd_vendida)
curtose       = kurtosis(qtd_vendida)

print("\n ### Quantidade Vendida em Curitiba ### ")
print(f"Moda: {moda}")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Percentil 94: {percentil_94}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print(f"Assimetria: {assimetria:.2f}")
print(f"Curtose: {curtose:.2f}")

### Medidas por Preço Unitário ###
contador      = Counter(preco_unitario)
moda          = contador.most_common(1)[0][0]
media         = np.mean(preco_unitario)
mediana       = median(preco_unitario)
percentil_94  = np.percentile(preco_unitario, 94)
desvio_padrao = np.std(preco_unitario)
assimetria    = skew(preco_unitario)
curtose       = kurtosis(preco_unitario)

print("\n ### Preço Unitário Curitiba ### ")
print(f"Moda: {moda}")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Percentil 94: {percentil_94}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print(f"Assimetria: {assimetria:.2f}")
print(f"Curtose: {curtose:.2f}")
