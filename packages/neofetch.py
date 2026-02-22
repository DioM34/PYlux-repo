import os
import platform
import sys
from datetime import datetime
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    # Colors
    PURPLE = Fore.MAGENTA + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT
    RESET = Style.RESET_ALL

    # 1. Calculate Uptime
    delta = datetime.now() - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    uptime_str = f"{hours}h {minutes}m {seconds}s"

    # 2. Gather System Info
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_count = 0
    total_size = 0
    for root, dirs, files in os.walk("."):
        file_count += len(files)
        for f in files:
            fp = os.path.join(root, f)
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)

    kb_size = round(total_size / 1024, 2)

    # 3. Requested Python ASCII Logo
    logo_lines = [
        "       ⢀⣤⣴⣶⣶⣶⣶⣶⣦⣄         ",
        "      ⢀⣾⠟⠛⢿⣿⣿⣿⣿⣿⣿⣷       ",
        "      ⢸⣿⣄⣀⣼⣿⣿⣿⣿⣿⣿⣿⠀⢀⣀⣀⣀⡀  ",
        "      ⠈⠉⠉⠉⠉⠉⠉⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣦ ",
        " ⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⡇",
        "⢰⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠋⠀⣼⣿⣿⣿⣿⣿⡇",
        "⢸⣿⣿⣿⣿⣿⡿⠉⢀⣠⣤⣤⣤⣤⣤⣤⣤⣴⣾⣿⣿⣿⣿⣿⣿⡇",
        "⢸⣿⣿⣿⣿⣿⡇⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿ ",
        "⠘⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠁  ",
        " ⠈⠛⠻⠿⠿⠇⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⡇      ",
        "        ⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣿⠇     ",
        "        ⠘⢿⣿⣿⣿⣿⣿⣿⣿⡿⠋      "
    ]

    # 4. System Info Data (Purple labels, White values)
    info_lines = [
        f"{PURPLE}{username}{WHITE}@{PURPLE}PYlux",
        f"{WHITE}-----------------------",
        f"{PURPLE}OS: {WHITE}PYlux OS 1.4.2",
        f"{PURPLE}Kernel: {WHITE}Python {platform.python_version()}",
        f"{PURPLE}Uptime: {WHITE}{uptime_str}",
        f"{PURPLE}Packages: {WHITE}{file_count} (files)",
        f"{PURPLE}Memory: {WHITE}{kb_size} KB (virtual)",
        f"{PURPLE}Host: {WHITE}{platform.system()}",
        f"{PURPLE}Root: {WHITE}/{current_dir}",
        f"{PURPLE}Local Time: {WHITE}{current_time}"
    ]

    # 5. Render side-by-side
    print("")
    max_lines = max(len(logo_lines), len(info_lines))
    for i in range(max_lines):
        logo_part = logo_lines[i] if i < len(logo_lines) else "                                        "
        info_part = info_lines[i] if i < len(info_lines) else ""
        # Adjusting space to account for wide-character ASCII
        print(f" {logo_part}   {info_part}")

    # 6. Color Palette
    palette = "".join([
        Fore.BLACK + "██", Fore.RED + "██", Fore.GREEN + "██",
        Fore.YELLOW + "██", Fore.BLUE + "██", Fore.MAGENTA + "██",
        Fore.CYAN + "██", Fore.WHITE + "██"
    ])
    print("\n" + " " * 20 + palette + RESET + "\n")
