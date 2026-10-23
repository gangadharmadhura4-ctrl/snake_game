
import pygame

pygame.init()

# Create the window
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Tic Tac Toe")

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# Board positions
a = ""
b = ""
c = ""
d = ""
e = ""
f = ""
g = ""
h = ""
i = ""

# Current player
player = "X"

running = True
game_over = False
win_line = None
winner = ""

while running:

    screen.fill(white)

    # Draw the board
    pygame.draw.line(screen, black, (133, 0), (133, 400), 3)
    pygame.draw.line(screen, black, (266, 0), (266, 400), 3)
    pygame.draw.line(screen, black, (0, 133), (400, 133), 3)
    pygame.draw.line(screen, black, (0, 266), (400, 266), 3)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = event.pos

            # First row
            if y < 133 and x < 133 and a == "":
                a = player
            elif y < 133 and x < 266 and x >= 133 and b == "":
                b = player
            elif y < 133 and x >= 266 and c == "":
                c = player

            # Second row
            elif y >= 133 and y < 266 and x < 133 and d == "":
                d = player
            elif y >= 133 and y < 266 and x >= 133 and x < 266 and e == "":
                e = player
            elif y >= 133 and y < 266 and x >= 266 and f == "":
                f = player

            # Third row
            elif y >= 266 and x < 133 and g == "":
                g = player
            elif y >= 266 and x >= 133 and x < 266 and h == "":
                h = player
            elif y >= 266 and x >= 266 and i == "":
                i = player

            else:
                continue

            # Check winning combinations
            if a != "" and a == b and b == c:
                win_line = ((20, 66), (380, 66))

            elif d != "" and d == e and e == f:
                win_line = ((20, 200), (380, 200))

            elif g != "" and g == h and h == i:
                win_line = ((20, 333), (380, 333))

            elif a != "" and a == d and d == g:
                win_line = ((66, 20), (66, 380))

            elif b != "" and b == e and e == h:
                win_line = ((200, 20), (200, 380))

            elif c != "" and c == f and f == i:
                win_line = ((333, 20), (333, 380))

            elif a != "" and a == e and e == i:
                win_line = ((30, 30), (370, 370))

            elif c != "" and c == e and e == g:
                win_line = ((370, 30), (30, 370))

            # ALWAYS alternate after a valid move
            if player == "X":
                player = "O"
            else:
                player = "X"


    # Display the marks
    font = pygame.font.SysFont(None, 100)

    text_a = font.render(a, True, blue)
    text_b = font.render(b, True, red)
    text_c = font.render(c, True, blue)
    text_d = font.render(d, True, red)
    text_e = font.render(e, True, blue)
    text_f = font.render(f, True, red)
    text_g = font.render(g, True, blue)
    text_h = font.render(h, True, red)
    text_i = font.render(i, True, blue)

    screen.blit(text_a, (45, 20))
    screen.blit(text_b, (178, 20))
    screen.blit(text_c, (310, 20))

    screen.blit(text_d, (45, 153))
    screen.blit(text_e, (178, 153))
    screen.blit(text_f, (310, 153))

    screen.blit(text_g, (45, 286))
    screen.blit(text_h, (178, 286))
    screen.blit(text_i, (310, 286))

        # Draw the winning line
    if win_line != None:
        pygame.draw.line(screen, red, win_line[0], win_line[1], 5)
    pygame.display.update()

pygame.quit()
