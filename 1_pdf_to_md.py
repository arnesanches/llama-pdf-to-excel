import os

# Define a chave da API necessária para o uso do LlamaParse
os.environ["LLAMA_CLOUD_API_KEY"] = "llx-LHEW7Nb8mUU69SHG8tndxYHVfcnueC4yLwjsR560vBBInBXi"

# Importa a biblioteca LlamaParse para análise de arquivos PDF
from llama_parse import LlamaParse

# Configura o analisador para retornar apenas tabelas em formato Markdown
documentos = LlamaParse(result_type="markdown", 
                        parsing_instruction="this file contains text and tables, I'd like to get only the tables from the text.").load_data("resultado.pdf")

# Exibe a quantidade de páginas processadas
print(len(documentos))

# Itera por todas as páginas processadas e salva o conteúdo de cada uma em arquivos individuais
for i, pagina in enumerate(documentos):
     # Cria e escreve o conteúdo da página no formato Markdown em arquivos separados
    with open(f"my_pdf/pagina{i+1}.md", "w", encoding="utf-8") as arquivo:
        arquivo.write(pagina.text)

