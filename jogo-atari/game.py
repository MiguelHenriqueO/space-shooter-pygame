import pygame
import sys
from settings import *
from sprites import Player, Asteroid

def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("arial", size, bold=True)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jogo Atari")
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    player = Player(all_sprites, bullets)
    all_sprites.add(player)

    # Evento customizado para spawn de asteroides
    SPAWNASTEROID = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWNASTEROID, ASTEROID_SPAWN_RATE)

    score = 0
    running = True
    game_over = False

    while running:
        clock.tick(FPS)

        # 1. Tratamento de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.shoot()
                
                if event.type == SPAWNASTEROID:
                    asteroid = Asteroid()
                    all_sprites.add(asteroid)
                    asteroids.add(asteroid)
            else:
                # Reiniciar o jogo com a tecla R
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    main()
                    return

        if not game_over:
            # 2. Atualização dos sprites
            all_sprites.update()

            # Checar colisões de balas em asteroides
            hits = pygame.sprite.groupcollide(asteroids, bullets, True, True)
            for hit in hits:
                score += 10

            # Checar colisões de jogador em asteroides
            hits = pygame.sprite.spritecollide(player, asteroids, False)
            if hits:
                game_over = True

            # Checar se asteroide passou do fundo da tela
            for asteroid in asteroids:
                if asteroid.rect.top > HEIGHT:
                    game_over = True
                    break

        # 3. Renderização
        screen.fill(BLACK)
        all_sprites.draw(screen)
        
        draw_text(screen, f"Score: {score}", 30, 10, 10)
        
        if game_over:
            draw_text(screen, "GAME OVER", 64, WIDTH//2 - 160, HEIGHT//2 - 50)
            draw_text(screen, "Pressione 'R' para reiniciar", 22, WIDTH//2 - 130, HEIGHT//2 + 20)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
