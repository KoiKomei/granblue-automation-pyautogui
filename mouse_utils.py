import datetime
import traceback
from timeit import default_timer as timer

import pyautogui
import pyperclip


class MouseUtils:
    """
    Provides the utility functions needed to perform mouse-related actions.

    Attributes
    ----------
    game (game.Game): The Game object.

    mouse_speed (float, optional): Time in seconds it takes for the mouse to move to the specified point. Defaults to 0.2.

    debug_mode (bool, optional): Optional flag to print debug messages related to this class. Defaults to False.

    """
    def __init__(self, game, mouse_speed: float = 0.2, debug_mode: bool = False):
        super().__init__()
        
        self.game = game
        self.mouse_speed = mouse_speed
        self.debug_mode = debug_mode

    def move_to(self, x: int, y: int, custom_mouse_speed: float = 0.0):
        """Move the cursor to the coordinates on the screen.

        Args:
            x (int): X coordinate on the screen.
            y (int): Y coordinate on the screen.
            custom_mouse_speed (float, optional): Time in seconds it takes for the mouse to move to the specified point. Defaults to 0.0.

        Returns:
            None
        """
        if (custom_mouse_speed <= 0.0):
            custom_mouse_speed = self.mouse_speed
            
        try:
            pyautogui.moveTo(x, y, custom_mouse_speed, pyautogui.easeInOutQuad)
            return None
        except Exception:
            self.game.print_and_save(f"\n{self.game.printtime()} [ERROR] Bot encountered exception attempting to move the mouse cursor to Point({x}, {y}): \n{traceback.format_exc()}")

    def move_to_instantly(self, x: int, y: int):
        """Move the cursor instantly to the coordinates on the screen.

        Args:
            x (int): X coordinate on the screen.
            y (int): Y coordinate on the screen.

        Returns:
            None
        """
        try:
            pyautogui.moveTo(x, y)
            return None
        except Exception:
            self.game.print_and_save(f"\n{self.game.printtime()} [ERROR] Bot encountered exception attempting to instantly move the mouse cursor to Point({x}, {y}): \n{traceback.format_exc()}")

    def move_and_click_point(self, x: int, y: int, custom_mouse_speed: float = 0.0, mouse_clicks: int = 1):
        """Move the cursor to the specified point on the screen and clicks it.

        Args:
            x (int): X coordinate on the screen.
            y (int): Y coordinate on the screen.
            custom_mouse_speed (float, optional): Time in seconds it takes for the mouse to move to the specified point. Defaults to 0.
            mouse_clicks (int, optional): Number of mouse clicks. Defaults to 1.

        Returns:
            None
        """
        if (custom_mouse_speed <= 0.0):
            custom_mouse_speed = self.mouse_speed
            
        try:
            pyautogui.moveTo(x, y, custom_mouse_speed, pyautogui.easeInOutQuad)
            pyautogui.click(clicks=mouse_clicks)
            return None
        except Exception:
            self.game.print_and_save(f"\n{self.game.printtime()} [ERROR] Bot encountered exception attempting to move the mouse cursor to Point({x}, {y}) and clicking it: \n{traceback.format_exc()}")

    def click_point_instantly(self, x: int, y: int, mouse_clicks: int = 1):
        """Click the specified point on the screen instantly.

        Args:
            x (int): X coordinate on the screen.
            y (int): Y coordinate on the screen.
            mouse_clicks (int, optional): Number of mouse clicks. Defaults to 1.

        Returns:
            None
        """
        try:
            pyautogui.click(x, y, clicks=mouse_clicks)
            return None
        except Exception:
            self.game.print_and_save(f"\n{self.game.printtime()} [ERROR] Bot encountered exception attempting to instantly click the Point({x}, {y}): \n{traceback.format_exc()}")

    def scroll_screen(self, x: int, y: int, scroll_clicks: int):
        """Attempt to scroll the screen to reveal more UI elements from the provided x and y coordinates.

        Args:
            x (int): X coordinate on the screen.
            y (int): Y coordinate on the screen.
            scroll_clicks (int): How much to scroll the screen. Positive for scrolling up and negative for scrolling down.

        Returns:
            None
        """
        if(self.debug_mode):
            self.game.print_and_save(f"{self.game.printtime()} [DEBUG] Now scrolling the screen from ({x}, {y}) by {scroll_clicks} clicks...")
            
        try:
            self.move_to(x, y)
            pyautogui.scroll(scroll_clicks, x=x, y=y)
            return None
        except Exception:
            self.game.print_and_save(f"\n{self.game.printtime()} [ERROR] Bot encountered exception attempting to scroll the screen at Point({x}, {y}) by {scroll_clicks} clicks: \n{traceback.format_exc()}")
    
    def scroll_screen_from_home_button(self, scroll_clicks: int):
        """Attempt to scroll the screen using the "Home" button coordinates to reveal more UI elements.

        Args:
            scroll_clicks (int): How much to scroll the screen. Positive for scrolling up and negative for scrolling down.

        Returns:
            None
        """
        try:
            x = self.game.home_button_location[0]
            y = self.game.home_button_location[1] - 50
            
            if(self.debug_mode):
                self.game.print_and_save(f"{self.game.printtime()} [DEBUG] Now scrolling the screen from the \"Home\" button's coordinates at ({x}, {y}) by {scroll_clicks} clicks...")
                
            self.move_to(x, y)
            pyautogui.scroll(scroll_clicks, x=x, y=y)
            return None
        except Exception:
            self.game.print_and_save(f"\n{self.game.printtime()} [ERROR] Bot encountered exception attempting to scroll the screen from the \"Home\" button: \n{traceback.format_exc()}")
    
    def clear_textbox(self):
        """Clear the selected textbox of all text by selecting all text by CTRL + A and then pressing DEL.

        Returns:
            None
        """
        pyautogui.keyDown("ctrl")
        pyautogui.press("a")
        pyautogui.keyUp("ctrl")
        pyautogui.press("del")
        return None

    def copy_to_clipboard(self, message: str):
        """Copy the message to the clipboard.

        Args:
            message (str): The message to be copied.

        Returns:
            None
        """
        pyperclip.copy(message)
        return None
    
    def paste_from_clipboard(self):
        """Paste from the clipboard. Make sure that the textbox is already selected.

        Returns:
            None
        """
        message = pyperclip.paste()
        pyautogui.write(message)
        return None
