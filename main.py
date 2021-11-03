# This is an animation test written in python for a future project

import AnimationController


def main() -> None:
    animation_controller = AnimationController.AnimationController(0.5, 10)
    animation_controller.animate_guy()


if __name__ == '__main__':
    main()

