# JOGO DA FORCA


# Escolha da palavra

carac_proib = ['á','à','â','ã','ä','é','è','ê','ë','í','ì','î','ï','ó','ò', '\\','ô','õ','ö','ú','ù','û','ü','!','@','#','$','%','¨','&','*','(',')','-','_','=','+','§','\´','\`','~','^','[',']','{','}','/','?','°',':',';','.','>',',','<','|','\'','\"','ª',' ']
val = 0

while val == 0:
    word = input("Escolha a palavra: ")
    word = word.lower()
    
    # Verificação dos caracteres proibidos
    for i in carac_proib:
        if (i in word) == True:
            print(f'O caracter {i} não é permitido. Escolha outra palavra, por favor.\n')
            break

        else:
            val = 1

word_list = list(word)            # Transforma a palavra numa lista

word_sec =  '_' * len(word)       # Cria uma string com a palavra escondida
word_sec_list = list(word_sec)

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
usadas = []                             # Lista de letras usadas nas tentativas


# Começa o jogo
erro = 0
while erro < 6:
    print(f'____________________________________\nPalavra: {word_sec}\nLetras usadas: {usadas}\nErros: {erro}\n')

    if word_list == word_sec_list:  # Para se a palavra estiver igual
        print(f"Parabéns!! Você acertou a palavra '{word}'.")
        break
    
    else:
        letra = input("Escolha uma letra: ")
        letra = letra.lower()
        
        if letra in alfabeto:       # Verifica se é um caracter válido
            
            if letra in usadas:     # Verifica se a letra já foi usada
                print('Essa letra já foi usada. Tente outra.')
            else:
                usadas.append(letra) # Adiciona a letra na lista de usadas
                
                if letra in word_list:    # Verifica se a letra está na palavra
                    
                    for i in range(0, len(word_list)):   # Substitui na palavra secreta
                        j = word_list[i]
                        
                        if j == letra:  # Revela a letra correta na palavra secreta
                            word_sec_list[i] = letra 
                            word_sec = ''.join(word_sec_list)
                            
                else:
                    erro += 1
                    if erro > 4:
                        print("Infelizmente você perdeu. Mas não desiste, tente novamente.")
        else:
            print('Esse caracter não é permitido.')


