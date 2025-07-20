






















# from ursina import *
# import pygame
# import sys
# import time

# # Timer settings
# URSINA_WINDOW_TIMER = 5  # Change this to set the timer duration for Ursina window
# PYGAME_WINDOW_TIMER = 10  # Change this to set the timer duration for Pygame window

# # Ursina Game Class
# class SafetyGame:
#     def __init__(self):
#         app = Ursina()
#         window.title = "Child Safety Game"
#         window.color = color.black
#         window.size = (1200, 700)

#         # Set up the main background
#         self.background = Entity(
#             parent=camera.ui,
#             model='quad',
#             texture="ass/environments/startPage4.png",
#             scale=(2, 1),
#             position=(0, 0, 1)
#         )

#         # Start Game Button
#         self.start_button = Button(
#             text="Start Game",
#             color=color.azure,
#             scale=(0.4, 0.15),
#             position=(0, 0),
#             text_color=color.white,
#             on_click=self.start_game_with_blink
#         )

#         self.start_button.border_color = color.dark_gray
#         self.start_button.border_width = 0.02
#         self.start_button.on_hover = self.on_hover
#         self.start_button.on_leave = self.on_leave

#         # Variables to hold entities
#         self.character_background = None
#         self.boy_image = None
#         self.girl_image = None
#         self.selection_text = None
#         self.character_image = None
#         self.clothing_options = []
#         self.shoe_options = []

#         app.run()

#     def on_hover(self):
#         self.start_button.color = color.lime
#         self.start_button.scale = (0.45, 0.18)

#     def on_leave(self):
#         self.start_button.color = color.azure
#         self.start_button.scale = (0.4, 0.15)

#     def start_game_with_blink(self):
#         self.start_button.animate_scale((0.45, 0.18), duration=0.1)
#         invoke(self.reset_button_scale, delay=0.1)
#         invoke(self.show_character_selection, delay=0.2)

#     def reset_button_scale(self):
#         self.start_button.scale = (0.4, 0.15)

#     def show_character_selection(self):
#         self.start_button.disable()
#         self.background.disable()

#         self.character_background = Entity(
#             parent=camera.ui,
#             model='quad',
#             texture="ass/environments/startPage4.png",
#             scale=(2, 1),
#             position=(0, 0, 1.5)
#         )

#         self.selection_text = Text(
#             text="Choose Your Character",
#             position=(0.1, 0.4),
#             scale=2.5,
#             color=color.black,
#             parent=camera.ui,
#             z=-1
#         )

#         self.boy_image = Button(
#             parent=camera.ui,
#             model='quad',
#             texture="ass/characters/boy/boy2.png",
#             scale=(0.2, 0.7),
#             position=(-0.4, -0.2),
#             color=color.white,
#             on_click=lambda: self.select_character("boy"),
#             z=-1
#         )

#         self.girl_image = Button(
#             parent=camera.ui,
#             model='quad',
#             texture="ass/characters/girl/girl1.png",
#             scale=(0.2, 0.7),
#             position=(0.3, -0.2),
#             color=color.white,
#             on_click=lambda: self.select_character("girl"),
#             z=-1
#         )

#         # Timer to close the character selection screen after the set duration
#         invoke(self.close_character_selection, delay=URSINA_WINDOW_TIMER)

#     def close_character_selection(self):
#         self.boy_image.disable()
#         self.girl_image.disable()
#         self.selection_text.disable()
#         self.character_background.disable()

#     def select_character(self, character_type):
#         print(f"Selected character: {character_type}")
#         self.boy_image.disable()
#         self.girl_image.disable()
#         self.selection_text.disable()
#         self.character_background.disable()
#         self.show_dressing_screen(character_type)

#     def show_dressing_screen(self, character_type):
#         self.dressing_background = Entity(
#             parent=camera.ui,
#             model='quad',
#             texture="ass/environments/back3.jpg",
#             scale=(2, 1),
#             position=(0, 0, 1)
#         )

#         self.character_image = Entity(
#             parent=camera.ui,
#             model='quad',
#             texture="ass/characters/girl/girl1.png" if character_type == "girl" else f'ass/characters/{character_type}/{character_type}1.png',
#             scale=(0.2, 0.7),
#             position=(0, 0)
#         )

#         # Clothing options
#         clothing_textures = [
#             "ass/cloths/girl-cloths/cloth1.jpg",
#             "ass/cloths/girl-cloths/cloth2.jpg",
#             "ass/cloths/girl-cloths/cloth3.jpg",
#             "ass/cloths/girl-cloths/cloth4.jpg",
#             "ass/cloths/girl-cloths/cloth5.jpg",
#             "ass/cloths/girl-cloths/cloth6.jpg"
#         ]

#         for i, texture in enumerate(clothing_textures):
#             button = Button(
#                 parent=camera.ui,
#                 model='quad',
#                 texture=texture,
#                 scale=(0.2, 0.2),
#                 position=(-0.7, 0.45 - i * 0.18),
#                 color=color.white
#             )
#             self.clothing_options.append(button)

#         # Shoe options (only for girl)
#         if character_type == "girl":
#             shoe_textures = [
#                 "ass/shoes/girlshooes/shoes1.png",
#                 "ass/shoes/girlshooes/shoes2.png",
#                 "ass/shoes/girlshooes/shoes3.png",
#                 "ass/shoes/girlshooes/shoes4.png",
#                 "ass/shoes/girlshooes/shoes5.png"
#             ]

#             for i, texture in enumerate(shoe_textures):
#                 button = Button(
#                     parent=camera.ui,
#                     model='quad',
#                     texture=texture,
#                     scale=(0.2, 0.2),
#                     position=(0.7, 0.45 - i * 0.18),
#                     color=color.white
#                 )
#                 self.shoe_options.append(button)

#         # Add Start Game button here on the dressing screen
#         self.start_game_button = Button(
#             text="Start Game",
#             color=color.orange,
#             scale=(0.25, 0.1),
#             position=(0, -0.4),
#             text_color=color.white,
#             on_click=self.start_main_game,
#             z=-1
#         )

#     def start_main_game(self):
#         pygame_game()

# # Pygame Game
# def pygame_game():
#     pygame.init()

#     # Screen settings
#     screen_width, screen_height = 1200, 700
#     screen = pygame.display.set_mode((screen_width, screen_height))
#     pygame.display.set_caption('Game')

#     # Colors
#     white = (255, 255, 255)

#     # Load images for scenario selection
#     background_image = pygame.image.load("ass/environments/back1.jpg").convert()
#     background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

#     playground_image = pygame.image.load("ass/playG3.jpg").convert_alpha()
#     school_image = pygame.image.load("ass/School1.jpg").convert_alpha()

#     # Scale images for scenario selection
#     playground_image = pygame.transform.scale(playground_image, (200, 150))
#     school_image = pygame.transform.scale(school_image, (200, 150))

#     # Font settings
#     font = pygame.font.Font(None, 48)
#     small_font = pygame.font.Font(None, 36)

#     # Text for scenario selection
#     title_text = font.render('Select Scenario', True, (255, 69, 0))
#     playground_text = small_font.render('Playground', True, (255, 69, 0))
#     school_text = small_font.render('School(Locked)', True, (255, 69, 0))

#     # Navigation settings
#     bg_x = 0
#     scroll_speed = 0.5
#     bg_images = [pygame.image.load("ass/house2.jpg").convert(), pygame.image.load("ass/funfair1.jpg").convert()]
#     bg_images = [pygame.transform.scale(bg, (screen_width, screen_height)) for bg in bg_images]
#     girl_image = pygame.image.load("ass/characters/girl/girl1.png").convert_alpha()
#     girl_image = pygame.transform.scale(girl_image, (100, 200))  # Fix character size

#     # Game state
#         # Game state
#     SCENARIO_SELECTION = 0
#     NAVIGATION = 1
#     game_state = SCENARIO_SELECTION
#     start_time = time.time()
#     running = True

#     # Position of scenario images
#     playground_rect = playground_image.get_rect(topleft=(300, 200))
#     school_rect = school_image.get_rect(topleft=(700, 200))
    
#     while running:
#         elapsed_time = time.time() - start_time
#         if elapsed_time > PYGAME_WINDOW_TIMER:
#             running = False  # Close Pygame window after timer expires

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse click
#                 mouse_pos = pygame.mouse.get_pos()
#                 if game_state == SCENARIO_SELECTION:
#                     if playground_rect.collidepoint(mouse_pos):
#                         game_state = NAVIGATION  # Switch to navigation
#                         print("Selected: Playground")
#                     elif school_rect.collidepoint(mouse_pos):
#                         print("Selected: School (Locked)")
#             elif event.type == pygame.KEYDOWN:
#                 if game_state == NAVIGATION:
#                     if event.key == pygame.K_RIGHT:
#                         bg_x -= scroll_speed  # Move background to simulate right movement
#                     elif event.key == pygame.K_LEFT:
#                         bg_x += scroll_speed  # Move background to simulate left movement

#         screen.fill(white)

#         # Game screen logic
#         if game_state == SCENARIO_SELECTION:
#             screen.blit(background_image, (0, 0))
#             screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 50))
#             screen.blit(playground_image, playground_rect.topleft)
#             screen.blit(school_image, school_rect.topleft)
#             screen.blit(playground_text, (playground_rect.centerx - playground_text.get_width() // 2, playground_rect.bottom + 20))
#             screen.blit(school_text, (school_rect.centerx - school_text.get_width() // 2, school_rect.bottom + 20))
#         elif game_state == NAVIGATION:
#             # Scroll background images
#             bg_x %= screen_width  # Wrap background position
#             for i, bg in enumerate(bg_images):
#                 screen.blit(bg, (bg_x + i * screen_width, 0))
#             # Draw character
#             screen.blit(girl_image, (screen_width // 2 - girl_image.get_width() // 2, screen_height - girl_image.get_height() - 50))

#         pygame.display.flip()

#     pygame.quit()


# # Start the game
# if __name__ == "__main__":
#     SafetyGame()































from ursina import *
import pygame
import sys
import time

# Timer settings
URSINA_WINDOW_TIMER = 5  # Change this to set the timer duration for Ursina window
PYGAME_WINDOW_TIMER = 10  # Change this to set the timer duration for Pygame window

# Ursina Game Class
class SafetyGame:
    def __init__(self):
        app = Ursina()
        window.title = "Child Safety Game"
        window.color = color.black
        window.size = (1200, 700)

        # Set up the main background
        self.background = Entity(
            parent=camera.ui,
            model='quad',
            texture="ass/environments/startPage4.png",
            scale=(2, 1),
            position=(0, 0, 1)
        )

        # Start Game Button
        self.start_button = Button(
            text="Start Game",
            color=color.azure,
            scale=(0.4, 0.15),
            position=(0, 0),
            text_color=color.white,
            on_click=self.start_game_with_blink
        )

        self.start_button.border_color = color.dark_gray
        self.start_button.border_width = 0.02
        self.start_button.on_hover = self.on_hover
        self.start_button.on_leave = self.on_leave

        # Variables to hold entities
        self.character_background = None
        self.boy_image = None
        self.girl_image = None
        self.selection_text = None
        self.character_image = None
        self.clothing_options = []
        self.shoe_options = []

        app.run()

    def on_hover(self):
        self.start_button.color = color.lime
        self.start_button.scale = (0.45, 0.18)

    def on_leave(self):
        self.start_button.color = color.azure
        self.start_button.scale = (0.4, 0.15)

    def start_game_with_blink(self):
        self.start_button.animate_scale((0.45, 0.18), duration=0.1)
        invoke(self.reset_button_scale, delay=0.1)
        invoke(self.show_character_selection, delay=0.2)

    def reset_button_scale(self):
        self.start_button.scale = (0.4, 0.15)

    def show_character_selection(self):
        self.start_button.disable()
        self.background.disable()

        self.character_background = Entity(
            parent=camera.ui,
            model='quad',
            texture="ass/environments/startPage4.png",
            scale=(2, 1),
            position=(0, 0, 1.5)
        )

        self.selection_text = Text(
            text="Choose Your Character",
            position=(0.1, 0.4),
            scale=2.5,
            color=color.black,
            parent=camera.ui,
            z=-1
        )

        self.boy_image = Button(
            parent=camera.ui,
            model='quad',
            texture="ass/characters/boy/boy2.png",
            scale=(0.2, 0.7),
            position=(-0.4, -0.2),
            color=color.white,
            on_click=lambda: self.select_character("boy"),
            z=-1
        )

        self.girl_image = Button(
            parent=camera.ui,
            model='quad',
            texture="ass/characters/girl/girl1.png",
            scale=(0.2, 0.7),
            position=(0.3, -0.2),
            color=color.white,
            on_click=lambda: self.select_character("girl"),
            z=-1
        )

        # Timer to close the character selection screen after the set duration
        invoke(self.close_character_selection, delay=URSINA_WINDOW_TIMER)

    def close_character_selection(self):
        self.boy_image.disable()
        self.girl_image.disable()
        self.selection_text.disable()
        self.character_background.disable()

    def select_character(self, character_type):
        print(f"Selected character: {character_type}")
        self.boy_image.disable()
        self.girl_image.disable()
        self.selection_text.disable()
        self.character_background.disable()
        self.show_dressing_screen(character_type)

    def show_dressing_screen(self, character_type):
        self.dressing_background = Entity(
            parent=camera.ui,
            model='quad',
            texture="ass/environments/back3.jpg",
            scale=(2, 1),
            position=(0, 0, 1)
        )

        self.character_image = Entity(
            parent=camera.ui,
            model='quad',
            texture="ass/characters/girl/girl1.png" if character_type == "girl" else f'ass/characters/{character_type}/{character_type}1.png',
            scale=(0.2, 0.7),
            position=(0, 0)
        )

        # Clothing options
        clothing_textures = [
            "ass/cloths/girl-cloths/cloth1.jpg",
            "ass/cloths/girl-cloths/cloth2.jpg",
            "ass/cloths/girl-cloths/cloth3.jpg",
            "ass/cloths/girl-cloths/cloth4.jpg",
            "ass/cloths/girl-cloths/cloth5.jpg",
            "ass/cloths/girl-cloths/cloth6.jpg"
        ]

        for i, texture in enumerate(clothing_textures):
            button = Button(
                parent=camera.ui,
                model='quad',
                texture=texture,
                scale=(0.2, 0.2),
                position=(-0.7, 0.45 - i * 0.18),
                color=color.white
            )
            self.clothing_options.append(button)

        # Shoe options (only for girl)
        if character_type == "girl":
            shoe_textures = [
                "ass/shoes/girlshooes/shoes1.png",
                "ass/shoes/girlshooes/shoes2.png",
                "ass/shoes/girlshooes/shoes3.png",
                "ass/shoes/girlshooes/shoes4.png",
                "ass/shoes/girlshooes/shoes5.png"
            ]

            for i, texture in enumerate(shoe_textures):
                button = Button(
                    parent=camera.ui,
                    model='quad',
                    texture=texture,
                    scale=(0.2, 0.2),
                    position=(0.7, 0.45 - i * 0.18),
                    color=color.white
                )
                self.shoe_options.append(button)

        # Add Start Game button here on the dressing screen
        self.start_game_button = Button(
            text="Start Game",
            color=color.orange,
            scale=(0.25, 0.1),
            position=(0, -0.4),
            text_color=color.white,
            on_click=self.start_main_game,
            z=-1
        )

    def start_main_game(self):
        pygame_game()

# Pygame Game
def pygame_game():
    pygame.init()

    # Screen settings
    screen_width, screen_height = 1200, 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Game')

    # Colors
    white = (255, 255, 255)

    # Load images for scenario selection
    background_image = pygame.image.load("ass/environments/back1.jpg").convert()
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    playground_image = pygame.image.load("ass/playG3.jpg").convert_alpha()
    school_image = pygame.image.load("ass/School1.jpg").convert_alpha()

    # Scale images for scenario selection
    playground_image = pygame.transform.scale(playground_image, (200, 150))
    school_image = pygame.transform.scale(school_image, (200, 150))

    # Font settings
    font = pygame.font.Font(None, 48)
    small_font = pygame.font.Font(None, 36)

    # Text for scenario selection
    title_text = font.render('Select Scenario', True, (255, 69, 0))
    playground_text = small_font.render('Playground', True, (255, 69, 0))
    school_text = small_font.render('School(Locked)', True, (255, 69, 0))

    # Navigation settings
    bg_x = 0
    scroll_speed = 0.5
    bg_images = [pygame.image.load("ass/house2.jpg").convert(), pygame.image.load("ass/funfair1.jpg").convert()]
    bg_images = [pygame.transform.scale(bg, (screen_width, screen_height)) for bg in bg_images]
    girl_image = pygame.image.load("ass/characters/girl/girl1.png").convert_alpha()
    girl_image = pygame.transform.scale(girl_image, (100, 200))  # Fix character size

    # Game state
        # Game state
    SCENARIO_SELECTION = 0
    NAVIGATION = 1
    game_state = SCENARIO_SELECTION
    start_time = time.time()
    running = True

    # Position of scenario images
    playground_rect = playground_image.get_rect(topleft=(300, 200))
    school_rect = school_image.get_rect(topleft=(700, 200))
    
    while running:
        elapsed_time = time.time() - start_time
        if elapsed_time > PYGAME_WINDOW_TIMER:
            running = False  # Close Pygame window after timer expires

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse click
                mouse_pos = pygame.mouse.get_pos()
                if game_state == SCENARIO_SELECTION:
                    if playground_rect.collidepoint(mouse_pos):
                        game_state = NAVIGATION  # Switch to navigation
                        print("Selected: Playground")
                    elif school_rect.collidepoint(mouse_pos):
                        print("Selected: School (Locked)")
            elif event.type == pygame.KEYDOWN:
                if game_state == NAVIGATION:
                    if event.key == pygame.K_RIGHT:
                        bg_x -= scroll_speed  # Move background to simulate right movement
                    elif event.key == pygame.K_LEFT:
                        bg_x += scroll_speed  # Move background to simulate left movement

        screen.fill(white)

        # Game screen logic
        if game_state == SCENARIO_SELECTION:
            screen.blit(background_image, (0, 0))
            screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 50))
            screen.blit(playground_image, playground_rect.topleft)
            screen.blit(school_image, school_rect.topleft)
            screen.blit(playground_text, (playground_rect.centerx - playground_text.get_width() // 2, playground_rect.bottom + 20))
            screen.blit(school_text, (school_rect.centerx - school_text.get_width() // 2, school_rect.bottom + 20))
        elif game_state == NAVIGATION:
            # Scroll background images
            bg_x %= screen_width  # Wrap background position
            for i, bg in enumerate(bg_images):
                screen.blit(bg, (bg_x + i * screen_width, 0))
            # Draw character
            screen.blit(girl_image, (screen_width // 2 - girl_image.get_width() // 2, screen_height - girl_image.get_height() - 50))

        pygame.display.flip()

    pygame.quit()


# Start the game
if __name__ == "__main__":
    SafetyGame()
















































































































































































































































































