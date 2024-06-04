import pygame

class FontRenderer:
    def __init__(self):
        #self.color = (255,255,0)
        self.color = (255,255,255)
        self.size = 100
        self.font = pygame.font.Font("fonts/mont.ttf",self.size)


    def renderFont(self,window,score):
        text = self.font.render("" + str(score),True,self.color)
        window.blit(text,(10,-15))