import os
import sys
import subprocess
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PyDownloader v1.0 - Media Downloader for PYlux
    Usage: pydownloader youtube [video/sound] [url]
    """
    CYAN = Fore.CYAN
    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    RESET = Style.RESET_ALL

    def print_help():
        print(f"\n{CYAN}═══ PyDownloader v1.0 ═══{RESET}")
        print(f"{Style.DIM}Download media directly to your home directory{RESET}")
        print(f"\n{YELLOW}Usage:{RESET}")
        print(f"  pydownloader youtube video <url> - Download MP4 video")
        print(f"  pydownloader youtube sound <url> - Download MP3 audio")
        print(f"  pydownloader help                - Show this menu")
        print(f"\n{YELLOW}Storage Path:{RESET}")
        print(f"  Files are saved to: /home/Downloads/")
        print(f"\n{YELLOW}Example:{RESET}")
        print(f"  pydownloader youtube sound https://youtu.be/dQw4w9WgXcQ\n")

    if not args or args[0] in ["help", "-h"]:
        print_help()
        return

    # Check for yt-dlp dependency
    try:
        import yt_dlp
    except ImportError:
        print(f"{RED}Error: Dependency 'yt-dlp' not found.{RESET}")
        print(f"{YELLOW}Please run: pip install yt-dlp{RESET}")
        return

    if len(args) < 3:
        print(f"{RED}Error: Missing arguments. Use 'pydownloader help'.{RESET}")
        return

    platform = args[0].lower()
    mode = args[1].lower()
    url = args[2]

    # Ensure the Downloads directory exists
    download_path = os.path.join("home", "Downloads")
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    if platform == "youtube":
        ydl_opts = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'quiet': False,
            'no_warnings': True,
        }

        if mode == "sound":
            print(f"{CYAN}Initializing Audio Extraction...{RESET}")
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        elif mode == "video":
            print(f"{CYAN}Initializing Video Download...{RESET}")
            ydl_opts.update({'format': 'bestvideo+bestaudio/best'})
        else:
            print(f"{RED}Unknown mode: {mode}. Use 'video' or 'sound'.{RESET}")
            return

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"{YELLOW}Downloading: {url}{RESET}")
                ydl.download([url])
            print(f"\n{GREEN}✔ Download complete! Check /home/Downloads/{RESET}")
        except Exception as e:
            print(f"{RED}Download Error: {e}{RESET}")
    else:
        print(f"{RED}Platform '{platform}' not supported yet.{RESET}")
