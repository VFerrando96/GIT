import Functions as f

url = r"https://www.bcb.gov.br/publicacoes/focus"

texto=f.abrir_site_e_buscar(url)
print(texto)