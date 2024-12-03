import re
import pandas as pd
from io import StringIO
import os
from openpyxl import load_workbook

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