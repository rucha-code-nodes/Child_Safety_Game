import pygame
import random
import math

def touch_balloon_popping_game():
    # Initialize pygame
    pygame.init()

    # Game Variables
    WIDTH, HEIGHT = 1100,650#800, 600
    BUBBLE_WIDTH = 20
    BUBBLE_HEIGHT = 30
    BUBBLE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
    ANGLE_SPEED = 5
    LAUNCH_SPEED = 10
    MAX_DARTS = 10
    MIN_BALLOONS_TO_WIN = 6

    # Screen setup for pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Targeted Balloon Pop Shooter")
    font = pygame.font.Font(None, 36)

    # Load assets
    background_image = pygame.image.load("D:/GameWithUrsina/ass/a/textures/balloon.jpg")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    pygame.mixer.music.load("D:/GameWithUrsina/ass/a/sounds/background_music.mp3")
    pygame.mixer.music.play(-1)  # Play music in loop

    good_img1 = pygame.image.load("D:/GameWithUrsina/ass/touches/good1.jpg")
    bad_img1 = pygame.image.load("D:/GameWithUrsina/ass/touches/bad7.jpg")
    good_img1 = pygame.transform.scale(good_img1, (200, 200))
    bad_img1 = pygame.transform.scale(bad_img1, (300, 200))

    def render_text_wrapped(text, font, max_width, color):
        """Render text wrapped to fit within max_width."""
        words = text.split(' ')
        lines, current_line, current_width = [], [], 0
        for word in words:
            word_surface = font.render(word, True, color)
            word_width = word_surface.get_width()
            if current_width + word_width <= max_width:
                current_line.append(word)
                current_width += word_width + font.size(' ')[0]  # Add space width
            else:
                lines.append(' '.join(current_line))
                current_line, current_width = [word], word_width + font.size(' ')[0]
        if current_line:
            lines.append(' '.join(current_line))
        return lines, len(lines)

    class Balloon:
        def __init__(self, x, y, color, number):
            self.x, self.y, self.color = x, y, color
            self.width, self.height, self.number, self.active = BUBBLE_WIDTH, BUBBLE_HEIGHT, number, True

        def draw(self):
            pygame.draw.ellipse(screen, self.color, (self.x - self.width // 2, self.y - self.height // 2, self.width, self.height))
            pygame.draw.line(screen, (200, 200, 200), (self.x, self.y + self.height // 2), (self.x, self.y + self.height // 2 + 20), 2)
            number_text = font.render(str(self.number), True, (0, 0, 0))
            screen.blit(number_text, (self.x - 10, self.y - 10))

    class Dart:
        def __init__(self, x, y):
            self.x, self.y, self.angle, self.speed, self.active = x, y, 90, LAUNCH_SPEED, False

        def draw(self):
            if self.active:
                pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 5)

        def move(self):
            if self.active:
                self.x += self.speed * math.cos(math.radians(self.angle))
                self.y -= self.speed * math.sin(math.radians(self.angle))

    def balloon_popping_game():
        clock, running, score, darts_used = pygame.time.Clock(), True, 0, 0
        balloons, rows, cols = [], 2, 5
        x_start, y_start, row_spacing = WIDTH // 2 - ((cols - 1) * BUBBLE_WIDTH * 2) // 2, 200, BUBBLE_HEIGHT * 2.5
        for row in range(rows):
            for col in range(cols):
                x, y = x_start + col * BUBBLE_WIDTH * 2, y_start + row * row_spacing
                balloons.append(Balloon(x, y, random.choice(BUBBLE_COLORS), row * cols + col + 1))

        dart, target_number = Dart(WIDTH // 2, HEIGHT - 50), random.choice([b.number for b in balloons])

        while running:
            screen.fill((0, 0, 0))
            screen.blit(background_image, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        dart.angle += ANGLE_SPEED
                    elif event.key == pygame.K_RIGHT:
                        dart.angle -= ANGLE_SPEED
                    elif event.key == pygame.K_SPACE and not dart.active and darts_used < MAX_DARTS:
                        dart, dart.angle, dart.active, darts_used = Dart(WIDTH // 2, HEIGHT - 50), dart.angle, True, darts_used + 1

            if dart.active:
                dart.move()
                for balloon in balloons:
                    if balloon.active and math.sqrt((balloon.x - dart.x) ** 2 + (balloon.y - dart.y) ** 2) < max(BUBBLE_WIDTH, BUBBLE_HEIGHT):
                        if balloon.number == target_number:
                            balloon.active, score, dart.active = False, score + 10, False
                            balloons.remove(balloon)
                            target_number = random.choice([b.number for b in balloons]) if balloons else None
                        break
                if dart.x < 0 or dart.x > WIDTH or dart.y < 0:
                    dart.active = False

            for balloon in balloons:
                if balloon.active:
                    balloon.draw()
            dart.draw()
            target_text, score_text, darts_text = font.render(f"Target Balloon: {target_number}", True, (0, 0, 0)), font.render(f"Score: {score}", True, (0, 0, 0)), font.render(f"Darts Used: {darts_used}/{MAX_DARTS}", True, (0, 0, 0))
            screen.blit(target_text, (10, HEIGHT - 150))
            screen.blit(score_text, (10, HEIGHT - 90))
            screen.blit(darts_text, (10, HEIGHT - 50))

            if target_number is None or darts_used >= MAX_DARTS:
                show_completion_screen(score >= MIN_BALLOONS_TO_WIN * 10)
                return

            pygame.display.flip()
            clock.tick(30)

    def show_completion_screen(user_wins):
        screen.fill((255, 255, 255))
        message = "Hurrey, You Win The Game! Which Appreciation Would You Choose?" if user_wins else "Game Over! Nice Try, Which Touch Would You Choose For Appreciation?"
        wrapped_text, num_lines = render_text_wrapped(message, font, WIDTH - 40, (0, 0, 0))
        y_offset = 50
        for line in wrapped_text:
            line_surface = font.render(line, True, (0, 0, 0))
            screen.blit(line_surface, (WIDTH // 2 - line_surface.get_width() // 2, y_offset))
            y_offset += 40
        screen.blit(good_img1, (150, 200))
        screen.blit(bad_img1, (450, 200))
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 150 < x < 350 and 200 < y < 400:
                        display_explanation("good")
                    elif 450 < x < 650 and 200 < y < 400:
                        display_explanation("bad")

    def display_explanation(label):
        explanation = "Hurrey,You Guessed Right. This Is A Friendly Touch." if label == "good" else "An Unsafe Touch Makes You Feel Bad , SHOUNT, RUN & TELL Your Parents."
        screen.fill((255, 255, 255))
        wrapped_text, num_lines = render_text_wrapped(explanation, font, WIDTH - 40, (0, 0, 0))
        y_offset = HEIGHT // 2 - num_lines * 20
        for line in wrapped_text:
            line_surface = font.render(line, True, (0, 0, 0))
            screen.blit(line_surface, (WIDTH // 2 - line_surface.get_width() // 2, y_offset))
            y_offset += 40
        ok_button_rect = pygame.Rect(WIDTH // 2 - 75, y_offset + 20, 150, 40)
        pygame.draw.rect(screen, (135, 206, 235), ok_button_rect, border_radius=20)
        ok_button_text = font.render("OK, Got It", True, (0, 0, 0))
        screen.blit(ok_button_text, (ok_button_rect.x + 10, ok_button_rect.y + 5))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and ok_button_rect.collidepoint(event.pos):
                    waiting = False
                    pygame.quit()  # Quit pygame
                    exit()         # Exit the script

    balloon_popping_game()

# # Run the game
# touch_balloon_popping_game()




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Well and full working$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# import pygame
# import random
# import math

# # Initialize pygame
# pygame.init()

# # Game Variables
# WIDTH, HEIGHT = 800, 600
# BUBBLE_WIDTH = 20
# BUBBLE_HEIGHT = 30
# BUBBLE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
# ANGLE_SPEED = 5
# LAUNCH_SPEED = 10
# MAX_DARTS = 10
# MIN_BALLOONS_TO_WIN = 6

# # Screen setup for pygame
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Targeted Balloon Pop Shooter")
# font = pygame.font.Font(None, 36)

# # Load assets
# background_image = pygame.image.load("D:/GameWithUrsina/ass/a/textures/balloon.jpg")
# background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
# pygame.mixer.music.load("D:/GameWithUrsina/ass/a/sounds/background_music.mp3")  # Path to background music file
# pygame.mixer.music.play(-1)  # Play music in loop

# # Load images for explanation screen
# good_img_path1 = "D:/GameWithUrsina/ass/touches/good1.jpg"
# bad_img_path1 = "D:/GameWithUrsina/ass/touches/bad1.jpg"

# good_img1 = pygame.image.load(good_img_path1)
# bad_img1 = pygame.image.load(bad_img_path1)
# good_img1 = pygame.transform.scale(good_img1, (200, 200))
# bad_img1 = pygame.transform.scale(bad_img1, (200, 200))


# def render_text_wrapped(text, font, max_width, color):
#     """Render text wrapped to fit within max_width."""
#     words = text.split(' ')
#     lines = []
#     current_line = []
#     current_width = 0

#     for word in words:
#         word_surface = font.render(word, True, color)
#         word_width = word_surface.get_width()
#         if current_width + word_width <= max_width:
#             current_line.append(word)
#             current_width += word_width + font.size(' ')[0]  # Add space width
#         else:
#             lines.append(' '.join(current_line))
#             current_line = [word]
#             current_width = word_width + font.size(' ')[0]

#     if current_line:
#         lines.append(' '.join(current_line))

#     return lines


# class Balloon:
#     def __init__(self, x, y, color, number):
#         self.x = x
#         self.y = y
#         self.color = color
#         self.width = BUBBLE_WIDTH
#         self.height = BUBBLE_HEIGHT
#         self.number = number
#         self.active = True

#     def draw(self):
#         pygame.draw.ellipse(screen, self.color, (int(self.x - self.width // 2), int(self.y - self.height // 2), self.width, self.height))
#         pygame.draw.line(screen, (200, 200, 200), (int(self.x), int(self.y + self.height // 2)), (int(self.x), int(self.y + self.height // 2 + 20)), 2)
#         number_text = font.render(str(self.number), True, (0, 0, 0))
#         screen.blit(number_text, (self.x - 10, self.y - 10))


# class Dart:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.angle = 90
#         self.speed = LAUNCH_SPEED
#         self.active = False

#     def draw(self):
#         if self.active:
#             pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 5)

#     def move(self):
#         if self.active:
#             self.x += self.speed * math.cos(math.radians(self.angle))
#             self.y -= self.speed * math.sin(math.radians(self.angle))


# def balloon_popping_game():
#     clock = pygame.time.Clock()
#     running = True
#     score = 0
#     darts_used = 0

#     balloons = []
#     rows, cols = 2, 5
#     x_start = WIDTH // 2 - ((cols - 1) * BUBBLE_WIDTH * 2) // 2
#     y_start = 200
#     row_spacing = BUBBLE_HEIGHT * 2.5

#     for row in range(rows):
#         for col in range(cols):
#             x = x_start + col * BUBBLE_WIDTH * 2
#             y = y_start + row * row_spacing
#             balloons.append(Balloon(x, y, random.choice(BUBBLE_COLORS), row * cols + col + 1))

#     dart = Dart(WIDTH // 2, HEIGHT - 50)
#     target_number = random.choice([b.number for b in balloons])

#     while running:
#         screen.fill((0, 0, 0))
#         screen.blit(background_image, (0, 0))

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()  # Exit program immediately
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     dart.angle += ANGLE_SPEED
#                 elif event.key == pygame.K_RIGHT:
#                     dart.angle -= ANGLE_SPEED
#                 elif event.key == pygame.K_SPACE and not dart.active and darts_used < MAX_DARTS:
#                     dart = Dart(WIDTH // 2, HEIGHT - 50)
#                     dart.angle = dart.angle
#                     dart.active = True
#                     darts_used += 1

#         if dart.active:
#             dart.move()
#             for balloon in balloons:
#                 if balloon.active and math.sqrt((balloon.x - dart.x) ** 2 + (balloon.y - dart.y) ** 2) < max(BUBBLE_WIDTH, BUBBLE_HEIGHT):
#                     if balloon.number == target_number:
#                         balloon.active = False
#                         score += 10
#                         dart.active = False
#                         balloons.remove(balloon)
#                         if balloons:
#                             target_number = random.choice([b.number for b in balloons])
#                         else:
#                             target_number = None
#                     break
#             if dart.x < 0 or dart.x > WIDTH or dart.y < 0:
#                 dart.active = False

#         for balloon in balloons:
#             if balloon.active:
#                 balloon.draw()
#         dart.draw()

#         target_text = font.render(f"Target Balloon: {target_number}", True, (0, 0, 0))
#         score_text = font.render(f"Score: {score}", True, (0, 0, 0))
#         darts_text = font.render(f"Darts Used: {darts_used}/{MAX_DARTS}", True, (0, 0, 0))

#         screen.blit(target_text, (10, HEIGHT - 150))
#         screen.blit(score_text, (10, HEIGHT - 90))
#         screen.blit(darts_text, (10, HEIGHT - 50))

#         if target_number is None or darts_used >= MAX_DARTS:
#             show_completion_screen(score >= MIN_BALLOONS_TO_WIN * 10)
#             return

#         pygame.display.flip()
#         clock.tick(30)


# def show_completion_screen(user_wins):
#     screen.fill((255, 255, 255))

#     message = (
#         "Yeah, you win the game! Which appreciation would you choose?"
#         if user_wins
#         else "Nice try! Keep it up, you'll get there! Which appreciation would you choose?"
#     )

#     wrapped_text = render_text_wrapped(message, font, WIDTH - 40, (0, 0, 0))
#     y_offset = 50

#     for line in wrapped_text:
#         line_surface = font.render(line, True, (0, 0, 0))
#         screen.blit(line_surface, (WIDTH // 2 - line_surface.get_width() // 2, y_offset))
#         y_offset += 40  # Line spacing

#     screen.blit(good_img1, (150, 200))
#     screen.blit(bad_img1, (450, 200))

#     pygame.display.flip()

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = event.pos
#                 if 150 < x < 350 and 200 < y < 400:
#                     display_explanation("good")
#                 elif 450 < x < 650 and 200 < y < 400:
#                     display_explanation("bad")


# def display_explanation(label):
#     explanation = (
#         "This is a friendly☺️ touch."
#         if label == "good"
#         else "An unsafe touch makes you feel bad or scared—always tell your parents or a trusted grown-up."
#     )
#     screen.fill((255, 255, 255))

#     wrapped_text = render_text_wrapped(explanation, font, WIDTH - 40, (0, 0, 0))
#     y_offset = HEIGHT // 2 - len(wrapped_text) * 20  # Adjust to center vertically

#     for line in wrapped_text:
#         line_surface = font.render(line, True, (0, 0, 0))
#         screen.blit(line_surface, (WIDTH // 2 - line_surface.get_width() // 2, y_offset))
#         y_offset += 40
#     # Draw button with sky blue color and rounded edges
#     ok_button_rect = pygame.Rect(WIDTH // 2 - 75, y_offset + 20, 150, 40)
#     pygame.draw.rect(screen, (135, 206, 235), ok_button_rect, border_radius=20)  # Sky blue color with rounded edges

#     ok_button_text = font.render("OK, Got It", True, (0, 0, 0))
    
#     screen.blit(ok_button_text, (WIDTH // 2 - ok_button_text.get_width() // 2, y_offset + 30))

#     pygame.display.flip()

#     waiting_for_click = True
#     while waiting_for_click:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()  # Exit the program completely
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = event.pos
#                 if WIDTH // 2 - 75 < x < WIDTH // 2 + 75 and y_offset + 20 < y < y_offset + 60:
#                     waiting_for_click = False
#                     pygame.quit()  # Quit the game window
#                     exit()  # Exit the program completely

#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = event.pos
#                 if WIDTH // 2 - 75 < x < WIDTH // 2 + 75 and y_offset + 20 < y < y_offset + 60:
#                     waiting_for_click = False
#                     balloon_popping_game()


# # Main game loop
# balloon_popping_game()
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




































































































































#$$$$$$$$$$$$$$$$$$$$$$$$$10Chances$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# import pygame  #[1]
# import random
# import math

# # Initialize pygame
# pygame.init()

# # Game Variables
# WIDTH, HEIGHT = 800, 600
# BUBBLE_WIDTH = 20
# BUBBLE_HEIGHT = 30
# BUBBLE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
# ANGLE_SPEED = 5
# LAUNCH_SPEED = 10
# MAX_DARTS = 10
# MIN_BALLOONS_TO_WIN = 6

# # Screen setup for pygame
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Targeted Balloon Pop Shooter")
# font = pygame.font.Font(None, 36)

# # Load assets
# background_image = pygame.image.load("D:/GameWithUrsina/ass/a/textures/balloon.jpg")
# background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
# pygame.mixer.music.load("D:/GameWithUrsina/ass/a/sounds/background_music.mp3")  # Path to background music file
# pygame.mixer.music.play(-1)  # Play music in loop

# # Load images for explanation screen
# good_img_path1 = "D:/GameWithUrsina/ass/touches/good1.jpg"
# bad_img_path1 = "D:/GameWithUrsina/ass/touches/bad1.jpg"

# good_img1 = pygame.image.load(good_img_path1)
# bad_img1 = pygame.image.load(bad_img_path1)
# good_img1 = pygame.transform.scale(good_img1, (200, 200))
# bad_img1 = pygame.transform.scale(bad_img1, (200, 200))


# def render_text_wrapped(text, font, max_width, color):
#     """Render text wrapped to fit within max_width."""
#     words = text.split(' ')
#     lines = []
#     current_line = []
#     current_width = 0

#     for word in words:
#         word_surface = font.render(word, True, color)
#         word_width = word_surface.get_width()
#         if current_width + word_width <= max_width:
#             current_line.append(word)
#             current_width += word_width + font.size(' ')[0]  # Add space width
#         else:
#             lines.append(' '.join(current_line))
#             current_line = [word]
#             current_width = word_width + font.size(' ')[0]

#     if current_line:
#         lines.append(' '.join(current_line))

#     return lines


# class Balloon:
#     def __init__(self, x, y, color, number):
#         self.x = x
#         self.y = y
#         self.color = color
#         self.width = BUBBLE_WIDTH
#         self.height = BUBBLE_HEIGHT
#         self.number = number
#         self.active = True

#     def draw(self):
#         pygame.draw.ellipse(screen, self.color, (int(self.x - self.width // 2), int(self.y - self.height // 2), self.width, self.height))
#         pygame.draw.line(screen, (200, 200, 200), (int(self.x), int(self.y + self.height // 2)), (int(self.x), int(self.y + self.height // 2 + 20)), 2)
#         number_text = font.render(str(self.number), True, (0, 0, 0))
#         screen.blit(number_text, (self.x - 10, self.y - 10))


# class Dart:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.angle = 90
#         self.speed = LAUNCH_SPEED
#         self.active = False

#     def draw(self):
#         if self.active:
#             pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 5)

#     def move(self):
#         if self.active:
#             self.x += self.speed * math.cos(math.radians(self.angle))
#             self.y -= self.speed * math.sin(math.radians(self.angle))


# def balloon_popping_game():
#     clock = pygame.time.Clock()
#     running = True
#     score = 0
#     darts_used = 0

#     balloons = []
#     rows, cols = 2, 5
#     x_start = WIDTH // 2 - ((cols - 1) * BUBBLE_WIDTH * 2) // 2
#     y_start = 200
#     row_spacing = BUBBLE_HEIGHT * 2.5

#     for row in range(rows):
#         for col in range(cols):
#             x = x_start + col * BUBBLE_WIDTH * 2
#             y = y_start + row * row_spacing
#             balloons.append(Balloon(x, y, random.choice(BUBBLE_COLORS), row * cols + col + 1))

#     dart = Dart(WIDTH // 2, HEIGHT - 50)
#     target_number = random.choice([b.number for b in balloons])

#     while running:
#         screen.fill((0, 0, 0))
#         screen.blit(background_image, (0, 0))

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()  # Exit program immediately
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     dart.angle += ANGLE_SPEED
#                 elif event.key == pygame.K_RIGHT:
#                     dart.angle -= ANGLE_SPEED
#                 elif event.key == pygame.K_SPACE and not dart.active and darts_used < MAX_DARTS:
#                     dart = Dart(WIDTH // 2, HEIGHT - 50)
#                     dart.angle = dart.angle
#                     dart.active = True
#                     darts_used += 1

#         if dart.active:
#             dart.move()
#             for balloon in balloons:
#                 if balloon.active and math.sqrt((balloon.x - dart.x) ** 2 + (balloon.y - dart.y) ** 2) < max(BUBBLE_WIDTH, BUBBLE_HEIGHT):
#                     if balloon.number == target_number:
#                         balloon.active = False
#                         score += 10
#                         dart.active = False
#                         balloons.remove(balloon)
#                         if balloons:
#                             target_number = random.choice([b.number for b in balloons])
#                         else:
#                             target_number = None
#                     break
#             if dart.x < 0 or dart.x > WIDTH or dart.y < 0:
#                 dart.active = False

#         for balloon in balloons:
#             if balloon.active:
#                 balloon.draw()
#         dart.draw()

#         target_text = font.render(f"Target Balloon: {target_number}", True, (0, 0, 0))
#         score_text = font.render(f"Score: {score}", True, (0, 0, 0))
#         darts_text = font.render(f"Darts Used: {darts_used}/{MAX_DARTS}", True, (0, 0, 0))

#         screen.blit(target_text, (10, HEIGHT - 150))
#         screen.blit(score_text, (10, HEIGHT - 90))
#         screen.blit(darts_text, (10, HEIGHT - 50))

#         if target_number is None or darts_used >= MAX_DARTS:
#             show_completion_screen(score >= MIN_BALLOONS_TO_WIN * 10)
#             return

#         pygame.display.flip()
#         clock.tick(30)


# def show_completion_screen(user_wins):
#     screen.fill((255, 255, 255))

#     message = (
#         "Yeah, you win the game! Which appreciation would you choose?"
#         if user_wins
#         else "Nice try! Keep it up, you'll get there! Which appreciation would you choose?"
#     )

#     wrapped_text = render_text_wrapped(message, font, WIDTH - 40, (0, 0, 0))
#     y_offset = 50

#     for line in wrapped_text:
#         line_surface = font.render(line, True, (0, 0, 0))
#         screen.blit(line_surface, (WIDTH // 2 - line_surface.get_width() // 2, y_offset))
#         y_offset += 40  # Line spacing

#     screen.blit(good_img1, (150, 200))
#     screen.blit(bad_img1, (450, 200))

#     pygame.display.flip()

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = event.pos
#                 if 150 < x < 350 and 200 < y < 400:
#                     display_explanation("good")
#                 elif 450 < x < 650 and 200 < y < 400:
#                     display_explanation("bad")


# def display_explanation(label):
#     explanation = (
#         "This is a friendly touch."
#         if label == "good"
#         else "An unusual touch is a touch that makes you feel uncomfortable, scared, or hurt, and should never happen."
#     )
#     screen.fill((255, 255, 255))

#     wrapped_text = render_text_wrapped(explanation, font, WIDTH - 40, (0, 0, 0))
#     y_offset = HEIGHT // 2 - len(wrapped_text) * 20  # Adjust to center vertically

#     for line in wrapped_text:
#         line_surface = font.render(line, True, (0, 0, 0))
#         screen.blit(line_surface, (WIDTH // 2 - line_surface.get_width() // 2, y_offset))
#         y_offset += 40  # Line spacing

#     ok_button_rect = pygame.Rect(WIDTH // 2 - 70, HEIGHT - 80, 140, 40)
#     pygame.draw.rect(screen, (100, 200, 255), ok_button_rect, border_radius=15)
#     ok_text = font.render("OK, Got It", True, (0, 0, 0))
#     screen.blit(ok_text, (ok_button_rect.centerx - ok_text.get_width() // 2, ok_button_rect.centery - ok_text.get_height() // 2))
#     pygame.display.flip()

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if ok_button_rect.collidepoint(event.pos):
#                     running = False  # Exit the loop when the button is clicked
#                     return


# if __name__ == "__main__":
#     balloon_popping_game()










#$$$$$$$$$$$$$$$$$$$$$$$$ 5 CHANCES$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# import pygame
# import random
# import math

# # Initialize pygame
# pygame.init()

# # Game Variables
# WIDTH, HEIGHT = 800, 600
# BUBBLE_WIDTH = 20
# BUBBLE_HEIGHT = 30
# BUBBLE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
# ANGLE_SPEED = 5
# LAUNCH_SPEED = 10
# MAX_DARTS = 5
# MIN_BALLOONS_TO_WIN = 6

# # Screen setup for pygame
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Targeted Balloon Pop Shooter")
# font = pygame.font.Font(None, 36)

# # Load assets
# background_image = pygame.image.load("D:/GameWithUrsina/ass/a/textures/balloon.jpg")
# background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
# pygame.mixer.music.load("D:/GameWithUrsina/ass/a/sounds/background_music.mp3")  # Path to background music file
# pygame.mixer.music.play(-1)  # Play music in loop

# # Load image paths
# good_img_paths = [
#     "D:/GameWithUrsina/ass/touches/good1.jpg",
#     "D:/GameWithUrsina/ass/touches/good1.jpg",
#     "D:/GameWithUrsina/ass/touches/good1.jpg",
# ]

# bad_img_paths = [
#     "D:/GameWithUrsina/ass/touches/bad5.png",
#     "D:/GameWithUrsina/ass/touches/bad1.jpg",
#     "D:/GameWithUrsina/ass/touches/bad3.jpg",
# ]


# def render_text_wrapped(text, font, max_width, color):
#     """Render text wrapped to fit within max_width."""
#     words = text.split(' ')
#     lines = []
#     current_line = []
#     current_width = 0

#     for word in words:
#         word_surface = font.render(word, True, color)
#         word_width = word_surface.get_width()
#         if current_width + word_width <= max_width:
#             current_line.append(word)
#             current_width += word_width + font.size(' ')[0]  # Add space width
#         else:
#             lines.append(' '.join(current_line))
#             current_line = [word]
#             current_width = word_width + font.size(' ')[0]

#     if current_line:
#         lines.append(' '.join(current_line))

#     return lines


# class Balloon:
#     def __init__(self, x, y, color, number):
#         self.x = x
#         self.y = y
#         self.color = color
#         self.width = BUBBLE_WIDTH
#         self.height = BUBBLE_HEIGHT
#         self.number = number
#         self.active = True

#     def draw(self):
#         pygame.draw.ellipse(screen, self.color, (int(self.x - self.width // 2), int(self.y - self.height // 2), self.width, self.height))
#         pygame.draw.line(screen, (200, 200, 200), (int(self.x), int(self.y + self.height // 2)), (int(self.x), int(self.y + self.height // 2 + 20)), 2)
#         number_text = font.render(str(self.number), True, (0, 0, 0))
#         screen.blit(number_text, (self.x - 10, self.y - 10))


# class Dart:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.angle = 90
#         self.speed = LAUNCH_SPEED
#         self.active = False

#     def draw(self):
#         if self.active:
#             pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 5)

#     def move(self):
#         if self.active:
#             self.x += self.speed * math.cos(math.radians(self.angle))
#             self.y -= self.speed * math.sin(math.radians(self.angle))


# def load_random_images():
#     """Randomly select one 'good' and one 'bad' image."""
#     good_img_path = random.choice(good_img_paths)
#     bad_img_path = random.choice(bad_img_paths)

#     good_img = pygame.image.load(good_img_path)
#     bad_img = pygame.image.load(bad_img_path)
#     good_img = pygame.transform.scale(good_img, (200, 200))
#     bad_img = pygame.transform.scale(bad_img, (200, 200))
    
#     return good_img, bad_img


# def balloon_popping_game():
#     clock = pygame.time.Clock()
#     running = True
#     score = 0
#     darts_used = 0

#     balloons = []
#     rows, cols = 2, 5
#     x_start = WIDTH // 2 - ((cols - 1) * BUBBLE_WIDTH * 2) // 2
#     y_start = 200
#     row_spacing = BUBBLE_HEIGHT * 2.5

#     for row in range(rows):
#         for col in range(cols):
#             x = x_start + col * BUBBLE_WIDTH * 2
#             y = y_start + row * row_spacing
#             balloons.append(Balloon(x, y, random.choice(BUBBLE_COLORS), row * cols + col + 1))

#     dart = Dart(WIDTH // 2, HEIGHT - 50)
#     target_number = random.choice([b.number for b in balloons])

#     while running:
#         screen.fill((0, 0, 0))
#         screen.blit(background_image, (0, 0))

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()  # Exit program immediately
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     dart.angle += ANGLE_SPEED
#                 elif event.key == pygame.K_RIGHT:
#                     dart.angle -= ANGLE_SPEED
#                 elif event.key == pygame.K_SPACE and not dart.active and darts_used < MAX_DARTS:
#                     dart = Dart(WIDTH // 2, HEIGHT - 50)
#                     dart.angle = dart.angle
#                     dart.active = True
#                     darts_used += 1

#         if dart.active:
#             dart.move()
#             for balloon in balloons:
#                 if balloon.active and math.sqrt((balloon.x - dart.x) ** 2 + (balloon.y - dart.y) ** 2) < max(BUBBLE_WIDTH, BUBBLE_HEIGHT):
#                     if balloon.number == target_number:
#                         balloon.active = False
#                         score += 10
#                         dart.active = False
#                         balloons.remove(balloon)
#                         if balloons:
#                             target_number = random.choice([b.number for b in balloons])
#                         else:
#                             target_number = None
#                     break
#             if dart.x < 0 or dart.x > WIDTH or dart.y < 0:
#                 dart.active = False

#         for balloon in balloons:
#             if balloon.active:
#                 balloon.draw()
#         dart.draw()

#         target_text = font.render(f"Target Balloon: {target_number}", True, (0, 0, 0))
#         score_text = font.render(f"Score: {score}", True, (0, 0, 0))
#         darts_text = font.render(f"Darts Used: {darts_used}/{MAX_DARTS}", True, (0, 0, 0))

#         screen.blit(target_text, (10, HEIGHT - 150))
#         screen.blit(score_text, (10, HEIGHT - 90))
#         screen.blit(darts_text, (10, HEIGHT - 50))

#         if target_number is None or darts_used >= MAX_DARTS:
#             show_completion_screen(score >= MIN_BALLOONS_TO_WIN * 10)
#             return

#         pygame.display.flip()
#         clock.tick(30)


# def show_completion_screen(user_wins):
#     screen.fill((255, 255, 255))

#     # Randomly load images
#     good_img, bad_img = load_random_images()
#     user_wins > 30

#     message = (
#         "Yeah, you win the game! Which appreciation would you choose?"
#         if user_wins
#         else "Nice try! Keep it up, you'll get there! Which appreciation would you choose?"
#     )

#     wrapped_text = render_text_wrapped(message, font, WIDTH - 40, (0, 0, 0))
#     y_offset = 50

#     for line in wrapped_text:
#         line_surface = font.render(line, True, (0, 0, 0))
#         screen.blit(line_surface, (WIDTH // 2 - line_surface.get_width() // 2, y_offset))
#         y_offset += 40  # Line spacing

#     # Display the dynamically selected images
#     screen.blit(good_img, (150, 200))
#     screen.blit(bad_img, (450, 200))

#     pygame.display.flip()

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = event.pos
#                 if 150 < x < 350 and 200 < y < 400:
#                     display_explanation("good")
#                 elif 450 < x < 650 and 200 < y < 400:
#                     display_explanation("bad")
#                 running = False


# def display_explanation(label):
#     explanation = (
#         "This is a friendly touch."
#         if label == "good"
#         else "An unusual touch is a touch that makes you uncomfortable."
#     )

#     running = True
#     while running:
#         screen.fill((255, 255, 255))

#         # Render explanation text
#         wrapped_text = render_text_wrapped(explanation, font, WIDTH - 40, (0, 0, 0))
#         y_offset = HEIGHT // 2 - len(wrapped_text) * 20

#         for line in wrapped_text:
#             line_surface = font.render(line, True, (0, 0, 0))
#             screen.blit(line_surface, (WIDTH // 2 - line_surface.get_width() // 2, y_offset))
#             y_offset += 40

#         # Draw "OK, Got It" button
#         button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 100, 200, 50)
#         pygame.draw.rect(screen, (135, 206, 235), button_rect, border_radius=15)  # Sky blue button with rounded corners
#         pygame.draw.rect(screen, (0, 128, 255), button_rect, 3, border_radius=15)  # Darker blue border with rounded corners
#         button_text = font.render("OK, Got It", True, (0, 0, 0))# button color
#         screen.blit(button_text, (button_rect.centerx - button_text.get_width() // 2, button_rect.centery - button_text.get_height() // 2))

#         pygame.display.flip()

#         # Event handling
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if button_rect.collidepoint(event.pos):
#                     running = False  # Exit explanation loop


# # Start the game
# balloon_popping_game()
