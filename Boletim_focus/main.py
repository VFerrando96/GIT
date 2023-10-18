import Functions as f 
import requests
import datetime
url_do_pdf = rf"https://www.bcb.gov.br/content/focus/focus/R20231013.pdf"

# Envie uma solicitação HTTP para a URL do PDF
response = requests.get(url_do_pdf)

# Verifique se a solicitação foi bem-sucedida (código de resposta 200)
if response.status_code == 200:
# Abra um arquivo local em modo de gravação binária (modo 'wb') para salvar o PDF
    with open(f'Download\\{datetime.date.today()}.pdf', 'wb') as file:
        file.write(response.content)
    print('PDF baixado com sucesso.')
else:
    print('Falha ao baixar o PDF. Código de resposta:', response.status_code)