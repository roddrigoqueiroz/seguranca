import matplotlib.pyplot as plt

# Dados do gráfico
x = [16, 64, 256, 1024, 8192, 16384]  # Tamanhos dos blocos
y_aes128 = [10735214.0468, 1639683.1081, 399447.6510, 102226.3334, 19818, 14203.6667]  # AES-128 (blocos/segundo)
y_aes192 = [5140343.3334, 1395735.7860, 347007.6923, 88224.6667, 10859.1973, 5266.6667]  # AES-192 (blocos/segundo)
y_aes256 = [4586874.6667, 1183958.6667, 290016.3334, 168719, 13388.3334, 4687.3334]  # AES-256 (blocos/segundo)

# Criação do gráfico
plt.figure(figsize=(10, 6))

# Linhas para cada tipo de AES
plt.plot(x, y_aes128, marker='o', linestyle='-', color='blue', label='AES-128')
plt.plot(x, y_aes192, marker='o', linestyle='-', color='green', label='AES-192')
plt.plot(x, y_aes256, marker='o', linestyle='-', color='red', label='AES-256')

# Personalizações
plt.xscale('log')  # Define o eixo X como logarítmico
plt.title('Desempenho de AES por Tamanho de Bloco (Escala Logarítmica)', fontsize=14)
plt.xlabel('Tamanho do Bloco (bits)', fontsize=12)
plt.ylabel('Blocos Cifrados por Segundo 10^3', fontsize=12)
plt.xticks(x, labels=x)  # Mostra os valores destacados no eixo X
plt.grid(True, which="both", linestyle='--', alpha=0.7)  # Grade para ambas as escalas (major e minor)
plt.legend(fontsize=10)
plt.tight_layout()

# Exibição
plt.show()
