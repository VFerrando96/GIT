import Functions as f
import datetime
import requests

data_destino = datetime.date(2004, 1, 1)
data_atual = datetime.date(2023,10,10)
while data_atual >= data_destino:
    ddd=str(data_atual).replace('-','')
    f.Baixar_arquivo(f.D_3(f.Dia_de_hoje()))
    url_do_pdf = rf"https://www.bcb.gov.br/content/focus/focus/R{ddd}.pdf"

    # Envie uma solicitação HTTP para a URL do PDF
    response = requests.get(url_do_pdf)

    # Verifique se a solicitação foi bem-sucedida (código de resposta 200)
    if response.status_code == 200:
    # Abra um arquivo local em modo de gravação binária (modo 'wb') para salvar o PDF
        with open(rf'Boletim_focus\Download\{data_atual}.pdf', 'wb') as file:
            file.write(response.content)
        print('PDF baixado com sucesso.')
    else:
        print('Falha ao baixar o PDF. Código de resposta:', response.status_code)
    from datetime import datetime, timedelta
    data_atual -= timedelta(days=1)
