import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

n_simul = 1000000

sum_array = np.zeros(n_simul)

for t in range(1,n_simul - 1):

    x = []
    x.append('A')
    k = 1
    sum_ = 0
    
    #realiza diversas trajetorias ate que chegue no ponto 'C'
    while(x[k-1] != 'C'):
        
        #variavel aleatoria que decide qual caminho sera seguido
        rand = np.random.rand()

        #caso esteja no ponto 'A' define qual sera o proximo caminho
        if x[k-1] == 'A':
            if rand <= 0.05:

                x.append('A')
                sum_ = sum_ + 5
            elif rand > 0.05 and rand <= 0.10:

                x.append('C')
                sum_ = sum_ + 10
                
            else:

                x.append('B')
                sum_ = sum_ + 2
                
        #caso esteja no ponto 'B' define qual sera o proximo caminho
        else:

            if rand <= 0.5:

                x.append('B')
                sum_ = sum_ + 3
            else:

                x.append('A')
                sum_ = sum_ + 3
        
        k = k + 1
        
    #adiciona ao vetor de resultado da trajetoria
    sum_array[t] = sum_ 
    
#soma o resultado de todas as trajetorias e divide pela quantidade
sum_array.sum()/len(sum_array)
        
        
    
