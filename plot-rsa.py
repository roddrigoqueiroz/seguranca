import matplotlib.pyplot as plt
import numpy as np

# Dados fornecidos
data = [
    (162150, 512, 9.99),
    (72256, 1024, 9.99),
    (11326, 2048, 9.99),
    (1109, 4096, 9.95)
]

# Processamento dos dados
rsa_labels = ['512', '1024', '2048', '4096']  # Rótulos no eixo X
blocks_per_second = [round(row[0] / row[2], 4) for row in data]  # Blocos cifrados por segundo

# Configurações do gráfico
colors = ['blue', 'green', 'red', 'orange']  # Cores diferentes para cada barra
x_positions = np.arange(len(rsa_labels))  # Posições aproximadas das barras

plt.figure(figsize=(10, 6))
bars = plt.bar(x_positions, blocks_per_second, color=colors, width=0.6, edgecolor='black')

# Adiciona os valores no topo das barras
for bar, value in zip(bars, blocks_per_second):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
             f'{value}', ha='center', va='bottom', fontsize=10)

# Personalizações
plt.title('Desempenho do RSA por Tamanho de Bloco (Chave Privada)', fontsize=14)
plt.xlabel('Tamanho do Bloco do RSA (bits)', fontsize=12)
plt.ylabel('Blocos Cifrados por Segundo', fontsize=12)
plt.xticks(x_positions, labels=rsa_labels)  # Define os rótulos para o eixo X
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exibe o gráfico
plt.tight_layout()
plt.show()
