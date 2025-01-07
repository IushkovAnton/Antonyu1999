import pygame
import sys
from button import ImageButton

# Инициализация
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 600, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")

# Создание кнопки
blue_button = ImageButton(WIDTH / 2 - (252 / 2), 100, 252, 74, "", "blue.jpg", "red.jpg")


def main_menu():
    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        blue_button.draw(screen)
        pygame.display.flip()


main_menu()