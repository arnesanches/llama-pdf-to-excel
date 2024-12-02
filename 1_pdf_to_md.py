import os

# Define a chave da API necessária para o uso do LlamaParse
os.environ["LLAMA_CLOUD_API_KEY"] = "llx-LHEW7Nb8mUU69SHG8tndxYHVfcnueC4yLwjsR560vBBInBXi"

# Importa a biblioteca LlamaParse para análise de arquivos PDF
from llama_parse import LlamaParse

# Configura o analisador para retornar apenas tabelas em formato Markdown
documentos = LlamaParse(result_type="markdown", 
                        parsing_instruction="this file contains text and tables, I'd like to get only the tables from the text.").load_data("resultado.pdf")



