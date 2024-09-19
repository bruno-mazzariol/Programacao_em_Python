                              #TORRE DE HANOI
#-------------------------------------------------------------------#

''' muda as posições de cada disco com saida para mostrar
    torre na posicao correta '''

def torre_hanoi(num_discos,origem,destino, auxiliar,torres):
    # caso base
    if num_discos == 1:
        # mover o disco da origem para torre de destino
        disco = torres[origem].pop()
        torres[destino].append(disco)
        mostrar_torres(torres)
        # caso recursivo 
    else:
        # Mover n-1 discos da torre de origem para a torre auxiliar
        torre_hanoi(num_discos-1,origem,auxiliar,destino,torres)
        # Mover o disco restante da torre de origem para a torre de destino
        torre_hanoi(1,origem, destino, auxiliar, torres)
        # Mover os n-1 discos da torre auxiliar para a torre de destino
        torre_hanoi(num_discos-1,auxiliar,destino,origem,torres)

'''mostrar as torres formatadas'''

def mostrar_torres(torres):
    # Encontra a altura máxima das torres
    altura = max(len(disco) for disco in torres.values())
    # Mostra os discos de cima para baixo
    for i in range(altura-1,-1,-1):
        for discos in torres.values():
        # imprime os valores que sao menores do que o tamanho da lista 
            if i < len(discos):
                print("{:^10}".format(discos[i]), end=" ")
            else:
                print(" "*10, end=" ")
        # Para mover para a próxima linha após cada conjunto de torres         
        print()  
        
    # Mostra os nomes das torres abaixo dos discos
    print("  TORREA     TORREB     TORREC   ")
    print()
    
    
''' obtem o numero de disco corretamente com saida de erro caso houver '''

def obter_numero_discos():
    while True:
        try:
            # Solicitar o número de discos
            num_discos = int(input('Entre com o número de discos (maior que zero): '))

            # Verificar se o número é válido
            if num_discos > 0:
                return num_discos
        
            print("\nDigite novamente! O número deve ser maior que zero.\n")
        # casos para entradas que nao sejam numeros inteiros
        except ValueError:
            print("\nEntrada inválida. Por favor, insira um número inteiro.\n")



num_discos = obter_numero_discos()
# inicialização das torres

torres = {'origem':list(range(num_discos,0,-1)),'destino':[],'auxiliar':[]}

mostrar_torres(torres)

# Executar a função de Hanói 
torre_hanoi(num_discos,'origem','destino','auxiliar',torres)
