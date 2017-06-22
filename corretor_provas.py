# -*- coding: utf-8 -*-
"""
Corretor de provas
@author: Neylson Crepalde
"""

import pandas as pd
import csv

print("Digite o nome do arquivo do banco de dados:")
#nome_do_arquivo = input()
nome_do_arquivo = "~/Documentos/Corretor testes/aval_int_20171_teste.csv"
dados = pd.read_csv(nome_do_arquivo, sep = ',')

saida = open('notas_'+str(nome_do_arquivo)[:-4]+'.csv', 'w')
export = csv.writer(saida, quoting = csv.QUOTE_NONNUMERIC)
export.writerow(['Nome', 'Nota Final'])

dados['Nota Final'] = 0

print("O banco de dados tem {} colunas".format(len(dados.columns)))

gabarito = ['E','C','E','C','B','B','A','A','C','E',
            'E','D','D','D','E','E','A','B','B','C',
            'B','E','E','C','D','C','D','B','B','B',
            'A','E','B','C','C']

total = 35
nota = 0
for row in dados.index:   #Alunos
    nota = 0
    print("Correção da prova de {}:".format(dados["NOME"][row]))
    
    for col in range(3, len(dados.columns)-1):    #Questões
        if dados.iloc[row, col] == gabarito[col-3]:
            print("{}: Correta".format(dados.columns[col]))
            nota += 1
        elif dados.iloc[row, col] != gabarito[col-3]:
            print("{}: Errada".format(dados.columns[col]))
            
    print("Nota final: {}\n".format(nota/total))
    dados.iloc[row, len(dados.columns)-1] = nota/total
    export.writerow([dados["NOME"][row], nota])

print(dados[['NOME','Nota Final']])

saida.close()
