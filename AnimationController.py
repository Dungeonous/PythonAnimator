# The AnimationController class controls the animation of the guy

import time


class AnimationController:

    def __init__(self, animation_speed: float, animation_length: int):
        self.animation_speed = animation_speed
        self.animation_length = animation_length

    def print_guy_one(self):
        time.sleep(self.animation_speed)
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")

        print("       This is a test       ")
        print("              0             ")
        print("              |             ")
        print("           ___|___          ")
        print("              |             ")
        print("             / \\            ")
        print("            /   \\           ")

    def print_guy_two(self):
        time.sleep(self.animation_speed)
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")
        print("                     ")

        print("       This is a test       ")
        print("              0             ")
        print("            \\ | /           ")
        print("             \\|/            ")
        print("              |             ")
        print("             / \\            ")
        print("            /   \\           ")

    def animate_guy(self):
        for i in range(0, self.animation_length):
            self.print_guy_one()
            self.print_guy_two()

    def get_animation_speed(self):
        return self.animation_speed

    def set_animation_speed(self, animation_speed):
        self.animation_speed = animation_speed

    def get_animation_length(self):
        return self.animation_length

    def set_animation_length(self, animation_length):
        self.animation_speed = animation_length
