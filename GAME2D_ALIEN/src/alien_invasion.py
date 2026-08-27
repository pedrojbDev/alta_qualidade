import sys

import pygame
from alien import Alien
from bullet import Bullet
from settings import Settings
from ship import Ship


class GameEventHandler:
    """Responsável apenas por ler e tratar os eventos do teclado/janela."""

    def __init__(self, ship, bullet_manager) -> None:
        self.ship = ship
        self.bullet_manager = bullet_manager

    def _check_events(self) -> None:
        """Responde a eventos de pressionamento de teclas e mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)

    def _handle_keydown(self, event: pygame.event.Event) -> None:
        """Responde a eventos de pressionamento de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.bullet_manager._fire_bullet()

    def _handle_keyup(self, event: pygame.event.Event) -> None:
        """Responde a eventos de soltura de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


class BulletManager:
    """Responsável apenas por criar, atualizar e desenhar os projéteis."""

    def __init__(self, screen, settings, ship) -> None:
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.bullets = pygame.sprite.Group()

    def _fire_bullet(self) -> None:
        """Dispara um projétil se o limite ainda não tiver sido alcançado."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self.screen, self.settings, self.ship)
            self.bullets.add(new_bullet)

    def _update_bullets(self, aliens) -> None:
        """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""
        self.bullets.update()
        self._remove_offscreen_bullets()
        self._check_bullet_alien_collisions(aliens)

    def _remove_offscreen_bullets(self) -> None:
        """Remove os projéteis que desapareceram da tela."""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collisions(self, aliens) -> None:
        """Verifica colisões entre projéteis e alienígenas."""
        pygame.sprite.groupcollide(self.bullets, aliens, True, True)


class FleetManager:
    """Responsável por criar e gerenciar a frota de alienígenas."""

    def __init__(self, screen, settings, ship) -> None:
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.aliens = pygame.sprite.Group()

    def create_fleet(self) -> None:
        """Cria uma frota de alienígenas."""
        alien = Alien(self.screen, self.settings)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                alien = Alien(self.screen, self.settings)
                alien.x = alien_width + 2 * alien_width * alien_number
                alien.rect.x = alien.x
                alien.y = alien_height + 2 * alien_height * row_number
                alien.rect.y = alien.y
                self.aliens.add(alien)

    def _update_aliens(self) -> None:
        """Verifica se a frota está em uma borda e atualiza suas posições."""
        self._check_fleet_edges()
        self.aliens.update()
        self._check_ship_collision()

    def _check_fleet_edges(self) -> None:
        """Responde apropriadamente se algum alienígena tiver alcançado uma borda."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self) -> None:
        """Desce a frota e muda sua direção."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_ship_collision(self) -> None:
        """Verifica se a nave colidiu com algum alienígena."""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("A nave foi atingida!")
            sys.exit()


class GameRenderer:
    """Responsável apenas por desenhar os elementos do jogo na tela."""

    def __init__(self, screen, bg_color, ship, bullets, aliens) -> None:
        self.screen = screen
        self.bg_color = bg_color
        self.ship = ship
        self.bullets = bullets
        self.aliens = aliens

    def _render_screen(self) -> None:
        """Redesenha a tela a cada passagem pelo laço."""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self._draw_bullets()
        pygame.display.flip()

    def _draw_bullets(self) -> None:
        """Desenha os projéteis na tela."""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()


class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""

    def __init__(self) -> None:
        """Inicializa o jogo e cria os recursos básicos."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self.screen, self.settings)
        self.bg_color = self.settings.bg_color
        self.bullet_manager = BulletManager(self.screen, self.settings, self.ship)
        self.fleet_manager = FleetManager(self.screen, self.settings, self.ship)
        self.event_handler = GameEventHandler(self.ship, self.bullet_manager)
        self.renderer = GameRenderer(
            self.screen,
            self.bg_color,
            self.ship,
            self.bullet_manager.bullets,
            self.fleet_manager.aliens,
        )

    def _update_game_state(self) -> None:
        """Atualiza a posição da nave, dos projéteis e dos alienígenas."""
        self.ship.update()
        self.bullet_manager._update_bullets(self.fleet_manager.aliens)
        self.fleet_manager._update_aliens()

    def run_game(self) -> None:
        """Cria um laço de repetição para manter a janela do jogo visível."""
        self.fleet_manager.create_fleet()

        while True:
            self.event_handler._check_events()
            self._update_game_state()
            self.renderer._render_screen()


if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
