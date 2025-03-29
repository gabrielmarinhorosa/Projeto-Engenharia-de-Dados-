import os
import streamlit as st


class FileHandler:
    def __init__(self, upload_dir="arquivos"):
        self.upload_dir = upload_dir
        self._ensure_upload_directory()

    def _ensure_upload_directory(self):
        """Ensure the upload directory exists"""
        if not os.path.exists(self.upload_dir):
            os.makedirs(self.upload_dir)

    def handle_file_upload(self):
        """Handle file upload and return the uploaded file"""
        uploaded_file = st.file_uploader(
            "Selecione um arquivo para arquivar",
            type=["txt", "csv", "pdf", "png", "jpg", "xlsx"]
        )

        if uploaded_file is not None:
            self._save_file(uploaded_file)
            self._display_file_info(uploaded_file)
            return uploaded_file
        else:
            st.warning("Nenhum arquivo selecionado.")
            return None

    def _save_file(self, uploaded_file):
        """Save the uploaded file to the upload directory"""
        file_path = os.path.join(self.upload_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("Arquivo arquivado com sucesso!")

    def _display_file_info(self, uploaded_file):
        """Display information about the uploaded file"""
        st.write("Nome do arquivo:", uploaded_file.name)
        st.write("Tipo do arquivo:", uploaded_file.type)
        st.write("Tamanho do arquivo:", uploaded_file.size, "bytes")
