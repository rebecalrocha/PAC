import pandas as pd
import numpy as np

df_read = pd.read_csv('TA Goiania 2005.csv')

choices = ["A","T","C","G"]
quantidades = [0,0,0,0]
coluna = list()
bn = list()

header = list()
h=list()
pos = pd.read_csv('cromoRice.csv')
for x in range(3935):
    h.append(pos.iloc[x,1])

TA = list()
for valor in range(281):
    saved_value = df_read.iloc[valor, 3935]  #TA
    TA.append(saved_value)

for j in range(3935):
    index = pd.read_csv('TA Goiania 2005.csv', usecols=[j])
    chave = int(index.keys()[0])

    for i in range(281):
        saved_cell = df_read.iloc[i, j]

        if saved_cell == "A":
            quantidades[0] += 1
        elif saved_cell == "T":
            quantidades[1] += 1
        elif saved_cell == "C":
            quantidades[2] += 1
        elif saved_cell == "G":
            quantidades[3] += 1

        choice = quantidades[0]
        pos = 0

    for x in range(4):
        if quantidades[x] > choice:
            choice = quantidades[x]
            pos = x

    quantidades = [0,0,0,0]
    if ((choice/281) < 0.6):
        #print("posição %d entrou"%(j))
        for i in range(0, 281):  # linhas selecionadas | (0,3935)
            saved_cell = df_read.iloc[i, j]
            bn.append(saved_cell)

    if (bn != []):
        coluna.extend([bn])
        header.append(h[j])
        bn = list()

quant = len(coluna)
print(quant)

linhas = list()
conversao = list()

for i in range(281): #quantidade de elementos da lista
    for j in range(quant): #quantidade de listas geradas
        linhas.append(coluna[j][i:i+1][0])

    linhas.append(TA[i])
    conversao.extend([linhas])
    linhas = list()

header.append('Amilose')

df_write = pd.DataFrame(conversao)
filename = 'decrease_60.csv'
df_write.to_csv(filename, index=False, header=header, encoding='utf-8')