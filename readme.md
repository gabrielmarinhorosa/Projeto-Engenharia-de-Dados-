# Análise de Dados de Imóveis

Este projeto é uma aplicação web desenvolvida com Streamlit para análise e visualização de dados de imóveis. A aplicação permite o upload de arquivos Excel contendo informações sobre transações imobiliárias e gera visualizações interativas dos dados.

## Funcionalidades

- Upload de arquivos Excel
- Processamento automático de dados
- Visualização de gráficos de evolução de preços
- Interface intuitiva e responsiva
- Armazenamento seguro de arquivos

## Estrutura do Projeto

```
.
├── src/
│   ├── data/
│   │   ├── __init__.py
│   │   └── data_processor.py    # Processamento de dados e geração de gráficos
│   ├── frontend/
│   │   ├── __init__.py
│   │   └── app.py              # Interface principal da aplicação
│   └── utils/
│       ├── __init__.py
│       └── file_handler.py     # Gerenciamento de upload de arquivos
├── run.py                      # Script para executar a aplicação
└── requirements.txt            # Dependências do projeto
```

## Requisitos

- Python 3.8 ou superior
- Dependências listadas em `requirements.txt`

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_DIRETÓRIO]
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como Usar

1. Inicie a aplicação:
```bash
streamlit run run.py
```

2. Acesse a aplicação no navegador (geralmente em http://localhost:8501)

3. Faça upload de um arquivo Excel com os seguintes requisitos:
   - Planilha nomeada "Imoveis"
   - Colunas necessárias:
     - "Data de Transação"
     - "Preço m²"

4. A aplicação processará automaticamente os dados e exibirá o gráfico de evolução de preços

## Formato do Arquivo Excel

O arquivo Excel deve conter uma planilha chamada "Imoveis" com as seguintes colunas:

- Data de Transação (formato de data)
- Preço m² (valores numéricos)

## Contribuição

Contribuições são bem-vindas! Por favor, siga estas etapas:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Contato

[Seu Nome] - [seu.email@exemplo.com]

Link do Projeto: [https://github.com/seu-usuario/nome-do-projeto](https://github.com/seu-usuario/nome-do-projeto)