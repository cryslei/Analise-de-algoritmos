import time

def analise(entrada,saida):
    arquivo_entrada  = open(entrada,'r')
    arquivo_saida = open(saida,'w')
    arq = arquivo_entrada.read().split('\n')
    n = arq[0]
    D = arq[2:]
    inicio = time.time()
    if n in D: 
        d_pos = D.index(n)
        fim = time.time()
        arquivo_saida.write('True'+'\n')
        arquivo_saida.write(str(d_pos+1)+'\n')
        arquivo_saida.write(str(round((fim-inicio)*1000, 10))+'\n')
    else:
        fim = time.time()
        arquivo_saida.write('False'+'\n')
        arquivo_saida.write(str(-1)+'\n')
        arquivo_saida.write(str(round((fim-inicio)*1000, 10))+'\n')
    arquivo_saida.close()
    arquivo_entrada.close()

entrada = ['a.csv','b.csv','c.csv']
saida = ['resposta-dataset-1-a.txt','resposta-dataset-1-b.txt','resposta-dataset-1-c.txt']


for x in range(len(entrada)):
    analise(entrada[x],saida[x])
    print('arquivo ', x ,' ok')


