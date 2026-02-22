import os
import time
from datetime import datetime
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PYlux Big Clock 1.0
    Usage: clock [--live]
    """
    
    # ASCII digits map
    digits = {
        '0': ["  ###  ", " #   # ", " #   # ", " #   # ", "  ###  "],
        '1': ["   #   ", "  ##   ", "   #   ", "   #   ", "  ###  "],
        '2': [" ##### ", "     # ", " ##### ", " #     ", " ##### "],
        '3': [" ##### ", "     # ", "  #### ", "     # ", " ##### "],
        '4': [" #   # ", " #   # ", " ##### ", "     # ", "     # "],
        '5': [" ##### ", " #     ", " ##### ", "     # ", " ##### "],
        '6': [" ##### ", " #     ", " ##### ", " #   # ", " ##### "],
        '7': [" ##### ", "     # ", "    #  ", "   #   ", "   #   "],
        '8': ["  ###  ", " #   # ", "  ###  ", " #   # ", "  ###  "],
        '9': [" ##### ", " #   # ", " ##### ", "     # ", " ##### "],
        ':': ["       ", "   #   ", "       ", "   #   ", "       "],
        ' ': ["       ", "       ", "       ", "       ", "       "]
    }

    def print_big_time():
        now = datetime.now().strftime("%H:%M:%S")
        # Build the 5 lines of the ASCII display
        output = ["", "", "", "", ""]
        for char in now:
            digit_lines = digits.get(char, digits[' '])
            for i in range(5):
                output[i] += digit_lines[i] + "  "
        
        # Clear screen for live effect if needed
        print(f"{Fore.CYAN}{Style.BRIGHT}")
        for line in output:
            print(line)
        print(f"{Style.RESET_ALL}")

    if "--live" in args:
        print(f"{Fore.YELLOW}Live Clock started. Press Ctrl+C to exit.{Style.RESET_ALL}")
        try:
            while True:
                # Use 'cls' for Windows, 'clear' for Linux/Mac
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\n{Fore.MAGENTA}--- PYlux Live Clock ---{Style.RESET_ALL}\n")
                print_big_time()
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{Fore.MAGENTA}Clock stopped.{Style.RESET_ALL}")
    else:
        print_big_time()
