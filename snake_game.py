import random
import pygame
from pygame.locals import *

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600

# Création de la fenêtre de jeu
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Couleurs
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)  # Couleur du serpent
RED = (255, 0, 0)    # Couleur de la nourriture

# Définir la vitesse du serpent
SNAKE_SPEED = 15

# Initialisation de la position du serpent
snake = [(100, 50), (90, 50), (80, 50)]

# Initialisation de la direction initiale du serpent
direction = "RIGHT"

# Initialisation de la nourriture
food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]

# Initialisation du score
score = 0

# Fonction pour afficher le serpent et la nourriture
def draw_snake(snake, screen):
    for pos in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

def draw_food(food, screen):
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], 10, 10))

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if direction != "DOWN":
                    direction = "UP"
            if event.key == K_DOWN:
                if direction != "UP":
                    direction = "DOWN"
            if event.key == K_LEFT:
                if direction != "RIGHT":
                    direction = "LEFT"
            if event.key == K_RIGHT:
                if direction != "LEFT":
                    direction = "RIGHT"

    if direction == "UP":
        new_head = (snake[0][0], snake[0][1] - 10)
    if direction == "DOWN":
        new_head = (snake[0][0], snake[0][1] + 10)
    if direction == "LEFT":
        new_head = (snake[0][0] - 10, snake[0][1])
    if direction == "RIGHT":
        new_head = (snake[0][0] + 10, snake[0][1])

    # Gestion de la collision avec la nourriture
    if new_head[0] == food_pos[0] and new_head[1] == food_pos[1]:
        score += 1
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        snake.insert(0, new_head)
    else:
        snake.insert(0, new_head)
        snake.pop()

    # Gestion de la collision avec les bords de l'écran
    if (
        snake[0][0] >= WIDTH
        or snake[0][0] < 0
        or snake[0][1] >= HEIGHT
        or snake[0][1] < 0
    ):
        running = False

    # Gestion de la collision avec le corps du serpent
    for block in snake[1:]:
        if snake[0] == block:
            running = False

    # Mettre à jour l'écran
    screen.fill(BLACK)
    draw_snake(snake, screen)
    draw_food(food_pos, screen)
    pygame.display.update()

    # Contrôler la vitesse du jeu
    pygame.time.Clock().tick(SNAKE_SPEED)

pygame.quit()
