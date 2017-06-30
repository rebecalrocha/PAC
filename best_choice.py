import pandas as pd
import numpy as np

df_read = pd.read_csv('cromoRice.csv')

choices = ["A","T","C","G"]
quantidades = [0,0,0,0]
bn = np.zeros(286)
bn = bn.tolist()

for j in range(5, 286):  # colunas selecionadas | (5,286)
    index = pd.read_csv('cromoRice.csv', usecols=[j])
    chave = int(index.keys()[0])

    for i in range(3935):  # linhas selecionadas | (0,3935)
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

    bn[j] = choices[pos]

    quantidades = [0, 0, 0, 0]

df_write = pd.DataFrame(bn)
filename = 'best_choice.csv'
df_write.to_csv(filename, index=False, header=False, encoding='utf-8')