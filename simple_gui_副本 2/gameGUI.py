import pygame
import sys
import time

# Initialize Pygame
def play():
    pygame.init()

    # Define colors
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BG_COLOR = (0,0,0)
    YELLOW = (255, 205, 67)
    WHITE = (255, 255, 255)

    # Initialize Pygame window
    width, height = 800, 600

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Paint Battle")
    clock = pygame.time.Clock()

    # Initialize game variables
    x1, y1 = width // 4, height // 2
    x2, y2 = width * 3 // 4, height // 2
    game_start = 0
    game_started = False

    # Number countdown animation variables
    countdown_start = 5
    countdown_timer = pygame.time.get_ticks()
    countdown_text = str(countdown_start)

    # Initialize ball variables
    ball1_trace = []
    ball2_trace = []
    ball1_color = RED
    ball2_color = BLUE
    ball1_size = 50
    ball2_size = 50

    # Game duration in seconds
    game_duration = 20
    game_end_time = 0

    # Game loop
    running = True
    screen.fill(BG_COLOR)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        

        if not game_started:
            font = pygame.font.SysFont(None, 80)
            text = font.render("CLICK TO START", True, YELLOW)
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

            if pygame.mouse.get_pressed()[0]:
                game_started = True
                pygame.draw.rect(screen, BLACK, (width // 2 - 400, height // 2 - 400, 800, 800))
                game_start = pygame.time.get_ticks()
                game_end_time = game_start + game_duration * 1000  # Convert to milliseconds

        if game_started:
            current_time = (pygame.time.get_ticks() - game_start) / 1000

            if current_time <= game_duration:
                keys = pygame.key.get_pressed()

                # Player 1 controls (Red)
                if keys[pygame.K_LEFT]:
                    x1 -= 5
                    x1 %= 800
                if keys[pygame.K_RIGHT]:
                    x1 += 5
                    x1 %= 800
                if keys[pygame.K_UP]:
                    y1 -= 5
                    y1 %= 600
                if keys[pygame.K_DOWN]:
                    y1 += 5
                    y1 %= 600



                # Player 2 controls (Blue)
                if keys[pygame.K_a]:
                    x2 -= 5
                    x2 %= 800
                if keys[pygame.K_d]:
                    x2 += 5
                    x2 %= 800
                if keys[pygame.K_w]:
                    y2 -= 5
                    y2 %= 600
                if keys[pygame.K_s]:
                    y2 += 5
                    y2 %= 600


                # Add ball positions to traces with respective colors and timestamps
                ball1_trace.append((x1, y1, RED, pygame.time.get_ticks()))
                ball2_trace.append((x2, y2, BLUE, pygame.time.get_ticks()))

                # Draw ball traces with colors
                all_traces = sorted(ball1_trace + ball2_trace, key=lambda x: x[3])
                for pos in all_traces:
                    pygame.draw.circle(screen, pos[2], (pos[0], pos[1]), ball1_size if pos[2] == RED else ball2_size)
                
            else:
                time.sleep(10)
                # Display final scene
                pygame.draw.rect(screen, BLACK, (width // 2 - 325, height // 2 - 125, 650, 250))
                font = pygame.font.SysFont(None, 50)

                # Calculate total painted area for each player
                screen_surface = pygame.surfarray.array3d(screen)
                total_area_player1 = 0
                total_area_player2 = 0
                c = 0
                for i in screen_surface:
                    c += 1
                    if c % 10 == 0:
                        for pixel in i:
                            if (pixel == RED).all():
                                total_area_player1 += 1
                            elif (pixel == BLUE).all():
                                total_area_player2 += 1
                # total_area_player1 = sum([ball1_size ** 2 for _ in ball1_trace])
                # total_area_player2 = sum([ball2_size ** 2 for _ in ball2_trace])

                # Determine the winner based on the total painted area
                
                red_ratio = int(total_area_player1*100/(total_area_player1 + total_area_player2))
                blue_ratio = 100 - red_ratio
                winner = "Player 1 (Red)" if total_area_player1 > total_area_player2 else "Player 2 (Blue)" if total_area_player1 < total_area_player2 else "It's a tie!"
                text = font.render(f"Winner: {winner}  {red_ratio}:{blue_ratio}", True, WHITE)
                screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
                pygame.display.flip()

                # Wait for a few seconds before quitting
                pygame.time.delay(5000)
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()



play()