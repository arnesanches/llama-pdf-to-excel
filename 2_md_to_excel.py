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
