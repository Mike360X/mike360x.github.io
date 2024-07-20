import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Defender-like Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player
player_width = 50
player_height = 30
player_x = 50
player_y = HEIGHT // 2
player_speed = 5

# Enemy
enemy_width = 40
enemy_height = 40
enemies = []
enemy_speed = 2

# Bullet
bullet_width = 5
bullet_height = 5
bullets = []
bullet_speed = 10

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + player_width, player_y + player_height // 2])

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_height:
        player_y += player_speed

    # Move bullets
    for bullet in bullets:
        bullet[0] += bullet_speed
        if bullet[0] > WIDTH:
            bullets.remove(bullet)

    # Spawn enemies
    if random.randint(1, 60) == 1:
        enemies.append([WIDTH, random.randint(0, HEIGHT - enemy_height)])

    # Move enemies
    for enemy in enemies:
        enemy[0] -= enemy_speed
        if enemy[0] < 0:
            enemies.remove(enemy)

    # Check for collisions
    for enemy in enemies:
        for bullet in bullets:
            if (enemy[0] < bullet[0] < enemy[0] + enemy_width and
                enemy[1] < bullet[1] < enemy[1] + enemy_height):
                enemies.remove(enemy)
                bullets.remove(bullet)
                break

    # Draw everything
    window.fill((0, 0, 0))
    pygame.draw.rect(window, GREEN, (player_x, player_y, player_width, player_height))
    for enemy in enemies:
        pygame.draw.rect(window, RED, (enemy[0], enemy[1], enemy_width, enemy_height))
    for bullet in bullets:
        pygame.draw.rect(window, WHITE, (bullet[0], bullet[1], bullet_width, bullet_height))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
