from alien import Alien


class FastAlien(Alien):
    """Alienígena mais rápido."""

    def update(self) -> None:
        self.x += (
            self.settings.alien_speed * 2
        ) * self.settings.fleet_direction
        self.rect.x = self.x
