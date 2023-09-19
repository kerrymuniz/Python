import random #importando o random para conseguir usá-lo
# Primeiro Algoritmo

clientes = ['Kerry', 'Mariana Ramos', 'Guilherme', 'Pedro']

vencedor = random.choice(clientes) #método que irá retornar um valor aleatório aquela variável imposta nele

sabor = 'baunilha'

print('Parabéns ' + vencedor + ' você ganhou um sundae!') #primeira impressão que irá aparecer ao rodar o código

prompt = 'Você quer uma cereja em cima? '

quer_cereja = input(prompt) #pede para o usuário digitar algo e atribuí-la a variável quer_cereja

pedido = 'sundae de ' + sabor

if(quer_cereja == 'sim'):
    pedido = pedido + ' com uma cereja em cima '

print('Um ' + pedido + ' para ' + vencedor + ' saindo...')