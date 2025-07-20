

# import pygame
# import sys
# import time
# # Initialize Pygame
# pygame.init()

# # Screen settings
# screen_width, screen_height = 800, 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Game')

# # Colors
# white = (255, 255, 255)

# # Load images for scenario selection
# background_image = pygame.image.load("D:/GameWithUrsina/ass/environments/back1.jpg").convert()
# background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# playground_image = pygame.image.load("D:/GameWithUrsina/ass/playG3.jpg").convert_alpha()
# school_image = pygame.image.load("D:/GameWithUrsina/ass/School1.jpg").convert_alpha()

# # Scale images for scenario selection
# playground_image = pygame.transform.scale(playground_image, (200, 150))
# school_image = pygame.transform.scale(school_image, (200, 150))

# # Set up fonts
# font = pygame.font.Font(None, 48)
# small_font = pygame.font.Font(None, 36)

# # Render text for scenario selection
# title_text = font.render('Select Scenario', True, (255, 69, 0))
# playground_text = small_font.render('Playground', True, (255, 69, 0))
# school_text = small_font.render('School(Locked)', True, (255, 69, 0))

# # Get text and image positions
# title_rect = title_text.get_rect(center=(screen_width // 2, 170))
# playground_rect = playground_image.get_rect(center=(screen_width // 2 - 150, screen_height // 2))
# playground_text_rect = playground_text.get_rect(center=(playground_rect.centerx, playground_rect.bottom + 20))
# school_rect = school_image.get_rect(center=(screen_width // 2 + 150, screen_height // 2))
# school_text_rect = school_text.get_rect(center=(school_rect.centerx, school_rect.bottom + 20))

# # Load navigation images
# home_image = pygame.image.load("D:/GameWithUrsina/ass/house2.jpg").convert()
# carnival_image = pygame.image.load("D:/GameWithUrsina/ass/funfair1.jpg").convert()
# girl_image = pygame.image.load("D:/GameWithUrsina/ass/characters/girl/girl1.png").convert_alpha()

# # Scale navigation images
# home_image = pygame.transform.scale(home_image, (screen_width, screen_height))
# carnival_image = pygame.transform.scale(carnival_image, (screen_width, screen_height))
# girl_image = pygame.transform.scale(girl_image, (100, 150))

# # Navigation settings
# bg_x = 0
# scroll_speed = 0.5
# bg_images = [home_image, carnival_image]
# current_bg_index = 0
# next_bg_index = 1
# girl_position = (50, screen_height - girl_image.get_height() - 50)

# # Game state
# SCENARIO_SELECTION = 0
# NAVIGATION = 1
# game_state = SCENARIO_SELECTION

# # Main loop
# running = True
# moving_right = False
# moving_left = False

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if game_state == NAVIGATION:
#                 if event.key == pygame.K_RIGHT:
#                     moving_right = True
#                 elif event.key == pygame.K_LEFT:
#                     moving_left = True
#         elif event.type == pygame.KEYUP:
#             if game_state == NAVIGATION:
#                 if event.key == pygame.K_RIGHT:
#                     moving_right = False
#                 elif event.key == pygame.K_LEFT:
#                     moving_left = False
#         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             mouse_pos = pygame.mouse.get_pos()
#             if game_state == SCENARIO_SELECTION:
#                 # Check if playground or school is clicked
#                 if playground_rect.collidepoint(mouse_pos):
#                     game_state = NAVIGATION
#                 elif school_rect.collidepoint(mouse_pos):
#                     print("School selected (add code for school navigation if needed)")

#     # Game states
#     if game_state == SCENARIO_SELECTION:
#         # Draw scenario selection screen
#         screen.blit(background_image, (0, 0))
#         screen.blit(title_text, title_rect)
#         screen.blit(playground_image, playground_rect)
#         screen.blit(playground_text, playground_text_rect)
#         screen.blit(school_image, school_rect)
#         screen.blit(school_text, school_text_rect)

#     elif game_state == NAVIGATION:
#         # Navigation background scrolling logic
#         if moving_right:
#             bg_x -= scroll_speed
#             if bg_x <= -screen_width:
#                 bg_x = 0
#                 current_bg_index = (current_bg_index + 1) % len(bg_images)
#                 next_bg_index = (current_bg_index + 1) % len(bg_images)
#         elif moving_left:
#             bg_x += scroll_speed
#             if bg_x >= screen_width:
#                 bg_x = 0
#                 current_bg_index = (current_bg_index - 1) % len(bg_images)
#                 next_bg_index = (current_bg_index - 1) % len(bg_images)

#         # Draw navigation screen
#         screen.blit(bg_images[current_bg_index], (bg_x, 0))
#         screen.blit(bg_images[next_bg_index], (bg_x + screen_width, 0))
#         screen.blit(girl_image, girl_position)

#     # Update display
#     pygame.display.flip()

# # Quit Pygame
# pygame.quit()
# sys.exit()




import pygame
import sys
import time
# Initialize Pygame
pygame.init()

# Screen settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game')

# Colors
white = (255, 255, 255)

# Load images for scenario selection
background_image = pygame.image.load("D:/GameWithUrsina/ass/environments/back1.jpg").convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

playground_image = pygame.image.load("D:/GameWithUrsina/ass/playG3.jpg").convert_alpha()
school_image = pygame.image.load("D:/GameWithUrsina/ass/School1.jpg").convert_alpha()

# Scale images for scenario selection
playground_image = pygame.transform.scale(playground_image, (200, 150))
school_image = pygame.transform.scale(school_image, (200, 150))

# Set up fonts
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)

# Render text for scenario selection
title_text = font.render('Select Scenario', True, (255, 69, 0))
playground_text = small_font.render('Playground', True, (255, 69, 0))
school_text = small_font.render('School(Locked)', True, (255, 69, 0))

# Get text and image positions
title_rect = title_text.get_rect(center=(screen_width // 2, 170))
playground_rect = playground_image.get_rect(center=(screen_width // 2 - 150, screen_height // 2))
playground_text_rect = playground_text.get_rect(center=(playground_rect.centerx, playground_rect.bottom + 20))
school_rect = school_image.get_rect(center=(screen_width // 2 + 150, screen_height // 2))
school_text_rect = school_text.get_rect(center=(school_rect.centerx, school_rect.bottom + 20))

# Load navigation images
home_image = pygame.image.load("D:/GameWithUrsina/ass/house2.jpg").convert()
carnival_image = pygame.image.load("D:/GameWithUrsina/ass/funfair1.jpg").convert()
girl_image = pygame.image.load("D:/GameWithUrsina/ass/characters/girl/girl1.png").convert_alpha()

# Scale navigation images
home_image = pygame.transform.scale(home_image, (screen_width, screen_height))
carnival_image = pygame.transform.scale(carnival_image, (screen_width, screen_height))
girl_image = pygame.transform.scale(girl_image, (100, 150))

# Navigation settings
bg_x = 0
scroll_speed = 0.5
bg_images = [home_image, carnival_image]
current_bg_index = 0
next_bg_index = 1
girl_position = (50, screen_height - girl_image.get_height() - 50)

# Game state
SCENARIO_SELECTION = 0
NAVIGATION = 1
game_state = SCENARIO_SELECTION

# Main loop
running = True
moving_right = False
moving_left = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_state == NAVIGATION:
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                elif event.key == pygame.K_LEFT:
                    moving_left = True
        elif event.type == pygame.KEYUP:
            if game_state == NAVIGATION:
                if event.key == pygame.K_RIGHT:
                    moving_right = False
                elif event.key == pygame.K_LEFT:
                    moving_left = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if game_state == SCENARIO_SELECTION:
                # Check if playground or school is clicked
                if playground_rect.collidepoint(mouse_pos):
                    game_state = NAVIGATION
                elif school_rect.collidepoint(mouse_pos):
                    print("School selected (add code for school navigation if needed)")

    # Game states
    if game_state == SCENARIO_SELECTION:
        # Draw scenario selection screen
        screen.blit(background_image, (0, 0))
        screen.blit(title_text, title_rect)
        screen.blit(playground_image, playground_rect)
        screen.blit(playground_text, playground_text_rect)
        screen.blit(school_image, school_rect)
        screen.blit(school_text, school_text_rect)

    elif game_state == NAVIGATION:
        # Navigation background scrolling logic
        if moving_right:
            bg_x -= scroll_speed
            if bg_x <= -screen_width:
                bg_x = 0
                current_bg_index = (current_bg_index + 1) % len(bg_images)
                next_bg_index = (current_bg_index + 1) % len(bg_images)
        elif moving_left:
            bg_x += scroll_speed
            if bg_x >= screen_width:
                bg_x = 0
                current_bg_index = (current_bg_index - 1) % len(bg_images)
                next_bg_index = (current_bg_index - 1) % len(bg_images)

        # Draw navigation screen
        screen.blit(bg_images[current_bg_index], (bg_x, 0))
        screen.blit(bg_images[next_bg_index], (bg_x + screen_width, 0))
        screen.blit(girl_image, girl_position)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
