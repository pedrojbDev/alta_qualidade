class Settings:
    """Classe que armazena todas as configurações do jogo."""
    
    def __init__(self):
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # Cor de fundo (cinza claro)
        self.ship_speed = 1.5 # Velocidade da nave
        
        # Configurações dos projéteis
        self.bullet_speed = 1.0 # Velocidade dos projéteis
        self.bullet_width = 3 # Largura dos projéteis   
        self.bullet_height = 15 # Altura dos projéteis
        self.bullet_color = (60, 60, 60) # Cor dos projeteis
        self.bullet_allowed = 1 # Número máximo de projéteis que podem existir na tela ao mesmo tempo
        
        # Configurações do alien
        self.alien_speed = .3 # Velocidade dos alienígenas
        self.fleet_drop_speed = 10 # Velocidade com que a frota de alienígenas desce em direção à nave
        self.fleet_direction = 1 # Direção da frota de alienígenas: 1 representa a direita; -1 representa a esquerda

