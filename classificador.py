import pandas as pd
import numpy as np

### Create dataset

# j = coluna
# i = linha

conversao = list()  # conjunto de DNAs; é um vetor de strings
dados = list() #vetor de bases nitrogenadas
y = list()  # vetor de quantidade de amiloses

df = pd.read_csv('cromoRice.csv')
amilose = pd.read_csv('DADOS-CNAE-Qualidade.csv')

escolha = pd.read_csv('best_choice.csv')

for j in range(5, 286):  # colunas selecionadas | (5,286)
    index = pd.read_csv('cromoRice.csv', usecols=[j])
    chave = int(index.keys()[0])  # pegando o valor contido no index que é a chave da coluna

    '''
    Toda vez que entro em uma coluna j na tabela CromoRice, acho sua chave na tabela DADOS:
    '''

    for valor in range(283):  # (0,283) são todas os possíveis valores
        saved_value = amilose.iloc[valor, 0]  # valor da coluna 'Denominacao - GBS'
        if saved_value == chave:
            qnt_amilose = amilose.iloc[valor, 6]  # (linha que contém a chave, qntdade de amilose Goiania 2005)
            if qnt_amilose <= 24.0388693:
                y.append('B')
            else:
                y.append('A')

    for i in range(3935):  # linhas selecionadas | (0,3935)
        saved_cell = df.iloc[i, j]

        if pd.isnull(saved_cell) == True:  # não contém uma BN
            saved_cell = escolha.iloc[j,0]  # tratamento para valores vazios

        dados.append(saved_cell)

    dados.append(y[j-5])
    conversao.extend([dados])
    dados = list()

header=list()
pos = pd.read_csv('cromoRice.csv')
for x in range(3935):
    header.append(pos.iloc[x,1])
header.append('Amilose')

df_write = pd.DataFrame(conversao)
filename = 'cassificacao_media.csv'
df_write.to_csv(filename ,index=None,header=header, encoding='utf-8')

