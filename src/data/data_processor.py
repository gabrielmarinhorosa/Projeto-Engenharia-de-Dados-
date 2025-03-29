import pandas as pd
import matplotlib.pyplot as plt


class DataProcessor:
    def __init__(self):
        self.dados_imoveis = None

    def read_excel_file(self, file_path):
        """Read Excel file and process the data"""
        self.dados_imoveis = pd.read_excel(file_path, sheet_name="Imoveis")
        self.dados_imoveis["Data de Transação"] = pd.to_datetime(
            self.dados_imoveis["Data de Transação"])
        self.dados_imoveis = self.dados_imoveis.sort_values(
            by="Data de Transação")
        return self.dados_imoveis

    def create_price_evolution_plot(self):
        """Create a plot showing price evolution over time"""
        if self.dados_imoveis is None:
            raise ValueError(
                "No data loaded. Please read an Excel file first.")

        plt.figure(figsize=(10, 6))
        plt.plot(self.dados_imoveis["Data de Transação"],
                 self.dados_imoveis["Preço m²"],
                 marker='o',
                 linestyle="-",
                 color="orange",
                 label="Preço m²")

        plt.title("Evolução do Preço por Metro Quadrado - Imóveis", fontsize=14)
        plt.xlabel("Data de Transação", fontsize=12)
        plt.ylabel("Preço m² (R$)", fontsize=12)
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()

        return plt.gcf()
