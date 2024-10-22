from random import randint

v_user = 0  # Contador de vitória do usuário
v_maq = 0   # Contador de vitória da máquina
rodada = 1  # Contador das rodadas
novamente = 's' # Jogar novamente ou não

# Possíveis resultados
lista = ['Pedra', 'Papel', 'Tesoura']
user_vitoria = [(0,2), (1,0), (2,1)]    # Baseados na lista
maq_vitoria = [(2,0), (0,1), (1,2)]

# Começo do jogo
while novamente == 's':
    print('\033[2mBEM VINDO AO JOGO PEDRA, PAPEL OU TESOURA!\033[0m\n')
    nome_user = input('Digite seu nome: ')

    while (v_user<3) and (v_maq<3):
        
        # Usuário faz sua escolha
        print(f'_________________\033[1mRODADA {rodada}\033[0m_________________')
        print(f'       {nome_user} ({v_user}) x ({v_maq}) Máquina\n')
        user_num = int(input('''Escolha uma das opções:\n1. Pedra\n2. Papel\n3. Tesoura\n\nEscolha: ''')) 
        
        user_num = user_num - 1
        user_escolha = lista[user_num]
        
        # Máquina faz sua escolha
        maq_num = randint(0,2)
        maq_escolha = lista[maq_num]

        # Combate
        print(f'\n\033[1m\033[0m {nome_user} ({user_escolha}) x ({maq_escolha}) Máquina')
        combate = (user_num, maq_num)

        # Conta a vitória
        if combate in user_vitoria:
            print('Parabéns! Você \033[1mganhou\033[0m a rodada!\n')
            v_user = v_user + 1

        elif combate in maq_vitoria:
            print('Que pena, você \033[1mperdeu\033[0m esta rodada!\n')
            v_maq = v_maq + 1
        
        else:
            print('Eita! Essa rodada deu \033[1mempate\033[0m!\n')
        
        
        rodada = rodada + 1

    print('______________________________\n')
    print('\033[1mRESULTADO FINAL\033[0m')
    if v_maq > v_user:
        print('Não foi dessa vez. A máquina ganhou. Mas não desista, tente novamente.\n')

    else:
        print('Você é incrível! Você ganhou!')

    
    print('______________________________')

    novamente = input('Deseja jogar novamente? [s/n]')

    if novamente == 's':
        v_user = 0
        v_maq = 0
        rodada = 0
        continue

    else:
        break