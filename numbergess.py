# o algoritmo vai gerar um número e devemos adivinhar
# contar tentativas
# 0 a 10

import random

num = random.randint(0, 10)
tentativa = 0
tentativas_max = 3

while tentativa < tentativas_max:
    tentativa += 1
    guess = int(input("Tente adivinhar o número: "))
    if guess == num:
        print(f"Você acertou o número! Parabéns :D")
        break
    if tentativa == tentativas_max:
        print(f"Você perdeu, tente novamente! O número sorteado era {num}")
    else:
        if guess < num:
            print(f'Sua tentativa falhou, tente novamente ainda lhe restam {tentativas_max - tentativa} para acertar! \nDica: O número é maior do que o qual você escolheu')
        else:
            print(f'Sua tentativa falhou, tente novamente ainda lhe restam {tentativas_max - tentativa} para acertar! \nDica: O número é menor do que o qual você escolheu')


