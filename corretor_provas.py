# -*- coding: utf-8 -*-
"""
Corretor de provas
@author: Neylson Crepalde
"""

import pandas as pd
import csv

print("Digite o nome do arquivo do banco de dados:")
nome_do_arquivo = input()
dados = pd.read_csv(nome_do_arquivo, sep = ',')

saida = open('notas_'+str(nome_do_arquivo)[:-4]+'.csv', 'w')
export = csv.writer(saida, quoting = csv.QUOTE_NONNUMERIC)
export.writerow(['Aluno', 'Nota Final'])

dados['Nota Final'] = 0

print("O banco de dados tem {} colunas".format(len(dados.columns)))

gabarito = ['B','D','D','C','C','B','A','D','C','D','A','C','B','B','D']



nota = 0
for row in dados.index:
    nota = 0
    print("Correção da prova de {}:".format(dados["Quem é você?"][row]))
    
    for col in range(2, len(dados.columns)-1):
        if dados.iloc[row, col] == gabarito[col-2]:
            print("{}: Correta".format(dados.columns[col]))
            nota += 0.1
        elif dados.iloc[row, col] != gabarito[col-2]:
            print("{}: Errada".format(dados.columns[col]))
            
    print("Nota final: {}\n".format(nota))
    dados.iloc[row, len(dados.columns)-1] = nota
    export.writerow([dados["Quem é você?"][row], nota])

print(dados[['Quem é você?','Nota Final']])

saida.close()
