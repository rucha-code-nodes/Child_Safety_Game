# from ursina import *

# app = Ursina()

# class SafetyGame:
#     def __init__(self):
#         window.title = "Child Safety Game"
#         window.color = color.black

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
#         parent=camera.ui,
#         model='quad',
#         texture="ass/characters/girl/girl1.png",
#         scale=(0.2, 0.7),  # Adjust the scale to make the image smaller
#         position=(0.3, -0.2),
#         color=color.white,
#         on_click=lambda: self.select_character("girl"),
#         z=-1
# )

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
#             # Use the specified girl image for the dressing screen as well
#             texture="ass/characters/girl/girl1.png" if character_type == "girl" else f'D:\\GameWithUrsina\\ass\\characters{character_type}\\{character_type}1.png',
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
#                 color=color.white,
#                 on_click=lambda t=texture: None
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
#                     color=color.white,
#                     on_click=lambda t=texture: None
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
#         print("Starting the main game...")

# # Run the game
# game = SafetyGame()
# app.run()


# from ursina import *


# def start_safety_game():
#     app = Ursina()

#     class SafetyGame:
#         def __init__(self):
#             window.title = "Child Safety Game"
#             window.color = color.black

#             # Set up the main background
#             self.background = Entity(
#                 parent=camera.ui,
#                 model='quad',
#                 texture="ass/environments/startPage4.png",
#                 scale=(2, 1),
#                 position=(0, 0, 1)
#             )

#             # Start Game Button
#             self.start_button = Button(
#                 text="Start Game",
#                 color=color.azure,
#                 scale=(0.4, 0.15),
#                 position=(0, 0),
#                 text_color=color.white,
#                 on_click=self.start_game_with_blink
#             )

#             self.start_button.border_color = color.dark_gray
#             self.start_button.border_width = 0.02
#             self.start_button.on_hover = self.on_hover
#             self.start_button.on_leave = self.on_leave

#             # Variables to hold entities
#             self.character_background = None
#             self.boy_image = None
#             self.girl_image = None
#             self.selection_text = None
#             self.character_image = None
#             self.clothing_options = []
#             self.shoe_options = []

#         def on_hover(self):
#             self.start_button.color = color.lime
#             self.start_button.scale = (0.45, 0.18)

#         def on_leave(self):
#             self.start_button.color = color.azure
#             self.start_button.scale = (0.4, 0.15)

#         def start_game_with_blink(self):
#             self.start_button.animate_scale((0.45, 0.18), duration=0.1)
#             invoke(self.reset_button_scale, delay=0.1)
#             invoke(self.show_character_selection, delay=0.2)

#         def reset_button_scale(self):
#             self.start_button.scale = (0.4, 0.15)

#         def show_character_selection(self):
#             self.start_button.disable()
#             self.background.disable()

#             self.character_background = Entity(
#                 parent=camera.ui,
#                 model='quad',
#                 texture="ass/environments/startPage4.png",
#                 scale=(2, 1),
#                 position=(0, 0, 1.5)
#             )

#             self.selection_text = Text(
#                 text="Choose Your Character",
#                 position=(0.1, 0.4),
#                 scale=2.5,
#                 color=color.black,
#                 parent=camera.ui,
#                 z=-1
#             )

#             self.boy_image = Button(
#                 parent=camera.ui,
#                 model='quad',
#                 texture="ass/characters/boy/boy2.png",
#                 scale=(0.2, 0.7),
#                 position=(-0.4, -0.2),
#                 color=color.white,
#                 on_click=lambda: self.select_character("boy"),
#                 z=-1
#             )

#             self.girl_image = Button(
#                 parent=camera.ui,
#                 model='quad',
#                 texture="ass/characters/girl/girl1.png",
#                 scale=(0.2, 0.7),
#                 position=(0.3, -0.2),
#                 color=color.white,
#                 on_click=lambda: self.select_character("girl"),
#                 z=-1
#             )

#         def select_character(self, character_type):
#             print(f"Selected character: {character_type}")
#             self.boy_image.disable()
#             self.girl_image.disable()
#             self.selection_text.disable()
#             self.character_background.disable()
#             self.show_dressing_screen(character_type)

#         def show_dressing_screen(self, character_type):
#             self.dressing_background = Entity(
#                 parent=camera.ui,
#                 model='quad',
#                 texture="ass/environments/back3.jpg",
#                 scale=(2, 1),
#                 position=(0, 0, 1)
#             )

#             self.character_image = Entity(
#                 parent=camera.ui,
#                 model='quad',
#                 texture="ass/characters/girl/girl1.png" if character_type == "girl" else f'ass/characters/{character_type}/{character_type}1.png',
#                 scale=(0.2, 0.7),
#                 position=(0, 0)
#             )

#             # Clothing options
#             clothing_textures = [
#                 "ass/cloths/girl-cloths/cloth1.jpg",
#                 "ass/cloths/girl-cloths/cloth2.jpg",
#                 "ass/cloths/girl-cloths/cloth3.jpg",
#                 "ass/cloths/girl-cloths/cloth4.jpg",
#                 "ass/cloths/girl-cloths/cloth5.jpg",
#                 "ass/cloths/girl-cloths/cloth6.jpg"
#             ]

#             for i, texture in enumerate(clothing_textures):
#                 button = Button(
#                     parent=camera.ui,
#                     model='quad',
#                     texture=texture,
#                     scale=(0.2, 0.2),
#                     position=(-0.7, 0.45 - i * 0.18),
#                     color=color.white,
#                     on_click=lambda t=texture: None
#                 )
#                 self.clothing_options.append(button)

#             # Shoe options (only for girl)
#             if character_type == "girl":
#                 shoe_textures = [
#                     "ass/shoes/girlshooes/shoes1.png",
#                     "ass/shoes/girlshooes/shoes2.png",
#                     "ass/shoes/girlshooes/shoes3.png",
#                     "ass/shoes/girlshooes/shoes4.png",
#                     "ass/shoes/girlshooes/shoes5.png"
#                 ]

#                 for i, texture in enumerate(shoe_textures):
#                     button = Button(
#                         parent=camera.ui,
#                         model='quad',
#                         texture=texture,
#                         scale=(0.2, 0.2),
#                         position=(0.7, 0.45 - i * 0.18),
#                         color=color.white,
#                         on_click=lambda t=texture: None
#                     )
#                     self.shoe_options.append(button)

#             # Add Start Game button here on the dressing screen
#             self.start_game_button = Button(
#                 text="Start Game",
#                 color=color.orange,
#                 scale=(0.25, 0.1),
#                 position=(0, -0.4),
#                 text_color=color.white,
#                 on_click=self.start_main_game,
#                 z=-1
#             )

#         def on_game_complete(self):
#             print("Safety game completed")
#             app.user_exit()  # Close the Ursina window after the game is done.


#     game = SafetyGame()
#     app.run()


from ursina import *
from time import sleep

def start_safety_game():
    app = Ursina()

    class SafetyGame:
        def __init__(self):
            window.title = "Child Safety Game"
            window.color = color.black

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
                    color=color.white,
                    on_click=lambda t=texture: None
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
                        color=color.white,
                        on_click=lambda t=texture: None
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
            # This method will be triggered when the 'start' button is clicked
            print("Starting the main game!")
            # Call a method with a slight delay to transition to the main game
            invoke(self.run_main_game, delay=1)

        def run_main_game(self):
            # Main game logic
            print("Main game is now running!")
            # Your main game code here

        def on_game_complete(self):
            print("Safety game completed")
            app.user_exit()  # Close the Ursina window after the game is done.

    game = SafetyGame()
    app.run()

# Start the game
start_safety_game()

