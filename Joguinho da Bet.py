from random import randint
pc = randint(1, 5)
print('Sou seu PC. Pensei em um número  entre 1 e 5 e quero que você adivinhe. E aí? Qual foi?  ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite?  '))
    palpite += 1
    if jogador == pc:
        acertou = True
print('Acertou! Deu green na sua BET depois de {} palpites!'.format(palpite))