import sys
import pygame

pygame.font.init()


def create_alien(ai_settings, Alien):
    """Create new alien if MAX_ALIENS hasn't been reached."""
    if Alien.current_alien_count != ai_settings.MAX_ALIENS:
        Alien()
        # I'll admit it might not be optimal to handle the Alien classes variables externally
        # but for this purpose it works.
        Alien.current_alien_count += 1


def handle_firing(ship, Bitcoin, SuperBitcoin):
    # If the ship is firing spawn the type of bitcoin requested.
    (is_firing, shot_type) = ship.shoot()
    if is_firing:
        if shot_type == "bitcoin":
            Bitcoin(ship.gunpos())
            ship.firing = False
            ship.bitcoin_mining = 0
        elif shot_type == "super_bitcoin":
            SuperBitcoin(ship.gunpos())
            ship.firing = False
            ship.bitcoin_mining = 0


def check_collisions(ship, aliens, bitcoins, super_bitcoins, Alien, ai_settings):
    # Check if ship has collided with an alien
    for alien in pygame.sprite.spritecollide(ship, aliens, True):
        # Check that mixer is loaded
        if pygame.mixer:
            ai_settings.boom_sound.play()
        ship.damage += 10
        Alien.current_alien_count -= 1

    # Check if normal bitcoin has collided with an alien
    for bitcoin in pygame.sprite.groupcollide(bitcoins, aliens, True, True):
        if pygame.mixer:
            ai_settings.boom_sound.play()
        ai_settings.score += 10
        Alien.current_alien_count -= 1

    # Check if super bitcoin has collided with an alien
    for super_bitcoin_lst in pygame.sprite.groupcollide(
        aliens, super_bitcoins, True, False
    ).values():
        if pygame.mixer:
            ai_settings.boom_sound.play()
        ai_settings.score += 10
        Alien.current_alien_count -= 1
        # groupcollide() returns a dictionary where each item is an alien associated with a list of super_bitcoins it has collided with
        for super_bitcoin in super_bitcoin_lst:
            super_bitcoin.calc_new_vector()


def check_events(screen, ship, sprites):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move ship right.
                ship.right()
            elif event.key == pygame.K_LEFT:
                # Move ship left.
                ship.left()
            elif event.key == pygame.K_q:
                # Move ship up.
                ship.up()
            elif event.key == pygame.K_a:
                # Move ship down.
                ship.down()
            # ANY OTHER KEY OPTIONS GO HERE
            elif event.key == pygame.K_SPACE:
                # Verify bitcoin_mining is at 100 and set firing status of the ship to true.
                if ship.bitcoin_mining == 100:
                    ship.firing = True
                    ship.shoot()


def update_screen(sprites, ai_settings, screen, ship, dashboard, text):
    """Update sprites & messages on the screen."""

    # Update the instrument readings

    # CODE GOES HERE

    # Set each dasboard component's value individually.
    # Note that you have to be aware in which order the variables are
    # provided within the tuple.
    dashboard[0].value = ship.damage
    dashboard[1].value = ai_settings.lives
    dashboard[2].value = ai_settings.score
    dashboard[3].value = ship.bitcoin_mining

    # If damage reaches 100%, display CRASHED message

    # CODE GOES HERE

    # # Update sprites one last time. Mainly necessary to for dashboard values to be displayed correctly.
    if ship.damage == 100:
        sprites.update()

    # Clear old sprites
    sprites.clear(screen, ai_settings.screen_backgrnd)

    # Draw sprites and return changed sprites (since we're using RenderUpdates group)
    rects = sprites.draw(screen)

    # Update the background region.
    pygame.display.update(rects)

    # There are two checks because sprites.update() needs to occur
    # the last time before pygame.display.update(rects) but the text needs to be printed
    # on top of everything hence it has to be last.
    if ship.damage == 100:
        screen.blit(text[0], text[1])
        pygame.display.flip()
