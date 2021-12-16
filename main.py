import pygame

pygame.init()
pygame.display.set_caption("Кирпичи")
n = int(input())
h = 1000
w = 1000
screen = pygame.display.set_mode((w, h))
screen.fill((255, 255, 255))
color = pygame.Color("orange")
a = 150 // n
for i in range(h // n):
    for j in range(w // n):
        pygame.draw.polygon(screen, color, [(j * n, i * n + n / 2),
                                            (j * n + n / 2, i * n),
                                            ((j + 1) * n, i * n + n / 2),
                                            (j * n + n / 2, (i + 1) * n)], 0)
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass