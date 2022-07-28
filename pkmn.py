import os
from random import randint
from time import sleep
import pygame
pygame.mixer.init()
pygame.mixer.music.load('pokemon intro.mp3')
pygame.mixer.music.play()
print('\n----- POKÉMON BATTLE -----')
e = input('aperte Enter para começar')
os.system('cls')
pkl = ('CHARMANDER', 'BULBASSAURO', 'SQUIRTLE')
c = randint(1, 3)
pkc = pkl[c-1]
j = 4
while j > 3 or j < 1:
    j = int(input('Escolha o seu pokémon:\n[1] CHARMANDER\n[2] BULBASSAURO\n[3] SQUIRTLE\n>>> '))
    if j > 3 or j < 1:
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE\n')
        sleep(1)
        os.system('cls')
pkj = pkl[j-1]
print('\nVocê escolheu {}'.format(pkj))
sleep(1.5)
print('Um {} selvagem apareceu para batalhar contra você!\n'.format(pkc))
pygame.mixer.init()
pygame.mixer.music.load('pokemon battle.mp3')
pygame.mixer.music.play()
sleep(2)
os.system('cls')
atkc = ('scratch', 'ember', 'potion')
atkb = ('tackle', 'vine whip', 'potion')
atks = ('tackle', 'bubble', 'potion')
atk = randint(1, 2)
hpj = 100
hpc = 100
pj = 2
pc = 2
while hpj > 0 < hpc:
    print('-' * 30)
    print('    BARRA DE VIDA    ')
    print('-' * 30)
    print('{} (você): {}'.format(pkj, hpj))
    print('{} (inimigo): {}'.format(pkc, hpc))
    print('-' * 30)
    miss = randint(1, 10)
    miss2 = randint(1, 5)
    miss3 = randint(1, 3)
    #player charmander
    if j == 1:
        hc = int(input('Escolha uma habilidade:\n[1] scratch\n[2] ember\n[3] poção de vida (inventário: {})\n>>> '.format(pj)))
        atkj = atkc[hc-1]
        if hc == 3:
            if pj == 0:
                while hc == 3:
                    print('\nvocê não tem mais potion')
                    sleep(1)
                    hc = int(input('\nEscolha uma habilidade:\n[1] scratch\n[2] ember\n[3] poção de vida (inventário: {})\n>>> '.format(pj)))
                    atkj = atkc[hc - 1]
            else:
                pj -= 1
                hpj += 35
                print('\nvocê: {} usou {}'.format(pkj, atkj))
                sleep(1)
                print('\033[32m+35\033[m')
            sleep(1)
        if hc == 1:
            print('\nvocê: {} usou {}'.format(pkj, atkj))
            sleep(1)
            if c == 3:
                if miss2 == 1:
                    print('Errou!')
                else:
                    hpc -= 25
                    print('\033[31m-25\033[m')
            else:
                if miss == 1:
                    print('Errou!')
                else:
                    hpc -= 25
                    print('\033[31m-25\033[m')
            sleep(1)
        elif hc == 2:
            print('\nvocê: {} usou {}'.format(pkj, atkj))
            sleep(1)
            if c == 2:
                if miss3 == 1:
                    print('Errou!')
                else:
                    hpc -= 40
                    print('SUPER EFETIVO!')
                    sleep(0.5)
                    print('\033[31m-40\033[m')
            elif c == 3:
                if miss == 1:
                    print('Errou!')
                else:
                    hpc -= 20
                    print('não foi muito efetivo...')
                    sleep(0.5)
                    print('\033[31m-20\033[m')
            else:
                if miss3 == 1:
                    print('Errou!')
                else:
                    hpc -= 30
                    print('\033[31m-30\033[m')
            sleep(1)
    #player bulbassauro
    elif j == 2:
        hb = int(input('\nEscolha uma habilidade:\n[1] tackle\n[2] vine whip\n[3] poção de vida (inventário: {})\n>>> '.format(pj)))
        atkj = atkb[hb-1]
        if hb == 3:
            if pj < 1:
                while hb == 3:
                    print('\nvocê não tem mais potion')
                    sleep(1)
                    hb = int(input('\nEscolha uma habilidade:\n[1] tackle\n[2] vine whip\n[3] poção de vida (inventário: {})\n>>> '.format(pj)))
                    atkj = atkb[hb - 1]
            else:
                pj -= 1
                hpj += 35
                print('\nvocê: {} usou {}'.format(pkj, atkj))
                sleep(1)
        if hb == 1:
            print('\nvocê: {} usou {}'.format(pkj, atkj))
            sleep(1)
            if c == 1:
                if miss2 == 1:
                    print('Errou!')
                else:
                    hpc -= 25
            else:
                if miss == 1:
                    print('Errou!')
                else:
                    hpc -= 25
        elif hb == 2:
            print('\nvocê: {} usou {}'.format(pkj, atkj))
            sleep(1)
            if c == 3:
                if miss3 == 1:
                    print('Errou!')
                else:
                    hpc -= 40
                    print('SUPER EFETIVO!')
            elif c == 1:
                if miss == 1:
                    print('Errou!')
                else:
                    hpc -= 20
                    print('não foi muito efetivo...')
            else:
                if miss3 == 1:
                    print('Errou!')
                else:
                    hpc -= 30
        sleep(1)
    #player squirtle
    elif j == 3:
        hs = int(input('\nEscolha uma habilidade:\n[1] tackle\n[2] bubble\n[3] poção de vida (inventário: {})\n>>> '.format(pj)))
        atkj = atks[hs-1]
        if hs == 3:
            if pj < 1:
                while hs == 3:
                    print('\nvocê não tem mais potion')
                    sleep(1)
                    hs = int(input('\nEscolha uma habilidade:\n[1] tackle\n[2] bubble\n[3] poção de vida (inventário: {})\n>>> '.format(pj)))
                    atkj = atks[hs - 1]
            else:
                pj -= 1
                hpj += 35
                print('\nvocê: {} usou {}'.format(pkj, atkj))
                sleep(1)
        if hs == 1:
            print('\nvocê: {} usou {}'.format(pkj, atkj))
            sleep(1)
            if c == 2:
                if miss2 == 1:
                    print('Errou!')
                else:
                    hpc -= 25
            else:
                if miss == 1:
                    print('Errou!')
                else:
                    hpc -= 25
        elif hs == 2:
            print('\nvocê: {} usou {}'.format(pkj, atkj))
            sleep(1)
            if c == 1:
                if miss3 == 1:
                    print('Errou!')
                else:
                    hpc -= 40
                    print('SUPER EFETIVO!')
            elif c == 2:
                if miss == 1:
                    print('Errou!')
                else:
                    hpc -= 20
                    print('não foi muito efetivo...')
            else:
                if miss3 == 1:
                    print('Errou!')
                else:
                    hpc -= 30
        sleep(1)
    if hpj > 100:
        hpj = 100
    if hpc <= 0:
        hpc = 0
        os.system('cls')
        pygame.mixer.init()
        pygame.mixer.music.load('pokemon victory.mp3')
        pygame.mixer.music.play()
        print('-' * 30)
        print('    BARRA DE VIDA    ')
        print('-' * 30)
        print('{} (você): {}'.format(pkj, hpj))
        print('{} (inimigo): {}'.format(pkc, hpc))
        print('-' * 30)
        print('VOCÊ VENCEU')
        sleep(7)
    if hpc > 0:
        #pc charmander
        if c == 1:
            hc = randint(1, 2)
            if hc == 1:
                print('\ninimigo: {} usou {}'.format(pkc, atkc[hc - 1]))
                sleep(1)
                if miss == 1:
                    print('Errou!')
                else:
                    hpj -= 25
            elif hc == 2:
                print('\ninimigo: {} usou {}'.format(pkc, atkc[hc - 1]))
                sleep(1)
                if j == 2:
                    if miss3 == 1:
                        print('Errou!')
                    else:
                        hpj -= 40
                        print('SUPER EFETIVO!')
                elif j == 3:
                    if miss == 1:
                        print('Errou!')
                    else:
                        hpj -= 20
                        print('não foi muito efetivo...')
                else:
                    if miss3 == 1:
                        print('Errou!')
                    else:
                        hpj -= 30
            sleep(2)
        #pc bulbassauro
        elif c == 2:
            hb = randint(1, 2)
            if hb == 1:
                print('\ninimigo: {} usou {}'.format(pkc, atkb[hb - 1]))
                sleep(1)
                if miss == 1:
                    print('Errou!')
                else:
                    hpj -= 25
            elif hb == 2:
                print('\ninimigo: {} usou {}'.format(pkc, atkb[hb - 1]))
                sleep(1)
                if j == 3:
                    if miss3 == 1:
                        print('Errou!')
                    else:
                        hpj -= 40
                        print('SUPER EFETIVO!')
                elif j == 1:
                    if miss == 1:
                        print('Errou!')
                    else:
                        hpj -= 20
                        print('não foi muito efetivo...')
                else:
                    if miss3 == 1:
                        print('Errou!')
                    else:
                        hpj -= 30
            sleep(2)
         #pc squirtle
        elif c == 3:
            hs = randint(1, 2)
            if hs == 1:
                print('\ninimigo: {} usou {}'.format(pkc, atks[hs - 1]))
                sleep(1)
                if miss == 1:
                    print('Errou!')
                else:
                    hpj -= 25
            elif hs == 2:
                print('\ninimigo: {} usou {}'.format(pkc, atks[hs - 1]))
                sleep(1)
                if j == 1:
                    if miss3 == 1:
                        print('Errou!')
                    else:
                        hpj -= 40
                        print('SUPER EFETIVO!')
                elif j == 2:
                    if miss == 1:
                        print('Errou!')
                    else:
                        hpj -= 20
                        print('não foi muito efetivo...')
                else:
                    if miss3 == 1:
                        print('Errou!')
                    else:
                        hpj -= 30
            sleep(2)
        os.system('cls')
        if hpc > 100:
            hpc = 100
        if hpj <= 0:
            hpj = 0
            os.system('cls')
            pygame.mixer.init()
            pygame.mixer.music.load('pokemon lose.mp3')
            pygame.mixer.music.play()
            print('-' * 30)
            print('    BARRA DE VIDA    ')
            print('-' * 30)
            print('{} (você): {}'.format(pkj, hpj))
            print('{} (inimigo): {}'.format(pkc, hpc))
            print('-' * 30)
            print('VOCÊ PERDEU')
            sleep(6)
