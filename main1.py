#Copy the contents from http://arcade.academy/examples/move_mouse.html#move-mouse and see if you can figure out what is going on. Add comments to any uncommented lines
"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""

import arcade #lets arcade be usable for the code

SCREEN_WIDTH = 640 #sets width of the sreen 
SCREEN_HEIGHT = 480 #sets height of the screen
SCREEN_TITLE = "Move Mouse Example" #names the screen


class Ball: #creates class called ball
    def __init__(self, position_x, position_y, radius, color): #sets up everything that will be in the class

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self): #defines function called draw
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)


class MyGame(arcade.Window): #creates class called mygame

    def __init__(self, width, height, title): #sets up class

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)

    def on_draw(self): #defines function on_draw
        """ Called whenever we need to draw the window. """
        arcade.start_render() #creates the window and ball or at least renders it
        self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy): #defines function on_mouse_motion,happens when mouse moves
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x
        self.ball.position_y = y #sets the postion to that of the mouse

    def on_mouse_press(self, x, y, button, modifiers): #defines function on_mouse_press
        """
        Called when the user presses a mouse button.
        """
        print(f"You clicked button number: {button}") #displays button pressed
        if button == arcade.MOUSE_BUTTON_LEFT: #occurs when mouse is pressed
            self.ball.color = arcade.color.BLACK #sets the balls color to black

    def on_mouse_release(self, x, y, button, modifiers): #defines function on_mouse_release
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT: #occurs when mouse is no longer pressed
            self.ball.color = arcade.color.AUBURN #sets the balls color to AUBURN


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
