import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Gerencia os alienígenas."""

    def __init__(self, alien_invasion_screen, alien_invasion_settings):
        """Inicializa o alienígena e define sua posição inicial."""
        super().__init__() # Chama o construtor da classe Sprite para garantir que a classe Alien seja inicializada corretamente como um sprite do Pygame
        self.screen = alien_invasion_screen
        self.settings = alien_invasion_settings
        
        # Carrega a imagem do alienígena e obtém seu rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Inicia cada novo alienígena próximo à parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x) # Armazena a posição horizontal do alienígena como um número de ponto flutuante para permitir movimentos suaves
        
    def drawme(self):
        """Desenha o alienígena em sua posição atual."""
        self.screen.blit(self.image, self.rect) # ('o que', 'onde')
        
    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction) # Move o alienígena para a direita ou esquerda com base na direção da frota
        self.rect.x = self.x # Atualiza a posição do rect do alienígena com base na nova coordenada x
        
    def check_edges(self):
        """Retorna True se o alienígena estiver na borda da tela."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True