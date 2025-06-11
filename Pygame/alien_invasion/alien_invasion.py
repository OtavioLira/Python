import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Classe geral para gerenciar ativos e comportamento do jogo. """

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
    
    def run_game(self):
        """ Inicia o loop principal do jogo. """
        while True:
            self._check_events()
            self._update_screen()
        
            # Deixa a tela desenhada mais recente visível
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        # Observa eventos de teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """ Atualiza as imagens na tela e mude para a nova tela. """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        pygame.display.flip()
        
if __name__ == '__main__':
    # Cria uma instância do jogo e inicia o loop principal
    ai = AlienInvasion()
    ai.run_game()