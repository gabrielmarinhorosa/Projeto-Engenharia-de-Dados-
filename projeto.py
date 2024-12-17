#maniuplação de dados com o pandas e matplotlib para criação de grafico

import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo Excel
caminho_arquivo = 'Rua Quata 391.xlsx'

# Carregar os dados da aba "2019"
dados_2019 = pd.read_excel(caminho_arquivo, sheet_name='2019')

# Converter a coluna "Data de Transação" para formato de data
dados_2019['Data de Transação'] = pd.to_datetime(dados_2019['Data de Transação'])

# Ordenar os dados pela data
dados_2019 = dados_2019.sort_values(by='Data de Transação')

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(dados_2019['Data de Transação'], dados_2019['Preço m²'], 
         marker='o', linestyle='-', color='orange', label='Preço m²')

# Configurar o gráfico
plt.title('Evolução da Base de Cálculo - 2019-2024', fontsize=14)
plt.xlabel('Data de Transação', fontsize=12)
plt.ylabel('Preço m² (R$)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.legend()

# Exibir o gráfico
plt.tight_layout()
plt.show()