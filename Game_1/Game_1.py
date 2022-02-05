import sys

import pygame

from settings import Settings
from star import Star

class STARS:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициалищирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode((800, 600))

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("GG")


        self.stars = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self._update_screen()
            self._update_stars()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_stars(self):
        """Обновляет позиции всех пришельцев во флоте"""
        self._check_fleet_edges()
        self.stars.update()

    def _create_fleet(self):
        """Создание флота вторжения."""
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2 * star_width)
        number_star_x = available_space_x // (2 * star_width)

        
        available_space_y = self.settings.screen_height \
                         - 3 * star_height
        number_rows = available_space_y // (2 * star_height)

        # Создание флота
        for row_number in range(number_rows):
            for star_number in range(number_star_x):
                self._create_star(star_number, row_number)

    def _create_alien(self, star_number, row_number):
        # Создание пришельца
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number 
        star.rect.x = star.x
        star.rect.y = star_height + 2 * star_height * row_number
        self.stars.add(star) 

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана"""
        for star in self.stars.sprites():
            if star.check_edges():
                break

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = STARS()
    ai.run_game()