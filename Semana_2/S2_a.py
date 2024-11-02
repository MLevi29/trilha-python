# jogo da forca
word = input("Escolha a palavra: ")  # Escolhe a palavra a ser descoberta
word_list = list(word)            # Transforma a palavra numa lista

word_sec =  '_' * len(word)       # Cria uma string com a palavra escondida
word_sec_list = list(word_sec)

usadas = []                             # Lista de letras usadas nas tentativas

# Jogo
erro = 0
while erro < 6:
    print(f'''
____________________________________
Palavra: {word_sec}

Letras usadas: {usadas}
Erros: {erro}
''')

    if word_list == word_sec_list:  # Para se a palavra estiver igual
        print(f"Parabéns!! Você acertou a palavra {word}.")
        break
    
    else:
        letra = input("Escolha uma letra: ")
        if letra in usadas:
            print('Essa letra já foi usada. Tente outra.')
        else:
            usadas.append(letra) # Adiciona a letra na lista de usadas
            
            if letra in word_list:    # Verifica se a letra está na palavra
                
                for i in range(0, len(word_list)):   # Substitui na palavra secreta
                    j = word_list[i]
                    
                    if j == letra:
                        word_sec_list[i] = letra 
                        word_sec = ''.join(word_sec_list)
                        
            else:
                erro += 1
                if erro > 4:
                    print("Infelizmente você perdeu. Mas não desiste, tente novamente.")


