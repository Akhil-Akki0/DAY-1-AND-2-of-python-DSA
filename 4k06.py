import os
import time
import random
import sys
import math

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Bright colors
    BRIGHT_RED = '\033[101m'
    BRIGHT_GREEN = '\033[102m'
    BRIGHT_YELLOW = '\033[103m'
    BRIGHT_BLUE = '\033[104m'
    BRIGHT_MAGENTA = '\033[105m'
    BRIGHT_CYAN = '\033[106m'
    BRIGHT_WHITE = '\033[107m'
    
    # Background colors
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_effect(text, speed=0.03):
    """Type text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

def animate_progress_bar(message="Loading", duration=2, width=50):
    """Animated progress bar with percentage"""
    for i in range(width + 1):
        percent = int((i / width) * 100)
        bar = '█' * i + '░' * (width - i)
        color = Colors.GREEN if percent < 70 else Colors.YELLOW if percent < 90 else Colors.RED
        sys.stdout.write(f"\r{color}[{bar}] {percent}% {message}{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(duration / width)
    print()

def spinning_loader(message="Processing", duration=2):
    """Spinning loader animation"""
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{Colors.CYAN}{frames[i % len(frames)]} {message}...{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    print()

def create_border(width=60, style="double"):
    """Create decorative borders"""
    if style == "double":
        return "╔" + "═" * (width - 2) + "╗", "║", "╚" + "═" * (width - 2) + "╝"
    elif style == "single":
        return "+" + "-" * (width - 2) + "+", "|", "+" + "-" * (width - 2) + "+"
    else:
        return "*" * width, "*", "*" * width

def matrix_rain_effect(duration=3):
    """Matrix-style rain effect"""
    clear_screen()
    width = 80
    height = 20
    columns = [random.randint(0, height - 1) for _ in range(width)]
    
    end_time = time.time() + duration
    while time.time() < end_time:
        line = []
        for i in range(width):
            if columns[i] > 0:
                char = chr(random.randint(33, 126))
                if random.random() < 0.1:
                    line.append(f"{Colors.GREEN}{char}{Colors.RESET}")
                else:
                    line.append(f"{Colors.DIM}{Colors.GREEN}{char}{Colors.RESET}")
            else:
                line.append(" ")
            columns[i] = (columns[i] + 1) % height
        print("".join(line[:80]))
        time.sleep(0.05)
    clear_screen()

def vs_code_intro():
    """VS Code style intro animation"""
    frames = [
        f"""
{Colors.BLUE}{Colors.BOLD}
    ██╗   ██╗███████╗     ██████╗ ██████╗ ██████╗ ███████╗
    ██║   ██║██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
    ██║   ██║███████╗    ██║     ██║   ██║██║  ██║█████╗  
    ╚██╗ ██╔╝╚════██║    ██║     ██║   ██║██║  ██║██╔══╝  
     ╚████╔╝ ███████║    ╚██████╗╚██████╔╝██████╔╝███████╗
      ╚═══╝  ╚══════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
{Colors.RESET}
        """,
        f"""
{Colors.CYAN}{Colors.BOLD}
    ██╗   ██╗███████╗     ██████╗ ██████╗ ██████╗ ███████╗
    ██║   ██║██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
    ██║   ██║███████╗    ██║     ██║   ██║██║  ██║█████╗  
    ╚██╗ ██╔╝╚════██║    ██║     ██║   ██║██║  ██║██╔══╝  
     ╚████╔╝ ███████║    ╚██████╗╚██████╔╝██████╔╝███████╗
      ╚═══╝  ╚══════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
{Colors.RESET}
        """
    ]
    
    for _ in range(3):
        for frame in frames:
            clear_screen()
            print("\n" * 5)
            print(frame)
            time.sleep(0.3)

def developer_journey_animation():
    """Developer journey animation with multiple scenes"""
    
    scenes = [
        # Scene 1: The Beginning
        f"""
{Colors.CYAN}{Colors.BOLD}  ╔══════════════════════════════════════════════════════╗
  ║                                                      ║
  ║    {Colors.WHITE}🚀 THE DEVELOPER'S JOURNEY{Colors.CYAN}                   ║
  ║                                                      ║
  ║    {Colors.GREEN}Morning 9:00 AM:{Colors.WHITE}                                ║
  ║    "Today I'll write perfect code!"                  ║
  ║                                                      ║
  ║    {Colors.GREEN}☕ Coffee level: 100%{Colors.WHITE}                            ║
  ║    {Colors.GREEN}⚡ Energy level: 100%{Colors.WHITE}                           ║
  ║    {Colors.GREEN}😊 Confidence: Over 9000!{Colors.WHITE}                     ║
  ║                                                      ║
  ╚══════════════════════════════════════════════════════╝{Colors.RESET}
        """,
        
        # Scene 2: First Bug
        f"""
{Colors.YELLOW}{Colors.BOLD}  ╔══════════════════════════════════════════════════════╗
  ║                                                      ║
  ║    {Colors.WHITE}🐛 BUG DETECTED{Colors.YELLOW}                               ║
  ║                                                      ║
  ║    {Colors.WHITE}11:30 AM:{Colors.YELLOW}                                        ║
  ║    "Hmm, that's odd..."                              ║
  ║                                                      ║
  ║    {Colors.YELLOW}☕ Coffee level: 75%{Colors.WHITE}                             ║
  ║    {Colors.YELLOW}⚡ Energy level: 80%{Colors.WHITE}                            ║
  ║    {Colors.YELLOW}🤔 Confusion: Increasing...{Colors.WHITE}                    ║
  ║                                                      ║
  ╚══════════════════════════════════════════════════════╝{Colors.RESET}
        """,
        
        # Scene 3: Stack Overflow Time
        f"""
{Colors.MAGENTA}{Colors.BOLD}  ╔══════════════════════════════════════════════════════╗
  ║                                                      ║
  ║    {Colors.WHITE}📚 STACK OVERFLOW TIME{Colors.MAGENTA}                       ║
  ║                                                      ║
  ║    {Colors.WHITE}2:00 PM:{Colors.MAGENTA}                                         ║
  ║    "Let me copy this solution..."                    ║
  ║    "It has 67 upvotes!"                              ║
  ║                                                      ║
  ║    {Colors.MAGENTA}☕ Coffee level: 50%{Colors.WHITE}                             ║
  ║    {Colors.MAGENTA}⚡ Energy level: 60%{Colors.WHITE}                            ║
  ║    {Colors.MAGENTA}😅 Desperation: High{Colors.WHITE}                            ║
  ║                                                      ║
  ╚══════════════════════════════════════════════════════╝{Colors.RESET}
        """,
        
        # Scene 4: The 67 Error Wall
        f"""
{Colors.RED}{Colors.BOLD}  ╔══════════════════════════════════════════════════════╗
  ║                                                      ║
  ║    {Colors.WHITE}💥 67 ERRORS FOUND{Colors.RED}                             ║
  ║                                                      ║
  ║    {Colors.WHITE}4:30 PM:{Colors.RED}                                         ║
  ║    "IT WORKS ON MY MACHINE!"                         ║
  ║    "But not in production..."                        ║
  ║                                                      ║
  ║    {Colors.RED}☕ Coffee level: 25%{Colors.WHITE}                             ║
  ║    {Colors.RED}⚡ Energy level: 15%{Colors.WHITE}                            ║
  ║    {Colors.RED}😱 Panic: MAXIMUM{Colors.WHITE}                               ║
  ║                                                      ║
  ╚══════════════════════════════════════════════════════╝{Colors.RESET}
        """,
        
        # Scene 5: The Solution
        f"""
{Colors.GREEN}{Colors.BOLD}  ╔══════════════════════════════════════════════════════╗
  ║                                                      ║
  ║    {Colors.WHITE}✨ THE SOLUTION{Colors.GREEN}                                 ║
  ║                                                      ║
  ║    {Colors.WHITE}6:00 PM:{Colors.GREEN}                                         ║
  ║    "Have you tried turning it off"                   ║
  ║    "and on again?"                                   ║
  ║                                                      ║
  ║    {Colors.GREEN}☕ Coffee level: 0%{Colors.WHITE}                               ║
  ║    {Colors.GREEN}⚡ Energy level: 5%{Colors.WHITE}                             ║
  ║    {Colors.GREEN}😌 Relief: It finally works!{Colors.WHITE}                     ║
  ║                                                      ║
  ╚══════════════════════════════════════════════════════╝{Colors.RESET}
        """
    ]
    
    return scenes

def error_count_animation():
    """Animated error counter"""
    clear_screen()
    print(f"{Colors.BOLD}{Colors.RED}  ERROR COUNTER{Colors.RESET}\n")
    
    for i in range(0, 68):
        if i < 20:
            color = Colors.GREEN
            status = "Normal"
        elif i < 40:
            color = Colors.YELLOW
            status = "Warning"
        elif i < 60:
            color = Colors.RED
            status = "Critical"
        else:
            color = Colors.BRIGHT_RED + Colors.BOLD
            status = "CATASTROPHIC"
        
        bar_length = int(i * 50 / 67)
        bar = '█' * bar_length + '░' * (50 - bar_length)
        
        sys.stdout.write(f"\r{color}Errors: {i:3d}/67 [{bar}] {status}{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def floating_67():
    """Floating 67 animation"""
    clear_screen()
    height = 15
    for _ in range(30):
        clear_screen()
        for y in range(height):
            if y == 7:  # Middle row
                spaces = ' ' * (30 + int(10 * math.sin(time.time() * 3)))
                print(f"{spaces}{Colors.BOLD}{Colors.RED}67{Colors.RESET}")
            else:
                print()
        time.sleep(0.1)

def main():
    try:
        # Matrix rain intro
        matrix_rain_effect(2)
        
        # VS Code logo animation
        vs_code_intro()
        
        # Welcome message
        clear_screen()
        print(f"{Colors.CYAN}{Colors.BOLD}")
        type_effect("  Welcome to the Ultimate Developer Meme Experience!\n", 0.05)
        print(f"{Colors.RESET}")
        time.sleep(1)
        
        # Loading bar
        print(f"\n{Colors.WHITE}  Initializing development environment...{Colors.RESET}")
        animate_progress_bar("Loading modules", 3)
        time.sleep(0.5)
        
        # Spinner
        spinning_loader("Compiling 67 files", 2)
        time.sleep(0.5)
        
        # Error counter animation
        error_count_animation()
        time.sleep(1)
        
        # Developer journey scenes
        scenes = developer_journey_animation()
        for scene in scenes:
            clear_screen()
            print(scene)
            time.sleep(3)
        
        # Floating 67 effect
        floating_67()
        
        # Final message with typing effect
        clear_screen()
        print(f"""
{Colors.GREEN}{Colors.BOLD}
  ╔══════════════════════════════════════════════════════╗
  ║                                                      ║
  ║              🎉 SUCCESS! 🎉                          ║
  ║                                                      ║
  ║    You've survived the 67 errors!                    ║
  ║    Level up: Junior → Senior Developer               ║
  ║                                                      ║
  ║    Remember the golden rules:                        ║
  ║    1. It's not a bug, it's a feature                ║
  ║    2. Works on my machine ✓                         ║
  ║    3. Stack Overflow is life                        ║
  ║                                                      ║
  ╚══════════════════════════════════════════════════════╝
{Colors.RESET}
        """)
        
        # Animated ending
        for i in range(3):
            sys.stdout.write(f"\r{Colors.MAGENTA}{Colors.BOLD}  [PRESS CTRL+C TO EXIT] {'🎮' * (i+1)}{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(0.5)
        print("\n")
        
    except KeyboardInterrupt:
        clear_screen()
        print(f"""
{Colors.YELLOW}{Colors.BOLD}
  ╔══════════════════════════════════════════════════════╗
  ║                                                      ║
  ║         Thanks for watching! See you next time!      ║
  ║                                                      ║
  ║         Remember: Keep coding, keep debugging!       ║
  ║                                                      ║
  ╚══════════════════════════════════════════════════════╝
{Colors.RESET}
        """)
        time.sleep(2)

if __name__ == "__main__":
    main()