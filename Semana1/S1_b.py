from math import log, pow
import numpy as np

soma = 0
lista = []
n = 2
soma_parcelas = 100000  # Quantas parcelas vou somar
pulos_somas = 10000     # Intervalos entre os valores a serem considerados para análise

# Somas
print('\033[1mVamos verificar se a série \033[92m1/n(ln n)²\033[0m\033[1m converge, com n inteiro de 2 à 100000.\033[0m\n\nSuas \033[1msomas\033[0m: \n')
while n < soma_parcelas: 
    soma = soma + (1 / (n * pow(log(n), 2)))
    n = n + 1
    
    if (n % pulos_somas) == 0:
        lista.append(soma)
        print(f'Valor {n}: {soma:.10f}')


# Variação
print('\n\033[1mVariação\033[0m entre cada valor apresentado: \n')

for i in range(0, len(lista)-1):
    print(f'{(i+1)*pulos_somas} ~ {(i+2)*pulos_somas}: {lista[i+1]-lista[i]:.10f}')

# Conclusão
print('''\n\033[1mConclusão\033[0m: avaliando os valores, vemos que a diferença entre valores equidistante fica cada vez menor. Podemos inferir que essa diferença tende a zero, concluindo que a série em questão \033[1mconverge\033[0m.
Entretando, vale a observação que esse não é o melhor método para avaliar a convergência de uma série. Por exemplo, a série 1/n, com n>0, chamada de série harmônica, age de forma parecida com a 1/n(ln n)² mas diverge). Há métodos teóricos melhores como o teste da razão, da raiz ou da integral.\n''')