import pygame as pg

Screen_Height = 1024
Screen_Width = 768

# setup da tela do jogo
screen = pg.display.set_mode((Screen_Height, Screen_Width))
pg.display.set_caption("test demo")

pg.font.init()
# fonte e tamanho
font = pg.font.SysFont('Courier New', 50, bold=True)

preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul_claro = (200, 200, 255)
azul = (100, 100, 255)
branco = (255, 255, 255)
azul_pastel = (52, 235, 235)
cor_fundo = (202, 228, 241)

# classe botao
class Button():
    # botao restart
    def __init__(self, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def draw(self):
        # desenhar botao na tela
        screen.blit(self.image, (self.rect.x, self.rect.y))

# game loop
run = True
while run:
    
    # event handler
    for event in pg.event.get():
        # quit game
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
    
pg.quit()




