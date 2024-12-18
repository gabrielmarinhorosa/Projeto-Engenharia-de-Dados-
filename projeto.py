#maniuplação de dados com o pandas e matplotlib para criação de grafico
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

arquivo = "RuaQuata391.xlsx"

dados_imoveis = pd.read_excel(arquivo, sheet_name = "Imoveis")

dados_imoveis["Data de Transação"] = pd.to_datetime(dados_imoveis["Data de Transação"])

dados_imoveis = dados_imoveis.sort_values(by= "Data de Transação")

plt.figure(figsize=(10,6))
plt.plot(dados_imoveis["Data de Transação"], dados_imoveis["Preço m²"], marker = 'o', linestyle ="-", color="orange", label = "Preço m²")

plt.title("Evolução do Preço por Metro Quadrado - Imóveis", fontsize = 14)
plt.xlabel("Data de Transação", fontsize = 12)
plt.ylabel("Preço m² (R$)", fontsize = 12)
plt.grid(True, linestyle = "--", alpha = 0.7)
plt.xticks(rotation = 45)
plt.legend()

plt.tight_layout()
plt.show()