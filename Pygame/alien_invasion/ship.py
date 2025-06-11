import pygame

class Ship:
    """ Classe para cuidar da aeronave """

    def __init__(self, ai_game):
        """ Inicializa a aeronave e define sua posição inicial. """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect() 

        # Sobe a imagem da aeronave e obtém seu retângulo
        self.image = pygame.image.load('imagens/ship.bmp')
        self.rect = self.image.get_rect()

        # Começa cada espaçonave nova no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ Desenha a aeronave na sua posição atual. """
        self.screen.blit(self.image, self.rect)