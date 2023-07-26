import sys
from time import sleep
from pathlib import Path
import json

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """AlienInvasion is created for manage resources and action of the game"""
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        # Establish an instance for the storage of game statistical info
        self.stats = GameStats(self)
        # Create a scoreboard.
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # set background color
        self.bg_color = (self.settings.bg_color)

        # Turn to inactive status when the game start
        self.game_active = False

        # Create play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Main loop of game when it has began."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Responding to key and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type - pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start the game when a player click play button."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked:
            self._start_game()

    def _start_game(self):
        """Start game when the game is inactive."""
        if not self.game_active:
            # Reset game's dynamic settings
            self.settings.initailize_dynamic_settings()

            # Resetting the game's statistical information.
            self.stats.reset_stats()
            self.sb.prep_images()
            self.game_active = True

            # Empty aliens list and bullets list
            self.bullets.empty()
            self.aliens.empty()
            
            # Create a new fleet and place the ship at the center of the screen
            self._create_fleet()
            self.ship.center_ship()
            
            # Play BGM
            self.playBGM()

            # Hiding the cursor
            pygame.mouse.set_visible(False)
        

    def _check_keydown_events(self, event):
        """Response for keydown"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self._save_high_score()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()

    def _check_keyup_events(self, event):
        """Response for release"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a bullet and put it into bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Reposition new bullets and remove disappeared bullets"""
        # Reposition new bullets
        self.bullets.update()
        
        # Remove disappeared bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Check if any bullet have hit the alien.
        # If there is, then delete the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.start_new_level()

    def start_new_level(self):
        # Delete all bullets on the screen and create a new fleet
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        # Increase the level
        self.stats.level += 1
        self.sb.prep_level()
        
    def _update_aliens(self):
        """Check if there is any alien reach the edge and update the position of the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        # Inspecting the collision between aliens and the ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Check if there's any alien have reached the bottom of the screen
        self._check_aliens_bottom()

    def _create_fleet(self):
        """Create an alien fleet"""
        # Create an alien and continue incorporating it until
        # there is no more space to accommodate additional alien.
        # The aliens' distance is equal to the alien's width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # After append a line of alien, reset the value of x and increase the value of y
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and put in current line."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Take appropriate measure when fleet reach the border."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
                
    def _change_fleet_direction(self):
        """Move down the fleet and reverse their direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Response collision between aliens and the ship."""
        if self.stats.ships_left > 0:
            # Reduce the value of ship_left by 1.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Empty the list of aliens and the list of bullets
            self.bullets.empty()
            self.aliens.empty()
        
            # Create a new fleet and place the ship at the center bottom of the screen.
            self._create_fleet()
            self.ship.center_ship()
        
            # Pause
            sleep(1)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
        
    def _check_aliens_bottom(self):
        """Check if there is any alien have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Response like ship collision
                self._ship_hit()
                break

    def playBGM(self):
        pygame.mixer.init()
        pygame.mixer.music.load('./BGM/bgm.mp3')
        pygame.mixer.music.play(-1)

    def _save_high_score(self):
        path = Path(self.settings.path_of_high_score)
        contents = json.dumps(self.sb.stats.high_score)
        path.write_text(contents)

    def _read_high_score(self):
        path = Path(self.settings.path_of_high_score)
        contents = path.read_text()
        self.stats.high_score = int(contents)
        self.sb.prep_high_score()
    
    def _update_screen(self):
        """update images on the screen and swich to new screen"""
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Display score
        self.sb.show_score()

        # Draw a play button when game is inactive
        if not self.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip()
        
            
if __name__ == '__main__':
    # Create a instance of the game and run it.
    ai = AlienInvasion()
    ai._read_high_score()
    ai.run_game()    