import random
import time
#set_caption
import os
import pygame.draw
from defs import *


ASSETSDI = "ast"
pygame.init()
pygame.mixer.init()
# Opengameart.org
#Brxf
#powerup
# pygame.init()
#pygame.set_caption

# ----Variáveis---- #

#tela / Global
difficulty_N = 0
difficulty = 1
hardculty = 1

boost = pygame.image.load(os.path.join(ASSETSDI,'Booster Mega_4.png'))
boost = pygame.transform.scale(boost, (150, 150))

najd = pygame.image.load(os.path.join(ASSETSDI,'Spaceship_blue.PNG'))
najd = pygame.transform.scale(najd, (100, 90))
najd = pygame.transform.rotate(najd, 45)

najd2 = pygame.image.load(os.path.join(ASSETSDI,'Spaceship_blue.PNG'))
najd2 = pygame.transform.scale(najd2, (150, 120))

najd3 = najd2
najd3 = pygame.transform.rotate(najd3, 90)

najbd = pygame.image.load(os.path.join(ASSETSDI,'laserBullet.png'))
najbd = pygame.transform.scale(najbd, (50, 50))
najbd = pygame.transform.rotate(najbd, 45)

naed = pygame.image.load(os.path.join(ASSETSDI,'Enemy.png'))
naed = pygame.transform.scale(naed, (50, 50))
naed = pygame.transform.rotate(naed, 45)

naebd = pygame.image.load(os.path.join(ASSETSDI,'Enemy_bullet.png'))
naebd = pygame.transform.scale(naebd, (30, 30))
naebd = pygame.transform.rotate(naebd, 45)

heal = pygame.mixer.Sound(os.path.join(ASSETSDI,'heal-up-39285.mp3'))
music = pygame.mixer.music.load(os.path.join(ASSETSDI,'M31.ogg'))
pygame.mixer.music.play(-1)

game_over = pygame.mixer.Sound(os.path.join(ASSETSDI,'game_over_1.mp3'))
clock = pygame.time.Clock()
tela = pygame.display.set_mode((1000, 800))
titulo('Unstracial')
started = False
over = False
lock = False
lock_s = False
table = [500]
space = pygame.image.load(os.path.join(ASSETSDI,'Space.png'))
space = pygame.transform.scale(space, (1000, 1000))

#Jogador
va = 0
numlife = 350
numlife2 = 350
heart_fullempty1 = pygame.image.load(os.path.join(ASSETSDI,'heart-1.png'))
heart_fullempty1 = pygame.transform.scale(heart_fullempty1, (50, 50))

heart_fullempty2 = pygame.image.load(os.path.join(ASSETSDI,'heart-1.png'))
heart_fullempty2 = pygame.transform.scale(heart_fullempty2, (50, 50))

heart_fullempty3 = pygame.image.load(os.path.join(ASSETSDI,'heart-1.png'))
heart_fullempty3 = pygame.transform.scale(heart_fullempty3, (50, 50))

heart_fullempty4 = pygame.image.load(os.path.join(ASSETSDI,'heart-1.png'))
heart_fullempty4 = pygame.transform.scale(heart_fullempty4, (50, 50))

heart_fullempty5 = pygame.image.load(os.path.join(ASSETSDI,'heart-1.png'))
heart_fullempty5 = pygame.transform.scale(heart_fullempty5, (50, 50))

heart_right = pygame.image.load(os.path.join(ASSETSDI,'heart-right-1.png'))
heart_right = pygame.transform.scale(heart_right, (50, 50))

heart_left = pygame.image.load(os.path.join(ASSETSDI,'heart-left-1.png'))
heart_left = pygame.transform.scale(heart_left, (50, 50))

taempty = [heart_fullempty1, heart_fullempty2, heart_fullempty3, heart_fullempty4, heart_fullempty5]
life  = 1

talife = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]# Três corações


shielded = 1

shield = pygame.image.load(os.path.join(ASSETSDI,'spr_shield.PNG'))
shield = pygame.transform.scale(shield, (70, 70))

shield_break = pygame.mixer.Sound(os.path.join(ASSETSDI,'Shield_break.wav'))
shield_break.set_volume(0.5)

dash = pygame.mixer.Sound(os.path.join(ASSETSDI,'Dash.wav'))
dash.set_volume(0.5)
movement = 5
mt= 0
hit = pygame.mixer.Sound(os.path.join(ASSETSDI,'Randomize16.wav'))
hit.set_volume(0.25)
tachose = []
vidas = 3
pos_x = 500
pos_y = 700
naj = pygame.image.load(os.path.join(ASSETSDI,'Spaceship.PNG'))
naj = pygame.transform.scale(naj, (200, 150))
naj2 = pygame.image.load(os.path.join(ASSETSDI,'Spaceship_blue.PNG'))
naj2 = pygame.transform.scale(naj2, (200, 150))
naj3 = pygame.image.load(os.path.join(ASSETSDI,'Spaceship_green.PNG'))
naj3 = pygame.transform.scale(naj3, (200, 150))
# inimigo
boom = pygame.mixer.Sound(os.path.join(ASSETSDI,'explosion.wav'))
boom.set_volume(0.25)
bullet_m = pygame.image.load(os.path.join(ASSETSDI,'Enemy_bullet.png'))
bullet_m = pygame.transform.scale(bullet_m, (50, 50))

di = random.randint(1, 2)

tablex = []
tabley = []
more = 1
count = 0
dl = 0
intensity  = 1
nae = pygame.image.load(os.path.join(ASSETSDI,'Enemy.png'))
nae = pygame.transform.scale(nae, (50, 50))
ex = pygame.image.load(os.path.join(ASSETSDI,'explosion.png'))
ex = pygame.transform.scale(ex, (50, 50))
explo = False
pos_xm = random.randint( 60, 940)
pos_ym = 75
pon = 0
#bala
pew = pygame.mixer.Sound(os.path.join(ASSETSDI,'alienshoot1.wav'))

ac = -1
bis = False
pos_xb = pos_x + 25
pos_yb = 700
nab = pygame.image.load(os.path.join(ASSETSDI,'laserBullet.png'))
nab = pygame.transform.scale(nab, (15, 15))
#bala inimiga
pew2 = pygame.mixer.Sound(os.path.join(ASSETSDI,'alienshoot2.wav'))
naeb = pygame.image.load(os.path.join(ASSETSDI,'Enemy_bullet.png'))
naeb = pygame.transform.scale(naeb, (30, 30))
shoot = random.randint(1, 2)
cap = random.randint(2 , 3) # - - - -- - - - CAP
count2 = 0
counter = 0
pos_xmb = [999]
pos_ymb = [999]
ic = False
numi = 0
bala_inimiga = pygame.draw.rect(tela, (255, 0, 0), (pos_xmb[numi], pos_ymb[numi], 15, 15))
#beserk

#Outros importantes
#level = (pon // 50) * 50
power_sound = pygame.mixer.Sound(os.path.join(ASSETSDI,'PowerUp1.wav'))
#chance
#shield
#
pos_xm2 = pos_xm
pos_ym2 = pos_ym

tapowex = [500]
tapowey = [500]
pw = False
pwc = random.randint(1, 1)
tapose = []
tapose2 = []
tahave = []
power_m = 0
power_numi = 0

multibullet = pygame.image.load(os.path.join(ASSETSDI,'multilaserbullet.png'))
multibullet = pygame.transform.scale(multibullet, (20, 20))

powerup_1 = pygame.image.load(os.path.join(ASSETSDI,'powerup.png'))
powerup_1 = pygame.transform.scale(powerup_1, (49, 49))

powerup_2 = pygame.image.load(os.path.join(ASSETSDI,'powerup-2.png'))
powerup_2 = pygame.transform.scale(powerup_2, (49, 49))


pod = 0
pod2 = 0
tab = [nab, multibullet]
tabc = 0

chance = random.randint(1, 100)
chancew = 0

warning = pygame.image.load(os.path.join(ASSETSDI,'warning.png'))
warning = pygame.transform.scale(warning, (100, 100))

meteor = pygame.image.load(os.path.join(ASSETSDI,'meteor.png'))
meteor = pygame.transform.scale(meteor, ( 150, 150))

meteor2 = pygame.image.load(os.path.join(ASSETSDI,'meteor-1.png.png'))
meteor2 = pygame.transform.scale(meteor2, ( 150, 150))

meteor3 = pygame.image.load(os.path.join(ASSETSDI,'meteor-2.png.png'))
meteor3 = pygame.transform.scale(meteor3, ( 150, 150))

meteor4 = pygame.image.load(os.path.join(ASSETSDI,'meteor-1.png.png'))
meteor4 = pygame.transform.scale(meteor4, ( 150, 150))

beserk_fire = pygame.image.load(os.path.join(ASSETSDI,'fireblast1.png'))
beserk_fire = pygame.transform.scale(beserk_fire, (150, 150))
beserk_fire = pygame.transform.rotate(beserk_fire, -90)

meteor_velocity = 5
meteor_timer = random.randint(300, 600)
meteor_counter = 0
meteor_counter2 = 0
meteor_counter3 = 0
meteor_numi = 1
beserk = False
beserkn = 1
meteor_table = [meteor, meteor2, meteor3, meteor4]

pos_xme = random.randint(150, 850)
pos_yme = -100

lockm1 = False

#locklock
lock1 = False
lock2 = False
lock3 = False
lock4 = False
lock5 = False
lock6 = False
lock7 = False
lock8 = False
lock9 = False
lock10 = False
lock11 = False
lock12 = False
lock13 = False
lock14 = False
lock15 = False
num = 1

j = True

#pod
#
#
#



while j:
    level = pon / 50
    level = level // 1
    clock.tick(60)
    pos_xb = pos_x + 18

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            j = False

    teclas = pygame.key.get_pressed()
    # iniciar
    if teclas[pygame.K_SPACE]:
        started = True
    if started == False:
        tela.blit(space, (0, 0))
        textador(tela, 'comicsans', 50, 'Introdução:', (255, 255, 255), True, (380, 0), 0)
        textador(tela, 'comicsans', 25, '[Pressione ESPAÇO para começar o jogo]', (255, 255, 255), True, (500, 750), 0)

        tela.blit(najd, (300, 300))
        tela.blit(najbd, (250, 250))
        tela.blit(naed, (200, 200))
        textador(tela, 'comicsans', 25, 'Espaço: Faz sua nave atirar', (255, 255, 255), True, (160, 425), 0)


        tela.blit(najd2, (650, 250))
        textador(tela, 'comicsans', 25, '[A/D| <-/->]', (255, 255, 255), True, (655, 400), 0)
        textador(tela, 'comicsans', 25, 'Movem a sua nave', (255, 255, 255), True, (625, 425), 0)

        tela.blit(boost,  (500, 500))
        tela.blit(najd3, (425, 500))
        textador(tela, 'comicsans', 25, '[W] = Dê um dash', (255, 255, 255), True, (400, 470), 0)
        textador(tela, 'comicsans', 50, '!OBJETIVO: SOBREVIVA!', (255, 0, 0), True, (190, 650), 0)

        pygame.display.update()
    elif over == False:

        #Seleção de personagens
        if lock_s == False:
            tela.blit(space, (0, 0))
            textador(tela, 'comicsans', 50, 'Selecione seu personagem:', (255, 255, 255), True, (200, 0), 0)

            textador(tela, 'comicsans', 25, 'Destroyer', (255, 255, 255), True, (140, 220), 0)
            textador(tela, 'comicsans', 25, '[Pressione R]', (255, 0, 0), True, (130, 450), 0)

            textador(tela, 'comicsans', 25, 'Outbreak', (255, 255, 255), True, (440, 220), 0)
            textador(tela, 'comicsans', 25, '[Pressione B]', (0, 0, 255), True, (430, 450), 0)

            textador(tela, 'comicsans', 25, 'Colossal', (255, 255, 255), True, (750, 220), 0)
            textador(tela, 'comicsans', 25, '[Pressione G]', (0, 255, 0), True, (730, 450), 0)

            tela.blit(naj, (100, 300))
            tela.blit(naj2, (400, 300))
            tela.blit(naj3, (700, 300))
            pygame.display.update()
            if teclas[pygame.K_b]:
                lock_s = True
                naj2 = pygame.transform.scale(naj2, (50, 50))

                tachose.append(naj2)
            if teclas[pygame.K_r]:
                lock_s = True
                naj = pygame.transform.scale(naj, (50, 50))
                tachose.append(naj)
            if teclas[pygame.K_g]:
                lock_s = True
                naj3 = pygame.transform.scale(naj3, (50, 50))
                tachose.append(naj3)
        else:
            # Escolha de dificuldade
            if lock9 == False:
                tela.blit(space, (0, 0))
                textador(tela, 'comicsans', 50, 'Escolha a dificuldade do jogo:', (255, 255, 255), True, (150, 100), 0)

                pygame.draw.rect(tela, (0, 255, 0), pygame.Rect(50, 225, 250, 475), 0)
                pygame.draw.rect(tela, (0, 0, 0), pygame.Rect(75, 250, 200, 425), 0)
                textador(tela, 'comicsans', 50, 'Fácil', (0, 255, 0), True, (120, 250), 0)
                textador(tela, 'comicsans', 12, 'Intensidade é multiplicada por 0.5', (255, 255, 255), True, (80, 350), 0)
                textador(tela, 'comicsans', 12, 'Tiros de inimigos são mais devagar', (255, 255, 255), True, (80, 375), 0)
                textador(tela, 'comicsans', 12, 'Meteoros são mais devagar', (255, 255, 255), True, (80, 400), 0)
                textador(tela, 'comicsans', 12, 'Tendência maior de powerups', (255, 255, 255), True, (80, 425), 0)
                textador(tela, 'comicsans', 24, '[Pressione 1]', (255, 255, 255), True, (100, 500), 0)

                pygame.draw.rect(tela, (255, 255, 0), pygame.Rect(375, 225, 250, 475), 0)
                pygame.draw.rect(tela, (0, 0, 0), pygame.Rect(400, 250, 200, 425), 0)
                textador(tela, 'comicsans', 50, 'Normal', (255, 255, 0), True, (415, 250), 0)
                textador(tela, 'comicsans', 12, 'Intensidade padrão', (255, 255, 255), True, (410, 350), 0)
                textador(tela, 'comicsans', 12, 'Tiros inimigos na velocidade padrão', (255, 255, 255), True, (405, 375), 0)
                textador(tela, 'comicsans', 12, 'Velocidade normal dos meteoros', (255, 255, 255), True, (410, 400), 0)
                textador(tela, 'comicsans', 12, 'Tendência padrão de powerups', (255, 255, 255), True, (410, 425), 0)
                textador(tela, 'comicsans', 24, '[Pressione 2]', (255, 255, 255), True, (425, 500), 0)

                pygame.draw.rect(tela, (255, 0, 0), pygame.Rect(700, 225, 250, 475), 0)
                pygame.draw.rect(tela, (0, 0, 0), pygame.Rect(725, 250, 200, 425), 0)
                textador(tela, 'comicsans', 50, 'Difícil', (255, 0, 0), True, (750, 250), 0)
                textador(tela, 'comicsans', 12, 'Intensidade multipliada por 1.5', (255, 255, 255), True, (740, 350), 0)
                textador(tela, 'comicsans', 12, 'Tiros dos inimigos são mais rápidos', (255, 255, 255), True, (730, 375), 0)
                textador(tela, 'comicsans', 12, 'Meteoros são mais rápidos', (255, 255, 255), True, (740, 400), 0)
                textador(tela, 'comicsans', 12, 'Powerups são bem raros', (255, 255, 255), True, (740, 425), 0)
                textador(tela, 'comicsans', 24, '[Pressione 3]', (255, 255, 255), True, (750, 500), 0)

                if teclas[pygame.K_1]: # Fácil
                    difficulty = 0.5
                    difficulty2 = 0.7
                    difficculty_N = 4
                    lock9 = True
                elif teclas[pygame.K_2]: # Normal
                    difficulty = 1
                    difficulty2 = 1
                    difficulty_N = 2
                    lock9 = True
                elif teclas[pygame.K_3]: # Difícil
                    difficulty = 1.5
                    difficulty2 = 1.25
                    hardculty = 1.25
                    difficulty_N = 0
                    lock9 = True
                pygame.display.update()
                #locklock
            else:
                # sistema de meteoros
                if pon >= 100 and lock2 == False: #and lockm1 == False:
                    meteor_counter = meteor_counter + 1 * beserkn * difficulty
                    if meteor_counter >= meteor_timer:
                        meteor_counter = 0
                        meteor_timer = random.randint(300, 600)
                        lockm1 = True

                # movimentação


                if teclas[pygame.K_d] and pos_x < 945:
                    pos_x = pos_x + movement

                if teclas[pygame.K_a] and pos_x > 5:
                    pos_x = pos_x - movement

                if teclas[pygame.K_RIGHT] and pos_x < 945 and not teclas[pygame.K_d]:
                    pos_x = pos_x + movement

                if teclas[pygame.K_LEFT] and pos_x < 945 and not teclas[pygame.K_a]:
                    pos_x = pos_x - movement

                tela.blit(space, (0, 0))

                if teclas[pygame.K_w] and mt == 0:
                    dash.play()
                    movement = 10
                    mt = mt + 1

                if mt >= 1:
                    mt= mt + 1
                    if mt >= 30:
                        movement = 5
                    if mt == 120:
                        mt = 0
                # Leveis
                if level == num and level != 0 and lock1 == False:
                    lock2 = True
                    textador(tela, 'comicsans', 50, f'Nível {level} completo!', (0, 255, 0), True, (275, 220), 0)
                    textador(tela, 'comicsans', 25, 'Pressione N para o próximo level', (255, 255, 255), True, (300, 320), 0)

                    if vidas < 5 and lock6 == False:
                        lock6 = True
                    #    for membro in talife:
                    #        if membro == 0:
                    #            va = va + 1
                    #            print(va)
                    #        if membro == talife.count(0) and lock14 == False:
                    #            lock14 = True
                    #            talife.insert(-va, 1)
                    #            print('')
                    #            talife.remove(talife[-va + 1])
                    #            print('')
                                
                        #va = 0
                        a = talife.count(0)
                        talife.insert(a * -1, 1)
                        talife.remove(talife[a * -1 + 1])
                        a = talife.count(0)
                        talife.insert(a * -1, 1)
                        talife.remove(talife[a * -1 + 1])

                        lock1 = False
                        vidas = vidas + 1
                        if vidas > 5:
                            vidas = 5
                            talife = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
                        heal.play()
                    if teclas[pygame.K_n] and lock4 == False:

                        num = num + 1
                        pos_xm = random.randint(60, 940)
                        pos_ym = 75
                        lock1 = True
                        lock2 = False
                        lock4 = True
                        lock6 = False

                # Intensidade
                if pon >= 10:
                    if pon < 50:
                        more = 1
                    elif pon >= 50 and pon < 100:
                        more = 2
                    elif pon >= 100 and pon < 150:
                        more = 3
                    elif pon >= 150 and pon < 250:
                        beserk = True
                        beserkn = 2
                        more = 4
                    else:
                        more = 5
                    intensity = difficulty * (1 + (more / 100) * pon)
                # Movimentação da nave inimiga
                
                dl = dl + 1 * intensity  # ---- Intensidade
                if dl >= 60:
                    dl = 0
                    pos_ym = pos_ym + 10
                    if pos_xm <= 60:
                        pos_xm = pos_xm + 20
                    if pos_xm >= 940:
                        pos_xm = pos_xm - 20
                    if di == 1:
                        di = random.randint(1, 2)
                        pos_xm = pos_xm - 10
                    else:
                        di = random.randint(1, 2)
                        pos_xm = pos_xm + 10

                # tiro da nave inimiga
                if pon >= 50:
                    if shoot == 1 and ic == False:
                        count = intensity * (count + 0.01)
                        if count > cap:
                            count = cap
                        if count == cap:
                            if lock2 == False:
                                pew2.play()
                            pos_xmb.append(pos_xm + 25)
                            pos_ymb.append(pos_ym + 25)
                            numi = numi + 1
                            count = 0
                            cap = random.randint(1, 2)
                            shoot = random.randint(1, 2)
                            ic = True
                    else:
                        shoot = random.randint(1, 2)
                    if ic == True:
                        pos_ymb[numi] = pos_ymb[numi] + 10 * difficulty2
                        pygame.draw.rect(tela, (0, 0, 0), (pos_xmb[numi], pos_ymb[numi], 15, 15))  # corrigido aqui?
                        # pygame.display.update()
                    if pos_ymb[numi] >= 925 * hardculty:
                        ic = False
                        pos_ymb[numi] = 999  # pos_ym#
                        pos_xmb[numi] = 999  # pos_xm#
                # hitbox do tiro do inimigo
                if pos_xmb[numi] in range(pos_x, pos_x + 50) and pos_ymb[numi] in range(pos_y, pos_y + 50) and lock5 == False:

                    if lock == False:
                        lock = True
                        hit.play()
                    #print('ACERTOU!!')
                    lock5 = True
                    vidas = vidas - 1 / shielded
                    
                    #for membro in talife:
                    #    if membro == 1:
                    #        va = va + 1
                    #        #print(va)
                    #    if membro == talife[-1]:
                    #        talife.insert(va, 0)
                    #        talife.remove(talife[va - 1])
                    #        if shielded == 1:
                    #            talife.insert(va, 0)
                    #            talife.remove(talife[va - 2])
                    #locklock
                    a = talife.count(1)
                    talife.insert(a, 0)
                    #print(list(talife))
                    talife.remove(talife[a - 1])
                    if shielded == 1:
                        a = talife.count(1)
                        talife.insert(a, 0)
                        #print(list(talife))
                        talife.remove(talife[a - 1])
       
                    #va = 0
                    if shielded == 2:
                        shielded = 1
                        tahave.remove('shield')
                        shield_break.play()

                if lock5 == True:
                    count2 = count2 + 1
                    #print(count2)
                    if count2 >= 100:
                        count2 = 0
                        lock = False
                        lock5 = False


                if pos_ym >= 700:
                    hit.play()
                    pos_xm = random.randint(60, 940)
                    pos_ym = 75
                    vidas = vidas - 1
                    a = talife.count(1)
                    talife.insert(a, 0)
                    #print(list(talife))
                    talife.remove(talife[a - 1])

                    a = talife.count(1)
                    talife.insert(a, 0)
                    #print(list(talife))
                    talife.remove(talife[a - 1])
                # tiro

                if teclas[pygame.K_SPACE] and bis == False and over == False:
                    pew.play()
                    lock13 = False
                    #print('input aceito')
                    #print(table)
                    #print(f'{pos_xm} x {pos_ym}, pontuação: {pon}')
                    bis = True
                    if lock3 == False:
                        table.append(pos_xb)
                        lock3 = True
                    else:
                        table.remove(table[0])
                        table.append(pos_xb)
                    ac = 0

                    #print(table)
                if ac >= 0:
                    pygame.draw.rect(tela, (0, 0, 0), pygame.Rect(table[-1], pos_yb, 15 + pod2, 10 + pod))  # Tiro
                    tela.blit(tab[tabc], (table[-1], pos_yb))
                    pos_yb = pos_yb - 10
                    ac = ac + 1
                    if ac > 70:
                        ac = -1
                        bis = False
                        pos_yb = 700
                #rect
                # Hitbox
                for membro in tahave:
                    if membro == 'double shoot' and lock13 == False:
                        lock13 = True
                        tabc = 1
                        pod = 10
                        pod2 = 7
                    if membro == 'shield': 
                        shielded = 2
                        tela.blit(shield,(pos_x - 10, pos_y - 10))

                if table[-1] in range(pos_xm - pod, pos_xm + 50 + pod2) and pos_yb in range(pos_ym - 50 - pod, pos_ym + 30 + pod):
                    lock7 = False
                    lock = False
                    lock1 = False
                    lock4 = False
                    pon = pon + 10  # pon aumenta
                    tablex.append(pos_xm)
                    tabley.append(pos_ym)
                    explo = True

                    if chance <= chancew and lock12 == False:
                        pos_xm2 = pos_xm
                        pos_ym2 = pos_ym
                        chancew = 0
                        lock12 = True
                        pw = True
                    else:
                        chancew = chancew + difficulty_N + 1  #CHANCE DE UM POWERUP APARECER
                        chance = random.randint(1, 100)
                    pos_xm = random.randint(60, 940)
                    pos_ym = 75
                # powerup
                if pw == True:
                    if lock15 == False:
                        pwc = random.randint(1, 2)
                        lock15 = True
                    if pwc == 1:
                        tapose.append(powerup_1)
                        tapose2.append('double shoot')
                    if pwc == 2:
                        tapose.append(powerup_2)
                        tapose2.append('shield')
                    pygame.draw.rect(tela, (0, 0, 0), pygame.Rect(pos_xm2, pos_ym2, 50, 50))
                    tela.blit(tapose[-1], (pos_xm2, pos_ym2))

                    power_m = power_m + 1
                    if power_m >= 10:
                        power_m = 0
                        pos_ym2 = pos_ym2 + 10
                    if pos_ym2 >= 850:
                        pw = False
                        lock12 = False
                        #lock14 = False
                        lock15 = False
                # hitbox do powerup

                if pos_x in range(pos_xm2, pos_xm2 + 50) and pos_y in range(pos_ym2 - 50, pos_ym2 + 50):
                    
                    lock15 = False
                    #lock14 = False
                    lock12 = False
                    pw = False
                    pos_xm2 = 9999
                    pos_ym2 = 9999
                    if tapose2[-1] not in tahave:
                        power_sound.play()
                        tahave.append(tapose2[-1])
                        
                # explosões :D
                if explo == True:
                    if lock7 == False:
                        lock7 = True
                        boom.play()
                    tela.blit(ex, (tablex[-1], tabley[-1]))
                    count = count + 1
                    if count == 20:
                        lock7 = False
                        count = 0
                        explo = False
                if pon < 50:  # 50
                    textador(tela, 'comicsans', 30, f'Pontuação: {pon}', (255, 255, 255), True, (50, 0), 0)
                    #textador(tela, 'comicsans', 30, f'Vidas: {vidas}', (255, 255, 255), True, (400, 0))
                    textador(tela, 'comicsans', 30, f'Intensidade: {intensity:.2f}', (255, 255, 255), True, (700, 0), 0)
                elif pon >= 50 and pon < 100: # 100
                    textador(tela, 'comicsans', 30, f'Pontuação: {pon}', (255, 255, 0), True, (50, 0), 0)
                    #textador(tela, 'comicsans', 30, f'Vidas: {vidas}', (255, 255, 0), True, (400, 0))
                    textador(tela, 'comicsans', 30, f'Intensidade: {intensity:2f}', (255, 255, 0), True, (700, 0), 0)

                elif pon >=  100 and pon < 150:  # 150
                    textador(tela, 'comicsans', 30, f'Pontuação: {pon}', (255, 0, 0), True, (50, 0), 0)
                    #textador(tela, 'comicsans', 30, f'Vidas: {vidas}', (255, 0, 0), True, (400, 0))
                    textador(tela, 'comicsans', 30, f'Intensidade: {intensity:2f}', (255, 0, 0), True, (700, 0), 0)
                else: # 150 até o infinito
                    textador(tela, 'comicsans', 30, f'Pontuação: {pon}', pygame.color.Color('purple'), True, (50, 0), 0)
                    #textador(tela, 'comicsans', 30, f'Vidas: {vidas}', pygame.color.Color('purple'), True, (400, 0))
                    textador(tela, 'comicsans', 30, f'Intensidade: {intensity:2f}', pygame.color.Color('purple'), True, (700, 0), 0)

                # desenhos
                # pygame.draw.rect(tela, (255, 0, 0), (pos_xmb[0], pos_ymb[0], 15, 15))
                #pygame.draw.rect(tela, (0, 0, 0), pygame.Rect(pos_x, pos_y, 50, 50))
                #pygame.draw.rect(tela, (0, 0, 0), pygame.Rect(pos_xm, pos_ym, 50, 50))

                if lock2 == True:
                    pos_xm = 9999
                    pos_ym = -999

                #tela.blit(shield, (pos_x - 10, pos_y - 10))
                for membro in taempty:
                    tela.blit(membro, (numlife, 20))
                    numlife = numlife + 50
                    if numlife >= 600:
                        numlife = 350

                for membro in talife:
                    #Primeiro coração
                    if membro == talife[0] and membro != 0:
                        tela.blit(heart_left, (350, 20))

                    if membro == talife[1] and membro != 0:
                        tela.blit(heart_right, (350, 20))

                    #Segundo coração
                    if membro == talife[2] and membro != 0:
                        tela.blit(heart_left, (400, 20))

                    if membro == talife[3] and membro != 0:
                        tela.blit(heart_right, (400, 20))

                    #terceiro coração
                    if membro  == talife[4] and membro != 0:
                        tela.blit(heart_left, (450, 20))

                    if membro == talife[5] and membro != 0:
                        tela.blit(heart_right, (450, 20))

                    #Quarto coração
                    if membro == talife[6] and membro != 0:
                        tela.blit(heart_left, (500, 20))

                    if membro == talife[7] and membro != 0:
                        tela.blit(heart_right, (500, 20))

                    #Quinto coração
                    if membro == talife[8] and membro != 0:
                        tela.blit(heart_left, (550, 20))

                    if membro == talife[9] and membro != 0:
                        tela.blit(heart_right, (550, 20))



                #print(list(talife))
                tela.blit(naeb, (pos_xmb[numi] - 7, pos_ymb[numi] - 10))
                tela.blit(tachose[0], (pos_x, pos_y))
                tela.blit(nae, (pos_xm, pos_ym))
                #print(list(talife))
                
                # meteoro em ação
                if lockm1 == True:
                    #print('METEORO!')
                    tela.blit(warning, (pos_xme + 25, 400))
                    #pygame.draw.rect(tela, (0, 0, 0), pygame.Rect(pos_xme, pos_yme, 150, 150))
                    if beserk == True:
                        meteor_velocity = 10
                        tela.blit(beserk_fire, (pos_xme, pos_yme))
                    else:
                        meteor_velocity = 5

                    pos_yme = pos_yme + meteor_velocity * difficulty2# velocidade de descida
                    pos_yme = int(pos_yme) #// 1
                    tela.blit(meteor_table[meteor_numi], (pos_xme, pos_yme))
                    meteor_counter2 = meteor_counter2 + 1
                    if meteor_counter2 == 10: # animação
                        meteor_counter2 = 0
                        tela.blit(meteor_table[meteor_numi], (pos_xme, pos_yme))
                        meteor_numi = meteor_numi + 1
                        if meteor_numi >= 4:
                            meteor_numi = 0

                    if pos_yme > 850:
                        lockm1 = False
                        pos_xme = random.randint(150, 850)
                        pos_yme = - 100

                    #meteoro hitbox
                    if pos_x in range(pos_xme, pos_xme + 150) and pos_y in range(pos_yme, pos_yme + 150) and lock11 == False:

                        hit.play()

                                    
                        if beserk == False:
                            vidas = vidas - 1 / shielded
                            a = talife.count(1)
                            talife.insert(a, 0)
                            talife.remove(talife[a - 1])
                            if shielded == 1:
                                a = talife.count(1)
                                talife.insert(a, 0)
                                talife.remove(talife[a - 1])
                        else:
                            vidas = vidas - 2 / shielded
                            a = talife.count(1)
                            talife.insert(a, 0)
                            talife.remove(talife[a - 1])
                            a = talife.count(1)
                            talife.insert(a, 0)
                            talife.remove(talife[a - 1])
                            if shielded == 1:
                                a = talife.count(1)
                                talife.insert(a, 0)
                                talife.remove(talife[a - 1])
                                a = talife.count(1)
                                talife.insert(a, 0)
                                talife.remove(talife[a - 1])
                        if shielded == 2:
                            shielded = 1
                            for membro in tahave:
                                if membro == 'shield':
                                    tahave.remove(membro)
                            shield_break.play()
                        lock11 = True
                    if lock11 == True:
                        meteor_counter3 = meteor_counter3 + 1
                        if meteor_counter3 >= 100:
                            meteor_counter3 = 0
                            lock11 = False


                #print(f'{tahave}, {shielded}')
                #print(f'{meteor_timer} x {meteor_counter} x {lockm1}')
                pygame.display.update()
            
                # game over44
            if vidas <= 0:
                if lock8 == False:
                    lock8 = True
                    game_over.play()
                #print('game over')
                over = True
                over1 = True

    else:
            # if tela.blit(space, (0, 0))lock == False:
            # lock = True
        tela.blit(space, (0, 0))
        textador(tela, 'comicsans', 100, 'Game Over', (255, 0, 0), True, (250, 100), 0)
        textador(tela, 'comicsans', 25, f'Pontuação total: {pon}', (255, 255, 255), True, (375, 300), 0)
        textador(tela, 'comicsans', 25, f'Pressione R para recomeçar', (255, 255, 255), True, (375, 350), 0)
        pos_xm = random.randint(60, 940)
        pos_ym = 75
        pygame.display.update()
            # restart?
        if teclas[pygame.K_r]:
            lock2 = False
            talife = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
            va = 0
            shielded = 1
            tablowex = [500]
            tablowey = [500]
            lock12 = False
            tabc = 0
            pod = 0
            pod2 = 0
            tapose2 = ['']
            tapose = []
            tahave = []
            beserk = False
            hardculty = 1
            pon = 0
            vidas = 3
            over = False
            Lock = False
            lock9 = False
            pos_xm = random.randint(60, 940)
            pos_ym = 75
            pos_xmb[numi] = 999
            pos_ymb[numi] = 999
            pos_x = 500
            num = 1
            intensity = 1 + (more / 50) * pon
            lock8 = False
            pygame.display.update()


pygame.quit()

#va
#None
#print
#pygame.draw.rect
#tela
#lock1
#time.sleep
#pos_ym
#pos_x
#pos_ymb
#lock2
#meteor_angle
#lock13
#double_shoot
#chance
# ESTOU LENTAMENTE APRIMORANDO O CÓDIGO, IREI(depende se acabei ou não) COLOCAR AINDA MAIS ATUALIZAÇÕES NESSE JOGO!
#(curiosidade: Este foi o meu primeiro jogo com mais de 700 linhas, esse mesmo jogo foi capaz de inspirar uma pessoa a programar, 99% do código foi feito de cabeça enquanto uma parte foi com auxilio do Chatgbt, partes não apagadas do código (como os #s) são partes de código que existiam nas versões anteriores deste jogo, uma das ideias de nome do jogo fazia com que o tradutor do google identificasse como 'merda' literalmente, o som do Dash foi feito por mim utilizando um site (por isso é de baixa qualidade comparado aos outros))