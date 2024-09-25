class Settings:
    def __init__(self):
        self.screen_width = 1920  # 1200
        self.screen_height = 1080  # 800
        self.bg_color = (230, 230, 230)
        # self.bg_color = (0, 0, 0)

        # speed of the ship
        self.ship_speed = 15

        # properties of bullet
        self.bullet_speed = 1.5
        self.bullet_color = (230, 0, 0)
        self.bullet_width = 800
        self.bullet_height = 18
        self.bullets_allowed = 9

        # self.alien_color = (0, 230, 0)
        self.alien_width = 10
        self.alien_height = 22
        self.alien_speed = 1.5

        self.fleet_drop_speed = 10
        self.fleet_direction = -1  # -1 is right & 1 is left
