import pygame

class Ship:
    """Gerencia a nave espacial."""

    def __init__(self, alien_invasion_screen, alien_invasion_settings):
        """Inicializa a nave e define sua posição inicial."""
        self.screen = alien_invasion_screen
        self.settings = alien_invasion_settings
        self.screen_rect = self.screen.get_rect() # Rect é uma estrutura usada para representar posições e áreas retangulares
        
        # Carrega a imagem da nave e obtém seu rect
        self.image = pygame.image.load('images/ship.bmp')
        # o pygame trata os elementos como retangulos, tornando seu processamento eficiente
        self.rect = self.image.get_rect()
        # Posiciona a nave no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom 
        
        self.moving_right = False # Variável de controle para o movimento da nave para a direita
        self.moving_left = False # Variável de controle para o movimento da nave para a esquerda
    
        self.x = float(self.rect.x) # Armazena a posição horizontal da nave como um número de ponto flutuante para permitir movimentos suaves
        
    
    def blitme(self):
        """Desenha a nave em sua posição atual."""
        # o método blit desenha a imagem da nave na tela usando as coordenadas do rect
        self.screen.blit(self.image, self.rect) # ('o que', 'onde')
        
    
    def update(self):
        """Atualiza a posição da nave com base na variável de controle."""
        if self.moving_right and self.rect.right < self.screen_rect.right: # Verifica se a nave pode se mover para a direita sem sair da tela
            self.x += self.settings.ship_speed # Move a nave para a direita aumentando a coordenada x
            
        if self.moving_left and self.rect.left > 0: # Verifica se a nave pode se mover para a esquerda sem sair da tela
            self.x -= self.settings.ship_speed # Move a nave para a esquerda diminuindo a coordenada x
            
        # Atualiza o rect object da nave
        self.rect.x = self.x