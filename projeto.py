#maniuplação de dados com o pandas e matplotlib para criação de grafico
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st 


st.title("Upload de Arquivo")

# Caixa para o upload do arquivo
uploaded_file = st.file_uploader("Selecione um arquivo para arquivar", type=["txt", "csv", "pdf", "png", "jpg"])

# Verifica se o arquivo foi carregado
if uploaded_file is not None:
    # Mostra informações sobre o arquivo
    st.write("Nome do arquivo:", uploaded_file.name)
    st.write("Tipo do arquivo:", uploaded_file.type)
    st.write("Tamanho do arquivo:", uploaded_file.size, "bytes")

    # Salva o arquivo no servidor local
    with open(f"arquivos/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("Arquivo arquivado com sucesso!")
else:
    st.warning("Nenhum arquivo selecionado.")


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

st.write("# Grafico da variação de imoveis")
st.pyplot(plt)





