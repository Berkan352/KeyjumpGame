import random
import pygame



def easy():
    def res():
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((600, 600))

        font = pygame.font.Font(None, 120)
        font2 = pygame.font.Font(None, 60)
        font3 = pygame.font.Font(None, 40)

        txt1 = font2.render("Score", 1, (139, 69, 19))
        if timer > 0 and puan>1000:
            txt_puan = font3.render(str(puan+(10*(timer))), 1, ("gray15"))
        else:
            txt_puan = font3.render(str(puan), 1, ("gray15"))
        txt2 = font2.render("Time", 1, (139, 69, 19))
        if 10 - timer <= 10:
            txt_time = font3.render("%.2f second" % (10 - timer), 1, ("gray15"))
        else:
            txt_time = font3.render("10", 1, ("gray15"))

        done = False
        while not done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            screen.fill((152, 245, 255))

            screen.blit(txt1, (200, 20))
            screen.blit(txt_puan, (220, 100))
            screen.blit(txt2, (210, 160))
            screen.blit(txt_time,(220,220))
            pygame.display.flip()
            clock.tick(30)
    kelimeler = open("kolay.txt", "r", encoding='utf-8')
    kelimeler = kelimeler.read()
    kelimeler = kelimeler.split()
    kolay=[]
    yasak=["fuck","fucker","fucked","vagina","penis","motherfucker","porn","dick","pussy","ass","dildo","bdsm"]#eliminate bad words
    for l in range(len(kelimeler)):
        if len(kelimeler[l])==4 and kelimeler[l] not in yasak:
            kolay.append(kelimeler[l])

    class Player(pygame.sprite.Sprite):
        # sprite for the player
        def __init__(self,surx,sury):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("katman3.png")
            self.image = pygame.transform.scale(self.image, (120, 20))
            self.rect = self.image.get_rect()
            self.rect.center = (surx, sury)


    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    katx=200
    katx2=70
    all_sprite = pygame.sprite.Group()
    player6 = Player(katx, 60)
    player7 = Player(katx2, 120)
    player8 = Player(katx, 180)
    player9 = Player(katx2, 240)
    player10 = Player(katx,300)
    player11 = Player(katx2, 360)
    player12 = Player(katx, 420)
    player13 = Player(katx2, 480)
    player14 = Player(katx, 540)
    player15 = Player(katx2, 600)


    all_sprite.add(player6,player7,player8,player9,player10,player11,player12,
                   player13,player14,player15)
    font = pygame.font.Font(None, 25)
    font2 = pygame.font.Font(None, 28)
    timer = 15
    dt = 0
    user_text = ""

    color_active = pygame.Color("green")
    color_passive = pygame.Color("gray15")
    color = color_passive
    active = True
    ball=pygame.image.load("character.png")
    ball2=pygame.image.load("character 2.png")
    ball = pygame.transform.scale(ball, (120, 60))
    ball2=pygame.transform.scale(ball2,(120,60))
    ballx=0
    bally=538

    can=pygame.image.load("can.png")
    can1=pygame.transform.scale(can,(30,30))
    can2 = pygame.transform.scale(can, (30, 30))
    can3 = pygame.transform.scale(can, (30, 30))
    can4 = pygame.transform.scale(can, (30, 30))
    can5 = pygame.transform.scale(can, (30, 30))

    elmas=pygame.image.load("elmas.png")
    yildiz=pygame.image.load("yildiz.png")
    yildiz1 = pygame.transform.scale(yildiz, (30, 30))
    yildiz2 = pygame.transform.scale(yildiz, (30, 30))
    yildiz3 = pygame.transform.scale(yildiz, (30, 30))
    yildiz4 = pygame.transform.scale(yildiz, (30, 30))
    yildiz5 = pygame.transform.scale(yildiz, (30, 30))
    yildiz6 = pygame.transform.scale(yildiz, (30, 30))
    yildiz7 = pygame.transform.scale(yildiz, (30, 30))
    yildiz8 = pygame.transform.scale(yildiz, (30, 30))
    elmas = pygame.transform.scale(elmas, (30, 30))

    carpi=pygame.image.load("carpi.png")
    carpi=pygame.transform.scale(carpi, (30, 30))
    asl_txt=random.choice(kolay)
    txt1 = font2.render(asl_txt, True, (139, 69 ,19))
    txt1x=380
    txt1y=535
    input_rect = pygame.Rect(txt1x-80,txt1y+23, 140, 32)
    puan=0
    puan1=font.render("Score: {}".format(str(puan)),True,(139 ,69 ,19))
    dogru=0
    hak=5
    sayac=0
    sinir=120
    sinir2=500
    sonZaman=0
    deneme=False
    deneme2=False
    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_RETURN:
                        if asl_txt == user_text:
                            txt1y-=55
                            deneme=True
                            dogru +=1

                            if dogru == 1:
                                yildiz1.fill((152,245,255))
                            elif dogru == 2:
                                yildiz2.fill((152,245,255))
                            elif dogru == 3:
                                yildiz3.fill((152,245,255))
                            elif dogru == 4:
                                yildiz4.fill((152,245,255))
                            elif dogru == 5:
                                yildiz5.fill((152,245,255))
                            elif dogru == 6:
                                yildiz6.fill((152,245,255))
                            elif dogru == 7:
                                yildiz7.fill((152,245,255))
                            elif dogru == 8:
                                yildiz8.fill((152,245,255))
                            elif dogru == 9:
                                elmas.fill((152,245,255))
                                puan += 1000

                            input_rect = pygame.Rect(txt1x - 80, txt1y + 20, 140, 32)
                            puan +=10
                            asl_txt = random.choice(kolay)
                            txt1 = font2.render(asl_txt, True, (139, 69 ,19))
                            puan1 = font.render("Score: {}".format(str(puan)), True, (139, 69 ,19))
                            user_text=""
                        else:
                            dogru -=1
                            hak -=1
                            deneme2=True
                            if hak == 4:
                                can1=carpi
                            elif hak == 3:
                                can2=carpi
                            elif hak == 2:
                                can3=carpi
                            elif hak == 1:
                                can4=carpi
                            elif hak == 0:
                                can5=carpi
                            puan1 = font.render("Score: {}".format(str(puan)), True, (139, 69 ,19))
                            if bally<500:
                                txt1y += 55

                                input_rect = pygame.Rect(txt1x - 80, txt1y + 30, 140, 32)
                                asl_txt = random.choice(kolay)
                                txt1 = font2.render(asl_txt, True, (139, 69 ,19))
                                user_text = ""
                            else:
                                user_text = ""
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        timer -= dt
        if timer <= 0:
            res()
            done=True

        screen.fill((152,245,255))
        if active:
            color = color_active
        else:
            color = color_passive


        screen.blit(yildiz1, (185, 500))
        screen.blit(yildiz2, (55, 440))
        screen.blit(yildiz3, (185, 380))
        screen.blit(yildiz4, (55, 320))
        screen.blit(yildiz5, (185, 260))
        screen.blit(yildiz6, (55, 200))
        screen.blit(yildiz7, (185, 140))
        screen.blit(yildiz8, (55, 80))
        screen.blit(elmas, (185, 20))
        screen.blit(ball, (ballx, bally))
        simdikiZaman=pygame.time.get_ticks()
        if simdikiZaman-sonZaman > 550:
            sonZaman=simdikiZaman
            screen.blit(ball2, (ballx, bally))

        if deneme:
            if sayac <= 12:
                bally-=5
                if ballx < sinir:
                    ballx += 10.83
                else:
                    ballx -= 10.83
                    sinir-=10.83
                sayac +=1
                if sayac ==12:
                    sayac=0
                    sinir=120
                    deneme=False

            else:
                deneme=False
                sayac=0
        if deneme2:
            if sayac <= 12:
                if bally<sinir2:
                    bally+=5
                    sinir2+=5
                    if ballx < sinir:
                        ballx += 10.83
                    else:
                        ballx -= 10.83
                        sinir-=10.83

                sayac +=1
                if sayac ==12:
                    sayac=0
                    sinir=120
                    sinir2=500
                    deneme2=False

            else:
                deneme=False
                sayac=0


        screen.blit(can1, (0,0))
        screen.blit(can2, (30, 0))
        screen.blit(can3, (60, 0))
        screen.blit(can4, (90, 0))
        screen.blit(can5, (120, 0))



        txt = font.render(str(round(timer, 2)), True, (139 ,69 ,19))
        screen.blit(txt, (530, 10))
        screen.blit(puan1,(0,30))
        screen.blit(txt1, (txt1x,txt1y))
        pygame.draw.rect(screen, color, input_rect, 2)
        text_surface = font.render(user_text, 1, (54, 54 ,54))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        all_sprite.draw(screen)
        if puan>1000:
            res()
            done = True
        if hak ==0:
            res()
            done = True
        input_rect.w = max(250, text_surface.get_width() + 10)


        pygame.display.flip()
        dt = clock.tick(30) / 1000

def medium():
    def res():
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((600, 600))

        font = pygame.font.Font(None, 120)
        font2 = pygame.font.Font(None, 60)
        font3 = pygame.font.Font(None, 40)

        txt1 = font2.render("Score", 1, (139, 69, 19))
        if timer > 0 and puan > 1000:
            txt_puan = font3.render(str(puan + (10 * (timer))), 1, ("gray15"))
        else:
            txt_puan = font3.render(str(puan), 1, ("gray15"))
        txt2 = font2.render("Time", 1, (139, 69, 19))
        if 15-timer <= 15:
            txt_time = font3.render("%.2f second" % (15 - timer), 1, ("gray15"))
        else:
            txt_time = font3.render("15", 1, ("gray15"))

        done = False
        while not done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            screen.fill((152, 245, 255))

            screen.blit(txt1, (200, 20))

            screen.blit(txt_puan, (220, 100))
            screen.blit(txt2, (210, 160))
            screen.blit(txt_time,(220,220))
            pygame.display.flip()
            clock.tick(30)
    kelimeler = open("kolay.txt", "r", encoding='utf-8')#getting words from txt file
    kelimeler = kelimeler.read()
    kelimeler = kelimeler.split()
    kolay=[]
    yasak=["fuck","fucker","fucked","vagina","penis","motherfucker","porn","dick","pussy","dildo","bdsm","niger"]#eliminate bad words
    for l in range(len(kelimeler)):
        if len(kelimeler[l])==5 and kelimeler[l] not in yasak:#getting medium episodes words
            kolay.append(kelimeler[l])


    class Player(pygame.sprite.Sprite):#initiliaze sprites
        # sprite for the player
        def __init__(self,surx,sury):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("katman3.png")
            self.image = pygame.transform.scale(self.image, (120, 20))
            self.rect = self.image.get_rect()
            self.rect.center = (surx, sury)


    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    katx=200
    katx2=70
    all_sprite = pygame.sprite.Group()
    player6 = Player(katx, 60)
    player7 = Player(katx2, 120)
    player8 = Player(katx, 180)
    player9 = Player(katx2, 240)
    player10 = Player(katx,300)
    player11 = Player(katx2, 360)
    player12 = Player(katx, 420)
    player13 = Player(katx2, 480)
    player14 = Player(katx, 540)
    player15 = Player(katx2, 600)#creating sprites


    all_sprite.add(player6,player7,player8,player9,player10,player11,player12,
                   player13,player14,player15)
    font = pygame.font.Font(None, 25)
    font2 = pygame.font.Font(None, 28)
    timer = 15
    dt = 0
    user_text = ""

    color_active = pygame.Color("green")
    color_passive = pygame.Color("gray15")
    color = color_passive
    active = True
    ball=pygame.image.load("character.png")
    ball2=pygame.image.load("character 2.png")
    ball = pygame.transform.scale(ball, (120, 60))
    ball2=pygame.transform.scale(ball2,(120,60))
    ballx=0
    bally=538

    can=pygame.image.load("can.png")
    can1=pygame.transform.scale(can,(30,30))
    can2 = pygame.transform.scale(can, (30, 30))
    can3 = pygame.transform.scale(can, (30, 30))
    can4 = pygame.transform.scale(can, (30, 30))
    can5 = pygame.transform.scale(can, (30, 30))

    elmas=pygame.image.load("elmas.png")
    yildiz=pygame.image.load("yildiz.png")
    yildiz1 = pygame.transform.scale(yildiz, (30, 30))
    yildiz2 = pygame.transform.scale(yildiz, (30, 30))
    yildiz3 = pygame.transform.scale(yildiz, (30, 30))
    yildiz4 = pygame.transform.scale(yildiz, (30, 30))
    yildiz5 = pygame.transform.scale(yildiz, (30, 30))
    yildiz6 = pygame.transform.scale(yildiz, (30, 30))
    yildiz7 = pygame.transform.scale(yildiz, (30, 30))
    yildiz8 = pygame.transform.scale(yildiz, (30, 30))
    elmas = pygame.transform.scale(elmas, (30, 30))

    carpi=pygame.image.load("carpi.png")
    carpi=pygame.transform.scale(carpi, (30, 30))
    asl_txt=random.choice(kolay)
    txt1 = font2.render(asl_txt, True, (139, 69 ,19))
    txt1x=380
    txt1y=535
    input_rect = pygame.Rect(txt1x-80,txt1y+23, 140, 32)
    puan=0
    puan1=font.render("Score: {}".format(str(puan)),True,(139 ,69 ,19))
    dogru=0
    hak=3
    sayac=0
    sinir=120
    sinir2=500
    sonZaman=0
    deneme=False
    deneme2=False
    done = False
    while not done:#creating game loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_RETURN:
                        if asl_txt == user_text:
                            txt1y-=55
                            deneme=True
                            dogru +=1

                            if dogru == 1:
                                yildiz1.fill((152,245,255))
                            elif dogru == 2:
                                yildiz2.fill((152,245,255))
                            elif dogru == 3:
                                yildiz3.fill((152,245,255))
                            elif dogru == 4:
                                yildiz4.fill((152,245,255))
                            elif dogru == 5:
                                yildiz5.fill((152,245,255))
                            elif dogru == 6:
                                yildiz6.fill((152,245,255))
                            elif dogru == 7:
                                yildiz7.fill((152,245,255))
                            elif dogru == 8:
                                yildiz8.fill((152,245,255))
                            elif dogru == 9:
                                elmas.fill((152,245,255))
                                puan += 1000

                            input_rect = pygame.Rect(txt1x - 80, txt1y + 20, 140, 32)
                            puan +=10
                            asl_txt = random.choice(kolay)
                            txt1 = font2.render(asl_txt, True, (139, 69 ,19))
                            puan1 = font.render("Score: {}".format(str(puan)), True, (139, 69 ,19))
                            user_text=""
                        else:
                            dogru -=1
                            hak -=1
                            deneme2=True
                            if hak == 2:
                                can3=carpi
                            elif hak == 1:
                                can4=carpi
                            elif hak == 0:
                                can5=carpi
                            puan1 = font.render("Score: {}".format(str(puan)), True, (139, 69 ,19))
                            if bally<500:
                                txt1y += 55

                                input_rect = pygame.Rect(txt1x - 80, txt1y + 30, 140, 32)
                                asl_txt = random.choice(kolay)
                                txt1 = font2.render(asl_txt, True, (139, 69 ,19))
                                user_text = ""
                            else:
                                user_text = ""
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        timer -= dt
        if timer <= 0:
            res()
            done=True

        screen.fill((152,245,255))
        if active:
            color = color_active
        else:
            color = color_passive


        screen.blit(yildiz1, (185, 500))
        screen.blit(yildiz2, (55, 440))
        screen.blit(yildiz3, (185, 380))
        screen.blit(yildiz4, (55, 320))
        screen.blit(yildiz5, (185, 260))
        screen.blit(yildiz6, (55, 200))
        screen.blit(yildiz7, (185, 140))
        screen.blit(yildiz8, (55, 80))
        screen.blit(elmas, (185, 20))
        screen.blit(ball, (ballx, bally))
        simdikiZaman=pygame.time.get_ticks()
        if simdikiZaman-sonZaman > 550:
            sonZaman=simdikiZaman
            screen.blit(ball2, (ballx, bally))

        if deneme:
            if sayac <= 12:
                bally-=5
                if ballx < sinir:
                    ballx += 10.83
                else:
                    ballx -= 10.83
                    sinir-=10.83
                sayac +=1
                if sayac ==12:
                    sayac=0
                    sinir=120
                    deneme=False

            else:
                deneme=False
                sayac=0
        if deneme2:
            if sayac <= 12:
                if bally<sinir2:
                    bally+=5
                    sinir2+=5
                    if ballx < sinir:
                        ballx += 10.83
                    else:
                        ballx -= 10.83
                        sinir-=10.83

                sayac +=1
                if sayac ==12:
                    sayac=0
                    sinir=120
                    sinir2=500
                    deneme2=False

            else:
                deneme=False
                sayac=0


        screen.blit(can3, (0, 0))
        screen.blit(can4, (30, 0))
        screen.blit(can5, (60, 0))

        txt = font.render(str(round(timer, 2)), True, (139 ,69 ,19))
        screen.blit(txt, (530, 10))
        screen.blit(puan1,(0,30))
        screen.blit(txt1, (txt1x,txt1y))
        pygame.draw.rect(screen, color, input_rect, 2)
        text_surface = font.render(user_text, 1, (54, 54 ,54))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        all_sprite.draw(screen)
        if puan>1000 or hak ==0:
            res()
            done = True
        input_rect.w = max(250, text_surface.get_width() + 10)


        pygame.display.flip()
        dt = clock.tick(30) / 1000


def hard():
    def res():
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((600, 600))

        font = pygame.font.Font(None, 120)
        font2 = pygame.font.Font(None, 60)
        font3 = pygame.font.Font(None, 40)

        txt1 = font2.render("Score", 1, (139, 69, 19))
        if timer > 0 and puan>1000:
            txt_puan = font3.render(str(puan + (10 * (timer))), 1, ("gray15"))
        else:
            txt_puan = font3.render(str(puan), 1, ("gray15"))
        txt2 = font2.render("Time", 1, (139, 69, 19))
        if 20-timer <= 20:
            txt_time=font3.render("%.2f second"%(20-timer), 1, ("gray15"))
        else:
            txt_time = font3.render("20", 1, ("gray15"))

        done = False
        while not done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            screen.fill((152, 245, 255))

            screen.blit(txt1, (200, 20))
            screen.blit(txt_puan, (220, 100))
            screen.blit(txt2, (210, 160))
            screen.blit(txt_time,(220,220))
            pygame.display.flip()
            clock.tick(30)
    kelimeler = open("kolay.txt", "r", encoding='utf-8')
    kelimeler = kelimeler.read()
    kelimeler = kelimeler.split()
    kolay=[]
    yasak=["fuck","fucker","fucked","vagina","penis","motherfucker"]
    for l in range(len(kelimeler)):
        if len(kelimeler[l])>5 and kelimeler[l] not in yasak:
            kolay.append(kelimeler[l])

    class Player(pygame.sprite.Sprite):
        # sprite for the player
        def __init__(self,surx,sury):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("katman3.png")
            self.image = pygame.transform.scale(self.image, (120, 20))
            self.rect = self.image.get_rect()
            self.rect.center = (surx, sury)


    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    katx=200
    katx2=70
    all_sprite = pygame.sprite.Group()
    player6 = Player(katx, 60)
    player7 = Player(katx2, 120)
    player8 = Player(katx, 180)
    player9 = Player(katx2, 240)
    player10 = Player(katx,300)
    player11 = Player(katx2, 360)
    player12 = Player(katx, 420)
    player13 = Player(katx2, 480)
    player14 = Player(katx, 540)
    player15 = Player(katx2, 600)


    all_sprite.add(player6,player7,player8,player9,player10,player11,player12,
                   player13,player14,player15)
    font = pygame.font.Font(None, 25)
    font2 = pygame.font.Font(None, 28)
    timer = 20
    dt = 0
    user_text = ""

    color_active = pygame.Color("green")
    color_passive = pygame.Color("gray15")
    color = color_passive
    active = True
    ball=pygame.image.load("character.png")
    ball2=pygame.image.load("character 2.png")
    ball = pygame.transform.scale(ball, (120, 60))
    ball2=pygame.transform.scale(ball2,(120,60))
    ballx=0
    bally=538

    can=pygame.image.load("can.png")
    can1=pygame.transform.scale(can,(30,30))
    can2 = pygame.transform.scale(can, (30, 30))
    can3 = pygame.transform.scale(can, (30, 30))
    can4 = pygame.transform.scale(can, (30, 30))
    can5 = pygame.transform.scale(can, (30, 30))

    elmas=pygame.image.load("elmas.png")
    yildiz=pygame.image.load("yildiz.png")
    yildiz1 = pygame.transform.scale(yildiz, (30, 30))
    yildiz2 = pygame.transform.scale(yildiz, (30, 30))
    yildiz3 = pygame.transform.scale(yildiz, (30, 30))
    yildiz4 = pygame.transform.scale(yildiz, (30, 30))
    yildiz5 = pygame.transform.scale(yildiz, (30, 30))
    yildiz6 = pygame.transform.scale(yildiz, (30, 30))
    yildiz7 = pygame.transform.scale(yildiz, (30, 30))
    yildiz8 = pygame.transform.scale(yildiz, (30, 30))
    elmas = pygame.transform.scale(elmas, (30, 30))

    carpi=pygame.image.load("carpi.png")
    carpi=pygame.transform.scale(carpi, (30, 30))
    asl_txt=random.choice(kolay)
    txt1 = font2.render(asl_txt, True, (139, 69 ,19))
    txt1x=380
    txt1y=535
    input_rect = pygame.Rect(txt1x-80,txt1y+23, 140, 32)
    puan=0
    puan1=font.render("Score: {}".format(str(puan)),True,(139 ,69 ,19))
    dogru=0
    hak=1
    sayac=0
    sinir=120
    sinir2=500
    sonZaman=0
    deneme=False
    deneme2=False
    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_RETURN:
                        if asl_txt == user_text:
                            txt1y-=55
                            deneme=True
                            dogru +=1

                            if dogru == 1:
                                yildiz1.fill((152,245,255))
                            elif dogru == 2:
                                yildiz2.fill((152,245,255))
                            elif dogru == 3:
                                yildiz3.fill((152,245,255))
                            elif dogru == 4:
                                yildiz4.fill((152,245,255))
                            elif dogru == 5:
                                yildiz5.fill((152,245,255))
                            elif dogru == 6:
                                yildiz6.fill((152,245,255))
                            elif dogru == 7:
                                yildiz7.fill((152,245,255))
                            elif dogru == 8:
                                yildiz8.fill((152,245,255))
                            elif dogru == 9:
                                elmas.fill((152,245,255))
                                puan += 1000

                            input_rect = pygame.Rect(txt1x - 80, txt1y + 20, 140, 32)
                            puan +=10
                            asl_txt = random.choice(kolay)
                            txt1 = font2.render(asl_txt, True, (139, 69 ,19))
                            puan1 = font.render("Score: {}".format(str(puan)), True, (139, 69 ,19))
                            user_text=""
                        else:
                            dogru -=1
                            hak -=1
                            deneme2=True

                            if hak == 0:
                                can5=carpi
                            puan1 = font.render("Score: {}".format(str(puan)), True, (139, 69 ,19))
                            if bally<500:
                                txt1y += 55

                                input_rect = pygame.Rect(txt1x - 80, txt1y + 30, 140, 32)
                                asl_txt = random.choice(kolay)
                                txt1 = font2.render(asl_txt, True, (139, 69 ,19))
                                user_text = ""
                            else:
                                user_text = ""
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        timer -= dt
        if timer <= 0:
            res()
            done=True

        screen.fill((152,245,255))
        if active:
            color = color_active
        else:
            color = color_passive


        screen.blit(yildiz1, (185, 500))
        screen.blit(yildiz2, (55, 440))
        screen.blit(yildiz3, (185, 380))
        screen.blit(yildiz4, (55, 320))
        screen.blit(yildiz5, (185, 260))
        screen.blit(yildiz6, (55, 200))
        screen.blit(yildiz7, (185, 140))
        screen.blit(yildiz8, (55, 80))
        screen.blit(elmas, (185, 20))
        screen.blit(ball, (ballx, bally))
        simdikiZaman=pygame.time.get_ticks()
        if simdikiZaman-sonZaman > 550:
            sonZaman=simdikiZaman
            screen.blit(ball2, (ballx, bally))

        if deneme:
            if sayac <= 12:
                bally-=5
                if ballx < sinir:
                    ballx += 10.83
                else:
                    ballx -= 10.83
                    sinir-=10.83
                sayac +=1
                if sayac ==12:
                    sayac=0
                    sinir=120
                    deneme=False

            else:
                deneme=False
                sayac=0
        if deneme2:
            if sayac <= 12:
                if bally<sinir2:
                    bally+=5
                    sinir2+=5
                    if ballx < sinir:
                        ballx += 10.83
                    else:
                        ballx -= 10.83
                        sinir-=10.83

                sayac +=1
                if sayac ==12:
                    sayac=0
                    sinir=120
                    sinir2=500
                    deneme2=False

            else:
                deneme=False
                sayac=0



        screen.blit(can5, (0, 0))

        txt = font.render(str(round(timer, 2)), True, (139 ,69 ,19))
        screen.blit(txt, (530, 10))
        screen.blit(puan1,(0,30))
        screen.blit(txt1, (txt1x,txt1y))
        pygame.draw.rect(screen, color, input_rect, 2)
        text_surface = font.render(user_text, 1, (54, 54 ,54))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        all_sprite.draw(screen)
        if puan>1000 or hak ==0:
            res()
            done = True
        input_rect.w = max(250, text_surface.get_width() + 10)


        pygame.display.flip()
        dt = clock.tick(30) / 1000