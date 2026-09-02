import os
import time
import sys
import random
import math
import threading
import platform

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BLACK = '\033[30m'
    ORANGE = '\033[38;5;208m'
    BROWN = '\033[38;5;130m'
    GOLD = '\033[38;5;220m'
    
    # Background colors
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    BG_BLACK = '\033[40m'
    BG_ORANGE = '\033[48;5;208m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_beep(frequency=440, duration=0.1):
    """Play a beep sound"""
    try:
        if platform.system() == 'Windows':
            import winsound
            winsound.Beep(frequency, int(duration * 1000))
        else:
            sys.stdout.write('\a')
            sys.stdout.flush()
            time.sleep(duration)
    except:
        pass

def play_dog_bark():
    """Play dog bark sound sequence"""
    barks = [
        (500, 0.1),
        (400, 0.1),
        (500, 0.1),
        (300, 0.2),
    ]
    for freq, duration in barks:
        play_beep(freq, duration)
        time.sleep(0.05)

def play_epic_music():
    """Play epic music sequence"""
    melody = [
        (440, 0.2), (523, 0.2), (659, 0.2), (880, 0.4),
        (659, 0.2), (880, 0.4), (1047, 0.6),
        (880, 0.2), (659, 0.2), (523, 0.2), (440, 0.4),
    ]
    for freq, duration in melody:
        play_beep(freq, duration)
        time.sleep(0.1)

def create_dog_face(expression="normal", sunglasses=False, crown=False):
    """Create dog face with different expressions"""
    
    faces = {
        "normal": [
            "   / \\__/ \\   ",
            "  (  ' . '  )  ",
            "  (   ___   )  ",
            "   ( (___) )   ",
            "   ( (   ) )   ",
            "    \\_/ \\_/    ",
        ],
        "happy": [
            "   / \\__/ \\   ",
            "  (  ^ . ^  )  ",
            "  (   ___   )  ",
            "   ( (___) )   ",
            "   ( (   ) )   ",
            "    \\_/ \\_/    ",
        ],
        "cool": [
            "   / \\__/ \\   ",
            "  (  ■ . ■  )  ",
            "  (   ___   )  ",
            "   ( (___) )   ",
            "   ( (   ) )   ",
            "    \\_/ \\_/    ",
        ],
        "king": [
            "   ♔ ♔ ♔ ♔ ♔   ",
            "   / \\__/ \\   ",
            "  (  • . •  )  ",
            "  (   ___   )  ",
            "   ( (___) )   ",
            "   ( (   ) )   ",
            "    \\_/ \\_/    ",
        ],
        "super": [
            "   ★ ★ ★ ★ ★   ",
            "   / \\__/ \\   ",
            "  (  ● . ●  )  ",
            "  (   ___   )  ",
            "   ( (___) )   ",
            "   ( (   ) )   ",
            "    \\_/ \\_/    ",
        ],
    }
    
    face = faces.get(expression, faces["normal"])
    
    # Add accessories
    if sunglasses:
        face[1] = "  (  █ . █  )  "
    
    if crown:
        face.insert(0, "   ♛ ♛ ♛ ♛ ♛   ")
    
    return "\n".join(face)

def create_dog_body():
    """Full dog body"""
    return f"""
{Colors.BROWN}      / \\__/ \\
     (  • . •  )
      (   ___   )
       ( (___) )
       ( (   ) )
      /  \\_/ \\_/ \\
     /           \\
    /  |       |  \\
   /   |       |   \\
  /    |_______|    \\
 /                   \\
(_____________________)
{Colors.RESET}
"""

def create_legendary_dog():
    """Legendary dog with effects"""
    return f"""
{Colors.GOLD}{Colors.BOLD}
    ╔═══════════════════════════════╗
    ║   ★ THE LEGENDARY DOG ★      ║
    ║   ★ SON OF RK ★              ║
    ╚═══════════════════════════════╝
{Colors.RESET}
{Colors.BROWN}
      / \\__/ \\
     (  ★ . ★  )
      (   ___   )
       ( (___) )
       ( (   ) )
      /  \\_/ \\_/ \\
     /           \\
    /  |       |  \\
   /   |       |   \\
  /    |_______|    \\
 /                   \\
(_____________________)
{Colors.RESET}
"""

def animate_dog_walking():
    """Dog walking animation"""
    frames = [
        f"""
{Colors.BROWN}   / \\__/ \\
  (  • . •  )  🐾
   (   ___   )
    ( (___) )
    ( (   ) )
   /  \\_/ \\_/ \\
  /           \\
 /             \\
{Colors.RESET}
""",
        f"""
{Colors.BROWN}    / \\__/ \\
   (  • . •  )  🐾
    (   ___   )
     ( (___) )
     ( (   ) )
    /  \\_/ \\_/ \\
   /           \\
  /             \\
{Colors.RESET}
""",
        f"""
{Colors.BROWN}     / \\__/ \\
    (  • . •  )  🐾
     (   ___   )
      ( (___) )
      ( (   ) )
     /  \\_/ \\_/ \\
    /           \\
   /             \\
{Colors.RESET}
""",
    ]
    
    for _ in range(5):
        for frame in frames:
            clear_screen()
            print(frame)
            play_dog_bark()
            time.sleep(0.3)

def dog_dance_party():
    """Dog dancing animation"""
    dance_frames = [
        "normal",
        "happy",
        "cool",
        "happy",
        "super",
        "happy",
        "normal",
        "king",
    ]
    
    for expression in dance_frames:
        clear_screen()
        print(f"{Colors.YELLOW}🎵 DOG DANCE PARTY! 🎵{Colors.RESET}")
        print(create_dog_face(expression=expression))
        print(f"{Colors.CYAN}♪ ♫ ♪ ♫ ♪{Colors.RESET}")
        play_dog_bark()
        time.sleep(0.4)

def epic_intro_animation():
    """Epic introduction animation"""
    clear_screen()
    
    # Fire effect
    fire = f"""
{Colors.RED}{Colors.BOLD}
    🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
   🔥                🔥
  🔥   THE LEGEND    🔥
   🔥                🔥
    🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
{Colors.RESET}
"""
    print(fire)
    play_epic_music()
    time.sleep(2)
    
    # Lightning effect
    lightning = f"""
{Colors.YELLOW}{Colors.BOLD}
        ⚡⚡⚡
       ⚡   ⚡
      ⚡  🐕 ⚡
       ⚡   ⚡
        ⚡⚡⚡
{Colors.RESET}
"""
    clear_screen()
    print(lightning)
    play_beep(880, 0.5)
    time.sleep(1)
    
    # Text reveal
    clear_screen()
    text = f"""
{Colors.GOLD}{Colors.BOLD}
    ╔═══════════════════════════════════════╗
    ║                                       ║
    ║   🐕 DOG - SON OF RK 🐕              ║
    ║                                       ║
    ║   The Ultimate Legendary Canine       ║
    ║                                       ║
    ╚═══════════════════════════════════════╝
{Colors.RESET}
"""
    print(text)
    play_epic_music()
    time.sleep(2)

def dog_superhero_transformation():
    """Dog transforming into superhero"""
    frames = [
        f"""
{Colors.CYAN}
    Transforming...
    
{create_dog_face("normal")}
{Colors.RESET}
""",
        f"""
{Colors.MAGENTA}
    Power Up!
    
    ⚡ {create_dog_face("happy")} ⚡
{Colors.RESET}
""",
        f"""
{Colors.YELLOW}
    MAXIMUM POWER!
    
    ★ {create_dog_face("cool", sunglasses=True)} ★
{Colors.RESET}
""",
        f"""
{Colors.RED}
    SUPER DOG ACTIVATED!
    
    🔥 {create_dog_face("super")} 🔥
{Colors.RESET}
""",
    ]
    
    for frame in frames:
        clear_screen()
        print(frame)
        play_epic_music()
        time.sleep(1)

def flying_dog_animation():
    """Dog flying through space"""
    for i in range(20):
        clear_screen()
        spaces = " " * (i * 2)
        stars = random.randint(3, 10)
        
        # Create star field
        star_field = ""
        for _ in range(stars):
            x = random.randint(0, 60)
            y = random.randint(0, 15)
            star_field += f"\033[{y};{x}H{Colors.YELLOW}*{Colors.RESET}"
        
        print(star_field)
        print(f"{spaces}{Colors.BROWN}  / \\__/ \\{Colors.RESET}")
        print(f"{spaces}{Colors.BROWN} (  ★ . ★  ){Colors.RESET}")
        print(f"{spaces}{Colors.BROWN}  (   ___   ){Colors.RESET}")
        print(f"{spaces}{Colors.BROWN}   ( (___) ){Colors.RESET}")
        print(f"{spaces}{Colors.BROWN}   ( (   ) ){Colors.RESET}")
        print(f"{spaces}{Colors.BROWN}  /  \\_/ \\_/ \\{Colors.RESET}")
        print(f"{spaces}{Colors.BROWN} /           \\{Colors.RESET}")
        print(f"{spaces}{Colors.RED}    🚀{Colors.RESET}")
        
        play_beep(600 + i * 20, 0.1)
        time.sleep(0.2)

def dog_rainbow_effect():
    """Dog with rainbow colors"""
    colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA]
    
    for _ in range(3):
        for color in colors:
            clear_screen()
            print(f"{color}{Colors.BOLD}")
            print("  🌈 RAINBOW DOG 🌈")
            print(create_dog_face("happy"))
            print(f"{Colors.RESET}")
            play_beep(440 + colors.index(color) * 80, 0.1)
            time.sleep(0.2)

def dog_battle_animation():
    """Dog battle scene"""
    clear_screen()
    
    # Enemy appears
    enemy = f"""
{Colors.RED}  👹 ENEMY APPEARS! 👹
    / \\__/ \\
   (  ^ . ^  )
    (   ___   )
     ( (___) )
{Colors.RESET}
"""
    print(enemy)
    play_beep(200, 0.5)
    time.sleep(2)
    
    # Dog enters battle
    clear_screen()
    battle_scene = f"""
{Colors.RED}  👹 ENEMY 👹              {Colors.BROWN}🐕 DOG 🐕{Colors.RESET}
{Colors.RED}    / \\__/ \\{Colors.RESET}              {Colors.BROWN}    / \\__/ \\{Colors.RESET}
{Colors.RED}   (  ^ . ^  ){Colors.RESET}             {Colors.BROWN}   (  • . •  ){Colors.RESET}
{Colors.RED}    (   ___   ){Colors.RESET}             {Colors.BROWN}    (   ___   ){Colors.RESET}
{Colors.RED}     ( (___) ){Colors.RESET}             {Colors.BROWN}     ( (___) ){Colors.RESET}
"""
    print(battle_scene)
    play_dog_bark()
    time.sleep(1)
    
    # Attack animation
    for i in range(3):
        clear_screen()
        attack = f"""
{Colors.YELLOW}        ⚡ ATTACK! ⚡
{Colors.RED}  👹 ENEMY 👹              {Colors.BROWN}🐕 DOG 🐕{Colors.RESET}
{Colors.RED}    / \\__/ \\{Colors.RESET}              {Colors.BROWN}    / \\__/ \\{Colors.RESET}
{Colors.RED}   (  X . X  ){Colors.RESET}            {Colors.BROWN}   (  ★ . ★  ){Colors.RESET}
{Colors.RED}    (   ___   ){Colors.RESET}             {Colors.BROWN}    (   ___   ){Colors.RESET}
{Colors.RED}     ( (___) ){Colors.RESET}             {Colors.BROWN}     ( (___) ){Colors.RESET}
{Colors.RESET}
"""
        print(attack)
        play_beep(800, 0.3)
        time.sleep(0.5)
    
    # Victory
    clear_screen()
    victory = f"""
{Colors.GREEN}{Colors.BOLD}
    🎉 VICTORY! 🎉
    
{Colors.BROWN}    / \\__/ \\
   (  ★ . ★  )
    (   ___   )
     ( (___) )
     ( (   ) )
    /  \\_/ \\_/ \\
   /           \\
  /             \\
{Colors.RESET}
"""
    print(victory)
    play_epic_music()

def particle_effects():
    """Particle effects around dog"""
    particles = ['✨', '⭐', '🌟', '💫', '⚡', '🔥', '💛']
    
    for _ in range(10):
        clear_screen()
        print(create_dog_face("super"))
        
        # Random particles
        for _ in range(8):
            x = random.randint(0, 50)
            y = random.randint(0, 10)
            particle = random.choice(particles)
            print(f"\033[{y};{x}H{Colors.YELLOW}{particle}{Colors.RESET}")
        
        play_beep(700, 0.05)
        time.sleep(0.2)

def main():
    try:
        # Title screen
        clear_screen()
        print(f"""
{Colors.GOLD}{Colors.BOLD}
    ╔═══════════════════════════════════════════════╗
    ║                                               ║
    ║   🐕 DOG - SON OF RK 🐕                      ║
    ║                                               ║
    ║   The Ultimate Python Animation               ║
    ║                                               ║
    ║   Press ENTER to begin the adventure!         ║
    ║                                               ║
    ╚═══════════════════════════════════════════════╝
{Colors.RESET}
        """)
        input()
        
        # Epic intro
        epic_intro_animation()
        
        # Dog walking
        print(f"\n{Colors.CYAN}  🐕 Dog is walking...{Colors.RESET}")
        animate_dog_walking()
        
        # Dance party
        dog_dance_party()
        
        # Superhero transformation
        print(f"\n{Colors.MAGENTA}  ⚡ Transformation sequence! ⚡{Colors.RESET}")
        dog_superhero_transformation()
        
        # Flying animation
        print(f"\n{Colors.CYAN}  🚀 Flying through space! 🚀{Colors.RESET}")
        flying_dog_animation()
        
        # Rainbow effect
        dog_rainbow_effect()
        
        # Battle scene
        print(f"\n{Colors.RED}  ⚔️ Battle time! ⚔️{Colors.RESET}")
        dog_battle_animation()
        
        # Particle effects
        particle_effects()
        
        # Legendary dog reveal
        clear_screen()
        print(create_legendary_dog())
        print(f"""
{Colors.GOLD}{Colors.BOLD}
    ╔═══════════════════════════════════════════════╗
    ║                                               ║
    ║   🎊 CONGRATULATIONS! 🎊                     ║
    ║                                               ║
    ║   You have witnessed the legend of            ║
    ║   DOG - SON OF RK!                           ║
    ║                                               ║
    ║   The most powerful canine in existence!      ║
    ║                                               ║
    ╚═══════════════════════════════════════════════╝
{Colors.RESET}
        """)
        
        # Final sound
        play_epic_music()
        
        # Ending animation
        for i in range(3):
            sys.stdout.write(f"\r{Colors.YELLOW}  The legend continues... {'🐕' * (i+1)}{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(0.5)
        print("\n")
        
    except KeyboardInterrupt:
        clear_screen()
        print(f"""
{Colors.YELLOW}
    🐕 Dog says: "Woof! (Goodbye!)"
    
    Thanks for watching!
{Colors.RESET}
        """)

if __name__ == "__main__":
    main()

    