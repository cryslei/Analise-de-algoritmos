import time
import numpy as np
import matplotlib.pyplot as plt

def analise(entrada,saida):
    arquivo_entrada  = open(entrada,'r')
    arquivo_saida = open(saida,'w')
    arq = arquivo_entrada.read().split('\n')
    inicio = time.time()
    maior = max(arq)
    fim = time.time()
    arquivo_saida.write(str(maior)+'\n'+ str(round((fim-inicio)*1000, 10))+'\n')
    lista.append( str(maior) )
    listavalores.append(str(round((fim-inicio)*1000, 10)))
    arquivo_saida.close()
    arquivo_entrada.close()
lista = []
listavalores = []
entrada = ['a.csv','b.csv','c.csv','d.csv','e.csv']
saida = ['resposta-dataset-2-a.txt','resposta-dataset-2-b.txt','resposta-dataset-2-c.txt','resposta-dataset-2-d.txt','resposta-dataset-2-e.txt']
for x in range(len(entrada)):
    analise(entrada[x],saida[x])
    print('arquivo ', x ,' ok')
#Grafico
plt.plot(listavalores, lista, 'ko-')
palavra = ['A','B','C','D','E']
for item in range(len(listavalores)):
    plt.annotate(palavra[item], (listavalores[item], lista[item]))

plt.xlabel('Time (ms)')
plt.ylabel('Valores')
plt.title('Resultado')
plt.show()

