import pandas as pd
import numpy as np
import random
import faker
# Dados=pd.read_csv('Seuarquivo.csv')
data = []
fake = faker.Faker()
for i in range(20):
    data.append({
        'id': i + 1,
        'codigo do cliente': random.randint(1000, 9999),
        'nome': fake.name(),
        'email': fake.email()
    })

# Criando o DataFrame
df = pd.DataFrame(data)

# Exibindo o DataFrame


df['email']=df['email'].replace(df['email'][0],'victor.ferrando@gmail.com')
df['email']=df['email'].replace(df['email'][1],'victor.ferrando@gmail.com')
df['email']=df['email'].drop_duplicates()
df = df.dropna(subset=['email'])
print(df)