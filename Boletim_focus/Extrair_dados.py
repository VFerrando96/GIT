from PyPDF2 import PdfReader
import pandas as pd
import re
reader = PdfReader(r"D:\GIT\Boletim_focus\Download\2023-10-18.pdf")
page = reader.pages[1]
dados=page.extract_text()



# Use expressões regulares para extrair os valores
valores = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d)?', dados)

# Divida os valores em segmentos de tamanho igual ao número de colunas
num_colunas = 20
segmentos = [valores[i:i + num_colunas] for i in range(0, len(valores), num_colunas)]

# Crie um DataFrame com os valores extraídos
df = pd.DataFrame(segmentos)

# Exiba o DataFrame
print(df)