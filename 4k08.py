import os
import time
import sys
import random
import threading
import platform

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BLACK = '\033[30m'  # Added missing BLACK color
    
    # Background colors
    BG_YELLOW = '\033[43m'
    BG_RED = '\033[41m'
    BG_BLACK = '\033[40m'
    BG_WHITE = '\033[47m'
    BG_BLUE = '\033[44m'  # Added for more options
    BG_GREEN = '\033[42m'  # Added for more options

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_beep(frequency=440, duration=0.1):
    """Play a beep sound (cross-platform)"""
    try:
        if platform.system() == 'Windows':
            import winsound
            winsound.Beep(frequency, int(duration * 1000))
        else:
            # For Linux/Mac, use print with bell character
            sys.stdout.write('\a')
            sys.stdout.flush()
            time.sleep(duration)
    except:
        # Fallback: visual indicator
        sys.stdout.write(f"{Colors.YELLOW}♪{Colors.RESET}")
        sys.stdout.flush()

def play_pikachu_sound():
    """Play Pikachu-like sound sequence"""
    # Simulate "Pika Pika" with beeps
    sounds = [
        (800, 0.1),  # Pi
        (600, 0.1),  # ka
        (800, 0.1),  # Pi
        (600, 0.1),  # ka
        (1000, 0.2), # CHU!
    ]
    
    for freq, duration in sounds:
        play_beep(freq, duration)
        time.sleep(0.05)

def play_thunder_sound():
    """Play thunder-like sound"""
    sounds = [
        (200, 0.3),
        (150, 0.4),
        (100, 0.5),
    ]
    
    for freq, duration in sounds:
        play_beep(freq, duration)

def create_pikachu_frame(expression="normal", electricity=False, size="medium"):
    """Create Pikachu ASCII art frame"""
    
    # Define Pikachu faces for different expressions
    faces = {
        "normal": [
            "   ⣿⣿⣿⣿⣿⣿⣿⣿   ",
            "  ⣿⣿⣿⣿⣿⣿⣿⣿⣿  ",
            " ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ",
            " ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ",
            " ⣿⣿⣿⠛⠛⣿⣿⣿⣿⣿ ",
            " ⣿⣿⠋    ⠙⣿⣿⣿⣿ ",
            " ⣿⣿  ◉  ◉  ⣿⣿⣿⣿ ",
            " ⣿⣿  ▄  ▄  ⣿⣿⣿⣿ ",
            "  ⣿⣿  ╰╯  ⣿⣿⣿⣿  ",
            "   ⣿⣿⣿⣿⣿⣿⣿⣿   ",
        ],
        "happy": [
            "   ⣿⣿⣿⣿⣿⣿⣿⣿   ",
            "  ⣿⣿⣿⣿⣿⣿⣿⣿⣿  ",
            " ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ",
            " ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ",
            " ⣿⣿⣿╮╭⣿⣿⣿⣿⣿⣿ ",
            " ⣿⣿╰╮╰╯╭╯⣿⣿⣿⣿⣿ ",
            " ⣿⣿  ◕  ◕  ⣿⣿⣿⣿ ",
            " ⣿⣿  ⌒  ⌒  ⣿⣿⣿⣿ ",
            "  ⣿⣿  ╰╯  ⣿⣿⣿⣿  ",
            "   ⣿⣿⣿⣿⣿⣿⣿⣿   ",
        ],
        "angry": [
            "   ⣿⣿⣿⣿⣿⣿⣿⣿   ",
            "  ⣿⣿⣿⣿⣿⣿⣿⣿⣿  ",
            " ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ",
            " ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ",
            " ⣿⣿╮╭⣿⣿╮╭⣿⣿⣿⣿ ",
            " ⣿⣿╰╯⣿⣿╰╯⣿⣿⣿⣿ ",
            " ⣿⣿  ◉  ◉  ⣿⣿⣿⣿ ",
            " ⣿⣿  ╭╮  ⣿⣿⣿⣿⣿ ",
            "  ⣿⣿  ╰╯  ⣿⣿⣿⣿  ",
            "   ⣿⣿⣿⣿⣿⣿⣿⣿   ",
        ],
        "surprised": [
            "   ⣿⣿⣿⣿⣿⣿⣿⣿   ",
            "  ⣿⣿⣿⣿⣿⣿⣿⣿⣿  ",
            " ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ",
            " ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ",
            " ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ",
            " ⣿⣿╭╮╭╮╭╮╭╮⣿⣿⣿⣿ ",
            " ⣿⣿  ○  ○  ⣿⣿⣿⣿ ",
            " ⣿⣿  ○  ○  ⣿⣿⣿⣿ ",
            "  ⣿⣿  ╰╯  ⣿⣿⣿⣿  ",
            "   ⣿⣿⣿⣿⣿⣿⣿⣿   ",
        ],
    }
    
    face = faces.get(expression, faces["normal"])
    
    # Add electricity effects
    electricity_art = ""
    if electricity:
        electricity_art = f"""
{Colors.YELLOW}    ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡
   ⚡              ⚡
  ⚡   ELECTRIC    ⚡
   ⚡              ⚡
    ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡{Colors.RESET}
"""
    
    # Combine face with color
    pikachu_art = "\n".join(face)
    
    return f"""
{Colors.BG_YELLOW}{Colors.BLACK}
{pikachu_art}
{Colors.RESET}
{electricity_art}
"""

def create_pikachu_body():
    """Full Pikachu with body"""
    return f"""
{Colors.YELLOW}      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
   ⣿⣿⣿⣿⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿
   ⣿⣿⣿⠋    ⠙⣿⣿⣿⣿⣿⣿⣿⣿
   ⣿⣿⣿  ◉  ◉  ⣿⣿⣿⣿⣿⣿⣿⣿
   ⣿⣿⣿  ▄  ▄  ⣿⣿⣿⣿⣿⣿⣿⣿
   ⣿⣿⣿  ╰╯  ⣿⣿⣿⣿⣿⣿⣿⣿
   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{Colors.RESET}
"""

def thunder_bolt_animation():
    """Animated thunder bolt"""
    bolts = [
        f"""
{Colors.YELLOW}      ⚡
     ⚡⚡
    ⚡⚡⚡
     ⚡⚡
      ⚡{Colors.RESET}
""",
        f"""
{Colors.YELLOW}      ⚡
     ⚡⚡
    ⚡⚡⚡
   ⚡⚡⚡⚡
    ⚡⚡⚡
     ⚡⚡
      ⚡{Colors.RESET}
""",
        f"""
{Colors.YELLOW}      ⚡
     ⚡⚡
    ⚡⚡⚡
   ⚡⚡⚡⚡
  ⚡⚡⚡⚡⚡
   ⚡⚡⚡⚡
    ⚡⚡⚡
     ⚡⚡
      ⚡{Colors.RESET}
""",
    ]
    
    for _ in range(3):
        for bolt in bolts:
            clear_screen()
            print(bolt)
            play_thunder_sound()
            time.sleep(0.2)

def pikachu_dance():
    """Pikachu dancing animation"""
    dance_frames = [
        "normal",
        "happy",
        "surprised",
        "happy",
        "normal",
        "angry",
        "happy",
        "surprised",
    ]
    
    for expression in dance_frames:
        clear_screen()
        print(create_pikachu_frame(expression=expression))
        play_pikachu_sound()
        time.sleep(0.3)

def pikachu_electric_attack():
    """Pikachu using electric attack"""
    frames = [
        ("normal", False),
        ("angry", False),
        ("angry", True),
        ("surprised", True),
        ("angry", True),
        ("normal", False),
    ]
    
    for expression, electricity in frames:
        clear_screen()
        print(create_pikachu_frame(expression=expression, electricity=electricity))
        if electricity:
            play_thunder_sound()
        else:
            play_pikachu_sound()
        time.sleep(0.4)

def type_text(text, speed=0.05):
    """Type text with sound effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char not in [' ', '\n']:
            play_beep(1000, 0.01)
        time.sleep(speed)

def main():
    try:
        print(f"{Colors.YELLOW}{Colors.BOLD}")
        print("  ╔════════════════════════════════════════╗")
        print("  ║     PIKACHU ANIMATION EXPERIENCE       ║")
        print("  ╚════════════════════════════════════════╝")
        print(f"{Colors.RESET}")
        time.sleep(1)
        
        # Intro with sound
        clear_screen()
        print(f"{Colors.CYAN}  Initializing Pikachu...{Colors.RESET}")
        for i in range(3):
            play_beep(500 + i * 100, 0.1)
            time.sleep(0.2)
        
        # Pikachu appears
        for _ in range(2):
            clear_screen()
            print(create_pikachu_frame("surprised"))
            play_pikachu_sound()
            time.sleep(0.5)
            
            clear_screen()
            print(create_pikachu_frame("normal"))
            time.sleep(0.3)
        
        # Thunder bolt animation
        print(f"\n{Colors.YELLOW}  ⚡ THUNDER BOLT! ⚡{Colors.RESET}")
        thunder_bolt_animation()
        time.sleep(0.5)
        
        # Pikachu dance
        print(f"\n{Colors.MAGENTA}  🎵 Pikachu is dancing! 🎵{Colors.RESET}")
        time.sleep(1)
        pikachu_dance()
        
        # Electric attack
        print(f"\n{Colors.RED}  ⚡ ELECTRIC ATTACK! ⚡{Colors.RESET}")
        time.sleep(1)
        pikachu_electric_attack()
        
        # Final message
        clear_screen()
        print(create_pikachu_frame("happy"))
        print(f"""
{Colors.GREEN}{Colors.BOLD}
  ╔════════════════════════════════════════╗
  ║                                        ║
  ║    PIKACHU says: "Pika Pika!"          ║
  ║                                        ║
  ║    Thanks for watching!                ║
  ║                                        ║
  ╚════════════════════════════════════════╝
{Colors.RESET}
        """)
        
        # Final sound sequence
        for _ in range(3):
            play_pikachu_sound()
            time.sleep(0.3)
        
    except KeyboardInterrupt:
        clear_screen()
        print(f"""
{Colors.YELLOW}
  Pikachu: "Pika... Pika..." (Goodbye!)
{Colors.RESET}
        """)

if __name__ == "__main__":
    main()