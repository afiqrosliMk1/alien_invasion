import sys

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # FULLSCREEN #
        # # First we pass (0, 0) so pygame can figure out screen size that can fit fullscreen
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # # We update width and height after screen is created
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        # WINDOWED #
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion")


        # Set the background color.
        self.bg_color = self.settings.bg_color

        # Create ship
        self.ship = Ship(self)

        # Create group that holds the bullet
        self.bullets = pygame.sprite.Group()

        # Create group that holds the aliens
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()

            # Update ship position
            self.ship.update()

            # Update bullets
            self._update_bullets()

            # Make the most recently drawn screen visible.
            self._update_screen()

            self.clock.tick(60)

    def _check_events(self):
        """Watch for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            # Move ship to the right. ship.rect is the variable that stores rect object returned by .get_rect(). It is also passed to blitme to as coordinate. 
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        else:
            pass

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # Update bullet position
        self.bullets.update()

        # Remove bullet that disappeared from memory
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets))

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Make an alien - alternative
        # for i in range(int(self.screen.get_width() // 2)):
        #     alien = Alien(self)
        #     alien.rect.x *= i*2
        
        #     self.aliens.add(alien)

        # Create an alien an keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width.
        alien = Alien(self)
        alien_width = alien.rect.width

        current_x = alien_width
        while current_x < (self.settings.screen_width - 2 * alien_width):
            self._create_alien(current_x)
            current_x += 2 * alien_width

    def _create_alien(self, x_position):
        """Create one alien"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.bg_color)

        # Blit bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Blit ship
        self.ship.blitme()

        # Blit fleet of alien
        self.aliens.draw(self.screen)

        pygame.display.flip()
            

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()



