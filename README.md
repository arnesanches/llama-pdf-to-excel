Llama Extractor PDF Excel

Este projeto tem como objetivo extrair tabelas de arquivos PDF e convertê-las em arquivos Excel (.xlsx) com formatação adequada. O processo é dividido em duas etapas principais, cada uma executada por um script Python.

Antes de executar os scripts, certifique-se de criar manualmente as pastas my_pdf e tabelas no mesmo diretório onde os scripts estão localizados. Essas pastas são necessárias para armazenar os arquivos intermediários e os resultados finais. Verifique se as dependências necessárias estão instaladas no seu ambiente Python, como llama_parse, openpyxl e pandas. Você pode instalar essas dependências utilizando um gerenciador de pacotes como pip. Certifique-se de salvar o arquivo PDF com o nome resultado.pdf no mesmo diretório do script antes de executar o primeiro script.

Para usar o projeto, comece executando o arquivo 1_pdf_to_md.py, que é responsável por extrair tabelas de um arquivo PDF e salvá-las no formato Markdown (.md) dentro de uma pasta chamada my_pdf. Certifique-se de que o arquivo PDF a ser processado esteja no mesmo diretório do script e nomeado como resultado.pdf. Após a execução, serão gerados arquivos .md correspondentes às páginas do PDF, salvos na pasta my_pdf.

Depois disso, execute o arquivo 2_md_to_excel.py. Este script processará os arquivos .md da pasta my_pdf, extrairá as tabelas no formato Markdown e as converterá para arquivos Excel (.xlsx). Esses arquivos Excel serão organizados por página e tabela e salvos em uma pasta chamada tabelas. A execução do segundo script depende dos arquivos gerados pelo primeiro, por isso é fundamental seguir essa ordem.

A estrutura do projeto inclui os seguintes elementos: dois scripts Python, sendo um para a extração das tabelas do PDF e outro para a conversão dessas tabelas em Excel; o arquivo PDF de entrada nomeado como resultado.pdf; a pasta my_pdf, onde serão armazenados os arquivos Markdown gerados; e a pasta tabelas, onde ficarão os arquivos Excel resultantes.

Contribuições para o projeto são bem-vindas. Caso tenha sugestões ou encontre problemas, sinta-se à vontade para abrir um pull request ou relatar na seção de issues.