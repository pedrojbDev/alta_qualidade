import pygame
from pygame.sprite import Sprite

# Nesse momento é utilizado o conceito de HERANÇA de Orientação a Objetos, onde a classe Bullet herda os atributos e métodos da classe Sprite, que é uma classe do Pygame usada para representar objetos visuais no jogo.
 # A classe Bullet é responsável por gerenciar os projéteis disparados pela nave, incluindo sua posição, movimento e aparência.
class Bullet(Sprite):
    """Gerencia os projéteis disparados pela nave."""

    def __init__(self, alien_invasion_screen, alien_invasion_settings, alien_invasion_ship):
        """Cria um objeto para o projétil na posição atual da nave."""
        super().__init__() # Chama o construtor da classe Sprite para garantir que a classe Bullet seja inicializada corretamente como um sprite do Pygame
        self.screen = alien_invasion_screen
        self.settings = alien_invasion_settings
        self.ship = alien_invasion_ship
        self.color = self.settings.bullet_color
        # Cria um rect para o projétil em (0, 0) e depois define a posição correta
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = self.ship.rect.midtop # Posiciona o projétil na parte superior da nave
        self.y = float(self.rect.y) # Armazena a posição vertical do projétil como um número de ponto flutuante para permitir movimentos suaves
        
    def update(self):
        """Move o projétil para cima na tela."""
        self.y -= self.settings.bullet_speed # Move o projétil para cima diminuindo a coordenada y
        self.rect.y = self.y # Atualiza a posição do rect do projétil com base na nova coordenada y
        
        
    def draw_bullet(self):
        """Desenha o projétil na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect) # Desenha um retângulo representando o projétil na tela usando as coordenadas do rect