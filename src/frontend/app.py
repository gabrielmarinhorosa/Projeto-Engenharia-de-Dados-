import streamlit as st
import os
from src.data.data_processor import DataProcessor
from src.utils.file_handler import FileHandler


def main():
    st.title("Análise de Dados de Imóveis")

    # Initialize components
    file_handler = FileHandler()
    data_processor = DataProcessor()

    # File upload section
    st.header("Upload de Arquivo")
    uploaded_file = file_handler.handle_file_upload()

    # Data analysis section
    if uploaded_file is not None and uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        st.header("Análise de Dados")

        try:
            # Process the Excel file
            dados_imoveis = data_processor.read_excel_file(uploaded_file)

            # Display the plot
            st.write("### Gráfico da Variação de Imóveis")
            fig = data_processor.create_price_evolution_plot()
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {str(e)}")


if __name__ == "__main__":
    main()
