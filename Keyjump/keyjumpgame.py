import random
import pygame
from Keyjump.episodes import *



def main():
    class Player(pygame.sprite.Sprite):
        def __init__(self,surx,sury):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("katman3.png")
            self.image = pygame.transform.scale(self.image, (120, 20))
            self.rect = self.image.get_rect()
            self.rect.center = (surx, sury)

    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((600, 600))

    font = pygame.font.Font(None, 120)
    font2 = pygame.font.Font(None, 60)
    font3= pygame.font.Font(None, 40)

    txt=font.render("Welcome!",1,(139 ,69 ,19))
    txt1=font2.render("Please write",1,(139 ,69 ,19))
    txt2 = font2.render("the hardness", 1, (139, 69, 19))
    txt3 = font3.render("Easy", 1, ("pink"))
    txt4 = font3.render("Medium", 1, ("red"))
    txt5 = font3.render("Hard", 1, (0,0,0))

    user_text = ""
    input_rect = pygame.Rect(360, 360, 140, 32)
    color_active = pygame.Color("lightskyblue3")
    color_passive = pygame.Color("gray15")

    all_sprite = pygame.sprite.Group()
    player6 = Player(200, 60)
    player7 = Player(70, 120)
    player8 = Player(200, 180)
    player9 = Player(70, 240)
    player10 = Player(200, 300)
    player11 = Player(70, 360)
    player12 = Player(200, 420)
    player13 = Player(70, 480)
    player14 = Player(200, 540)
    player15 = Player(70, 600)

    all_sprite.add(player7, player8, player9, player10, player11, player12,
                   player13, player14, player15)
    color = color_passive
    active = False
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
                        if user_text.lower() == "easy":
                            easy()
                            user_text=""
                        if user_text.lower() == "medium":
                            medium()
                            user_text=""
                        if user_text.lower() == "hard":
                            hard()
                            user_text=""
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
        screen.fill((152,245,255))

        if active:
            color = color_active
        else:
            color = color_passive

        screen.blit(txt,(120,0))
        screen.blit(txt1, (300, 200))
        screen.blit(txt2, (300, 260))
        screen.blit(txt3, (300, 320))
        screen.blit(txt4, (380, 320))
        screen.blit(txt5, (500, 320))
        pygame.draw.rect(screen, color, input_rect, 2)
        text_surface = font3.render(user_text, 1, (54, 54 ,54))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        all_sprite.draw(screen)

        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
    pygame.quit()