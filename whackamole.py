from random import randrange
import pygame


def main():
    try:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        pygame.init()
        clock = pygame.time.Clock()
        running = True

        randrow = 0
        randcol = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill("light green")

            for i in range(1, 21):
                pygame.draw.line(
                    screen,
                    'dark green',
                    (i * 32, 0),
                    (i * 32, 512),
                )

            for i in range(1, 17):
                pygame.draw.line(
                    screen,
                    'dark green',
                    (0, i * 32),
                    (640, i * 32),
                )

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = y // 32
                    col = x // 32
                    if row == randrow and col == randcol:
                        randrow = randrange(0, 17)
                        randcol = randrange(0, 21)

            screen.blit(mole_image, mole_image.get_rect(topleft=(randcol * 32, randrow * 32)))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
