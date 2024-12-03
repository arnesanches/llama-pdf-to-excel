# Importando as bibliotecas necessárias
import re  # Operações com expressões regulares
import pandas as pd  # Manipulação e análise de dados
from io import StringIO  # Tratamento de strings como arquivos para entrada/saída de dados
import os # Manipulação de diretórios e arquivos
from openpyxl import load_workbook  # Manipulação de arquivos Excel


# Função para identificar e extrair tabelas em formato Markdown do texto
def tratar_tabelas_texto(texto):
    # Regex para encontrar tabelas no formato Markdown
    regra_busca_regex = re.compile(r'((?:\|.+\|(?:\n|\r))+)', re.MULTILINE)
    tabelas = regra_busca_regex.findall(texto)  # Retorna todas as tabelas encontradas
    return tabelas


# Função para ajustar automaticamente a largura das colunas em um arquivo Excel
def ajustar_colunas_excel(caminho_arquivo):
    # Carrega o arquivo Excel
    wb = load_workbook(caminho_arquivo)
    ws = wb.active

    # Ajusta a largura de cada coluna com base no conteúdo
    for col in ws.columns:
        max_length = 0
        col_letter = col[0].column_letter  # Obtém a letra da coluna
        for cell in col:
            if cell.value:  # Calcula o comprimento do valor máximo na coluna
                max_length = max(max_length, len(str(cell.value)))
        ws.column_dimensions[col_letter].width = max_length + 2  # Define a largura

    # Salva as alterações no arquivo Excel
    wb.save(caminho_arquivo)


# Função para transformar tabelas em Markdown em arquivos Excel
def transformar_markdown_excel(texto, num_pagina):
    # Extrai as tabelas em formato Markdown do texto
    lista_texto_tabelas = tratar_tabelas_texto(texto)

    if len(lista_texto_tabelas) > 0:  # Verifica se há tabelas para processar
        for i, texto_tabela in enumerate(lista_texto_tabelas):
            # Lê a tabela em Markdown como DataFrame do Pandas
            tabela = pd.read_csv(StringIO(texto_tabela), sep="|", encoding="utf-8", engine="python")
            tabela = tabela.dropna(how="all", axis=1)  # Remove colunas vazias
            tabela = tabela.dropna(how="all", axis=0)  # Remove linhas vazias
            
            # Define o caminho para salvar o arquivo Excel
            caminho_arquivo = f"tabelas/Pagina{num_pagina}Tabela{i+1}.xlsx"
            tabela.to_excel(caminho_arquivo, index=False)  # Salva o DataFrame como Excel

            # Ajusta as colunas do arquivo Excel gerado
            ajustar_colunas_excel(caminho_arquivo)


# Diretório onde estão as páginas no formato Markdown
pasta_paginas = "my_pdf"
# Lista de arquivos ordenada pelo tamanho do nome
lista_paginas = sorted(os.listdir(pasta_paginas), key=len)

# Itera pelas páginas para processar os arquivos Markdown e converter tabelas para Excel
for i, pagina in enumerate(lista_paginas):
    with open(f"my_pdf/{pagina}", "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()  # Lê o conteúdo da página

    num_pagina = i + 1  # Número da página atual
    transformar_markdown_excel(texto, num_pagina)  # Processa as tabelas da página

