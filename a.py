import pygame

FPS = 60
size = width, height = [200, 200]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.font.init()

font_size = 100000
font = pygame.font.SysFont("Arial", font_size)

def draw(n):
    screen.fill(pygame.Color("black"))
    txt_surface = font.render(str(n), True, pygame.Color("red"))
    screen.blit(txt_surface, ((width - txt_surface.get_width()) // 2,
                               (height - txt_surface.txt_surface.get_height()) // 2))

hide_count = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEOEXPOSE:
            hide_count += 1

    draw(hide_count)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()