import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 300
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dinosaur Game - VS Code Version")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Dino settings
dino_width, dino_height = 40, 50
dino_x = 50
dino_y = HEIGHT - dino_height - 30
dino_y_velocity = 0
gravity = 1
is_jumping = False

# Obstacle settings
obstacles = []
obstacle_width = 20
obstacle_height = 50
obstacle_speed = 8

# Score
score = 0
font = pygame.font.SysFont(None, 36)


def draw_dino(x, y):
    pygame.draw.rect(SCREEN, BLACK, (x, y, dino_width, dino_height))


def draw_obstacles(obs_list):
    for obs in obs_list:
        pygame.draw.rect(SCREEN, BLACK, obs)


def main():
    global dino_y, dino_y_velocity, is_jumping, score, obstacles

    running = True
    spawn_timer = 0

    while running:
        clock.tick(60)
        SCREEN.fill(WHITE)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Jump with SPACE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jumping:
                    dino_y_velocity = -18
                    is_jumping = True

        # Dino movement (gravity)
        dino_y += dino_y_velocity
        dino_y_velocity += gravity

        if dino_y >= HEIGHT - dino_height - 30:
            dino_y = HEIGHT - dino_height - 30
            is_jumping = False

        # Spawn obstacles
        spawn_timer += 1
        if spawn_timer > 90:
            obstacles.append(
                pygame.Rect(WIDTH, HEIGHT - obstacle_height - 30,
                            obstacle_width, obstacle_height)
            )
            spawn_timer = 0

        # Move obstacles
        for obs in obstacles:
            obs.x -= obstacle_speed

        # Remove off-screen obstacles
        obstacles = [obs for obs in obstacles if obs.x > -20]

        # Collision detection
        dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)
        for obs in obstacles:
            if dino_rect.colliderect(obs):
                print("GAME OVER! Final Score:", score)
                pygame.quit()
                sys.exit()

        # Score update
        score += 1
        score_text = font.render(f"Score: {score}", True, BLACK)
        SCREEN.blit(score_text, (10, 10))

        # Draw everything
        draw_dino(dino_x, dino_y)
        draw_obstacles(obstacles)

        pygame.display.update()


if __name__ == "__main__":
    main()