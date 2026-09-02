import os
import time
import random
import sys

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Background colors
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_vscode_logo():
    return f"""
{Colors.BLUE}  +================================+
  |  {Colors.CYAN}VS CODE{Colors.BLUE}  {Colors.WHITE}67 MEME{Colors.BLUE}         |
  +================================+{Colors.RESET}
"""

def animate_meme_frames():
    """The famous 'This is fine' meme but with a programmer theme"""
    
    frames = [
        # Frame 1 - The calm before the storm
        f"""
{Colors.YELLOW}  +========================================+
  |                                        |
  |   {Colors.WHITE}:) {Colors.GREEN}"My code is perfect"{Colors.WHITE}        |
  |                                        |
  |   {Colors.CYAN}+-----------------------------+{Colors.WHITE}         |
  |   {Colors.CYAN}| {Colors.WHITE}if (code == 'works') {{     {Colors.CYAN}|{Colors.WHITE}         |
  |   {Colors.CYAN}|   {Colors.GREEN}[OK] All tests pass{Colors.WHITE}     {Colors.CYAN}|{Colors.WHITE}         |
  |   {Colors.CYAN}| {Colors.WHITE}}}{Colors.WHITE}                          {Colors.CYAN}|{Colors.WHITE}         |
  |   {Colors.CYAN}+-----------------------------+{Colors.WHITE}         |
  |                                        |
  |   {Colors.GREEN}[{Colors.WHITE}=========={Colors.GREEN}] 0 errors{Colors.WHITE}        |
  +========================================+{Colors.RESET}
        """,
        
        # Frame 2 - First error appears
        f"""
{Colors.YELLOW}  +========================================+
  |                                        |
  |   {Colors.WHITE}:| {Colors.YELLOW}"Hmm, that's weird"{Colors.WHITE}        |
  |                                        |
  |   {Colors.RED}+-----------------------------+{Colors.WHITE}         |
  |   {Colors.RED}| {Colors.WHITE}if (code == 'works') {{     {Colors.RED}|{Colors.WHITE}         |
  |   {Colors.RED}|   {Colors.RED}[X] Error: line 67{Colors.WHITE}      {Colors.RED}|{Colors.WHITE}         |
  |   {Colors.RED}| {Colors.WHITE}}} {Colors.RED}[!]{Colors.WHITE}                        {Colors.RED}|{Colors.WHITE}         |
  |   {Colors.RED}+-----------------------------+{Colors.WHITE}         |
  |                                        |
  |   {Colors.YELLOW}[{Colors.WHITE}======={Colors.RED}==={Colors.YELLOW}] 1 error{Colors.WHITE}         |
  +========================================+{Colors.RESET}
        """,
        
        # Frame 3 - More errors
        f"""
{Colors.RED}  +========================================+
  |                                        |
  |   {Colors.WHITE}:'( {Colors.RED}"It works on my machine!"{Colors.WHITE}   |
  |                                        |
  |   {Colors.RED}+-----------------------------+{Colors.WHITE}         |
  |   {Colors.RED}| {Colors.WHITE}if (code == 'works') {{     {Colors.RED}|{Colors.WHITE}         |
  |   {Colors.RED}|   {Colors.RED}[X][X][X] 67 errors{Colors.WHITE}       {Colors.RED}|{Colors.WHITE}         |
  |   {Colors.RED}| {Colors.WHITE}}} {Colors.RED}[!][!][!]{Colors.WHITE}                     {Colors.RED}|{Colors.WHITE}         |
  |   {Colors.RED}+-----------------------------+{Colors.WHITE}         |
  |                                        |
  |   {Colors.RED}[{Colors.WHITE}=={Colors.RED}========{Colors.RED}] 67 errors{Colors.WHITE}      |
  +========================================+{Colors.RESET}
        """,
        
        # Frame 4 - Full chaos
        f"""
{Colors.BG_RED}  +========================================+
  |                                        |
  |   {Colors.WHITE}*_* {Colors.RED}"This is fine" *_*{Colors.WHITE}        |
  |                                        |
  |   {Colors.RED}+-----------------------------+{Colors.WHITE}         |
  |   {Colors.RED}| {Colors.WHITE}if (code == 'works') {{     {Colors.RED}|{Colors.WHITE}         |
  |   {Colors.RED}|   {Colors.RED}[X][X][X][X][X] 67 CRASH{Colors.WHITE}      {Colors.RED}|{Colors.WHITE}         |
  |   {Colors.RED}| {Colors.WHITE}}} {Colors.RED}[!][!][!]{Colors.WHITE}                   {Colors.RED}|{Colors.WHITE}         |
  |   {Colors.RED}+-----------------------------+{Colors.WHITE}         |
  |                                        |
  |   {Colors.RED}[{Colors.WHITE}=========={Colors.RED}] 67 CRASHES{Colors.WHITE}     |
  +========================================+{Colors.RESET}
        """
    ]
    
    return frames

def animate_loading_bar():
    """Animated loading bar with VS Code style"""
    width = 40
    for i in range(width + 1):
        bar = f"{Colors.GREEN}[{Colors.WHITE}{'=' * i}{' ' * (width - i)}{Colors.GREEN}]{Colors.RESET}"
        percent = int((i / width) * 100)
        sys.stdout.write(f"\r{bar} {percent}% Compiling 67 files...")
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def meme_zoom_effect():
    """Zoom effect with the number 67"""
    sizes = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    for size in sizes:
        clear_screen()
        print("\n" * 5)
        spaces = " " * (20 - size)
        if size == 5:
            text = f"{Colors.RED}{Colors.BOLD}67{Colors.RESET}"
        elif size >= 3:
            text = f"{Colors.YELLOW}{Colors.BOLD}67{Colors.RESET}"
        else:
            text = f"{Colors.GREEN}{Colors.BOLD}67{Colors.RESET}"
        print(f"{spaces}{text}")
        time.sleep(0.3)

def spinning_cursor():
    """VS Code style spinner"""
    cursor_frames = ['|', '/', '-', '\\']
    for i in range(20):
        sys.stdout.write(f"\r{Colors.CYAN}{cursor_frames[i % len(cursor_frames)]}{Colors.RESET} Building...")
        sys.stdout.flush()
        time.sleep(0.1)
    print()

def main():
    try:
        # Initial setup
        clear_screen()
        print(create_vscode_logo())
        print(f"{Colors.CYAN}[*] Loading 67 Meme Animation...{Colors.RESET}")
        time.sleep(1)
        
        # Loading sequence
        animate_loading_bar()
        time.sleep(0.5)
        
        # Spinning cursor
        spinning_cursor()
        time.sleep(0.5)
        
        # Main meme animation
        frames = animate_meme_frames()
        
        # Animate frames with effects
        for _ in range(2):  # Loop animation twice
            for frame in frames:
                clear_screen()
                print(create_vscode_logo())
                print(frame)
                time.sleep(1)
        
        # Zoom effect
        meme_zoom_effect()
        
        # Final frame
        clear_screen()
        print(create_vscode_logo())
        print(f"""
{Colors.GREEN}  +========================================+
  |                                        |
  |   {Colors.WHITE}[PARTY] {Colors.YELLOW}CONGRATULATIONS!{Colors.WHITE} [PARTY]          |
  |                                        |
  |   {Colors.CYAN}You've reached level 67 of{Colors.WHITE}         |
  |   {Colors.CYAN}programming frustration!{Colors.WHITE}           |
  |                                        |
  |   {Colors.GREEN}Remember: It's not a bug,{Colors.WHITE}          |
  |   {Colors.GREEN}it's a feature!{Colors.WHITE}                  |
  |                                        |
  +========================================+{Colors.RESET}
        """)
        
        # Typing effect for the punchline
        punchline = f"{Colors.BOLD}{Colors.MAGENTA}\n  [ROCKET] Stack Overflow is your best friend!{Colors.RESET}"
        for char in punchline:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print("\n")
        
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}[!] Animation interrupted!{Colors.RESET}")
    
if __name__ == "__main__":
    main()