import matplotlib.pyplot as plt

# Dados do gráfico
x = [16, 64, 256, 1024, 8192, 16384]  # Tamanhos dos blocos
y_aes128 = [6127845.637583893, 1622250, 942828, 141585, 12187.583892617, 6374]  # AES-128 (blocos/segundo)
y_aes192 = [5091276.3334, 3199159, 506992, 88834.3334, 10902.6667, 5462.6667]  # AES-192 (blocos/segundo)
y_aes256 = [8773950.8361, 2364564.6667, 307326.3334, 77599, 9696.6555, 4738.255]  # AES-256 (blocos/segundo)

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
