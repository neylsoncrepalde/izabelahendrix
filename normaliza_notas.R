# Avaliação Integrada Izabela Hendrix
# Curso de Música
# Script: Neylson Crepalde
#####################################

setwd("~/Documentos/Neylson Crepalde/Izabela Hendrix/Códigos/izabelahendrix")
list.files()

library(readr)
aval = read_csv("notas_aval_int_20171.csv")
head(aval)

aval$`Nota em 1.5` = round(aval$`Nota Final`*1.5, digits = 2)
head(aval)

aval$`Nota Normalizada` = 0

# Corrigindo as notas de quem está antes da metade do curso
# Até o 3 período a nota é multiplicada por 2
for (i in 1:nrow(aval)){
  if (aval$Período[i] < 4){
    aval$`Nota Normalizada`[i] = round(aval$`Nota em 1.5`[i] * 2, digits=2)
  }
  else{
    aval$`Nota Normalizada`[i] = aval$`Nota em 1.5`[i]
  }
}

# Corrigindo os excessos para 1.5
for (i in 1:nrow(aval)){
  if (aval$`Nota Normalizada`[i] > 1.5){
    aval$`Nota Normalizada`[i] = 1.5
  }
}

# exporta os dados
#write_excel_csv(aval, "notas_aval_int_20171.xlsx")
