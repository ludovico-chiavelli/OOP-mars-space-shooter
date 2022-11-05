import pygame
import time
import sys

# COMPLETE FILE PROVIDED IN STARTER CODE
from settings import Settings

# PARTIAL FILE PROVIDED IN STARTER CODE
import game_functions as gf

# IMPORT OTHER FILES/CLASSES HERE AS REQUIRED
from ship import Ship
from aliens import Alien
from bitcoin import Bitcoin, SuperBitcoin
from value_tracker import ValueTracker


def run_game():
    # Initialize pygame, settings and screen object.
    pygame.init()

    # Set keys to repeat if held down.
    pygame.key.set_repeat(5, 5)

    # Create settings object containing game settings.
    ai_settings = Settings()

    # Create the main game screen.
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )

    # Create a main window caption.
    pygame.display.set_caption("Space Z - Mars Flight")

    # Create clock object
    clock = pygame.time.Clock()

    while ai_settings.lives > 0:

        # ** CODE TO CREATE SPRITES/GROUPS GOES HERE **

        # Assign default groups for each class. Method taken from https://github.com/pygame/pygame/blob/main/examples/aliens.py line 287
        aliens = pygame.sprite.Group()
        bitcoins = pygame.sprite.Group()
        super_bitcoins = pygame.sprite.Group()
        sprites = pygame.sprite.RenderUpdates()

        ValueTracker.containers = sprites
        Ship.containers = sprites
        Alien.containers = aliens, sprites
        Bitcoin.containers = bitcoins, sprites
        SuperBitcoin.containers = super_bitcoins, sprites

        # Reset the screen by drawing the background over everything each time the player starts with a new life.
        # It's better to do it within this loop than outside (after the screen variables as in the starter code)
        # so it doesn't get repeated.
        screen.blit(ai_settings.screen_backgrnd, [0, 0])
        pygame.display.flip()

        # Initialize starting sprites
        ship = Ship()
        Alien()  # this is "alive" as it's in a sprite group https://github.com/pygame/pygame/blob/main/examples/aliens.py line 310

        # Reset values if we're at round 2 or more.
        if ai_settings.lives < 3:
            ai_settings.score = 0
            Alien.current_alien_count = 0

        # Starting dashboard values initialized with their position.
        damage = ValueTracker(120, 17)
        lives = ValueTracker(250, 17)
        score = ValueTracker(120, 44)
        bitcoin_mining = ValueTracker(335, 40)

        def text():
            """Initialize message for when ship crashes"""
            font = pygame.font.Font(None, 100)
            text = font.render("You Have Crashed!", True, pygame.Color("red"))
            textRect = text.get_rect()
            textRect.center = (
                ai_settings.screen_width // 2,
                ai_settings.screen_height // 2,
            )
            return (text, textRect)

        # Start the main loop for the game.
        while ship.damage < 100:
            # Make the loop run no faster than the set FPS
            clock.tick(ai_settings.FPS)

            # Watch for keyboard events.
            gf.check_events(screen, ship, sprites)
            # Tell all the sprites to update their status
            sprites.update()

            # ** ANY OTHER MAIN GAME CODE GOES HERE **

            gf.create_alien(ai_settings, Alien)

            gf.handle_firing(ship, Bitcoin, SuperBitcoin)

            gf.check_collisions(
                ship, aliens, bitcoins, super_bitcoins, Alien, ai_settings
            )

            # Now update the sprites, etc. on the screen
            gf.update_screen(
                sprites,
                ai_settings,
                screen,
                ship,
                (damage, lives, score, bitcoin_mining),
                text(),
            )

        # Remove a life
        ai_settings.lives -= 1

        # Wait for a moment before continuing so user can read the text.
        time.sleep(2)

        # Wait specifically for a keypress to continue. Modified, from https://stackoverflow.com/questions/20748326/pygame-waiting-the-user-to-keypress-a-key
        # I used this method instead of the pygame.event.wait because it would allow for mouse movements too, which I didn't think was correct. This way it's
        # limited to keypresses only to continue.
        pygame.event.clear()  # The event que may contain previous key presses hence you need to clear it.
        wait = True
        while wait:
            for event in pygame.event.get():
                # If the player quits the window or his lives are zero, close the program.
                if event.type == pygame.QUIT or ai_settings.lives == 0:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    wait = False

    # GAME ENDS
    pygame.quit()


# Call the main method to start the game
run_game()
