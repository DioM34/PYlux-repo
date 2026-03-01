import os
import sys
import platform
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PyDownloader v1.1 - Multi-format Media Downloader for PYlux
    Usage: pydownloader youtube [format] [url]
    """
    CYAN = Fore.CYAN
    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    RESET = Style.RESET_ALL

    # Supported formats mapping
    VIDEO_FORMATS = ["mp4", "mkv", "webm"]
    AUDIO_FORMATS = ["mp3", "m4a", "wav", "flac"]

    def print_help():
        print(f"\n{CYAN}═══ PyDownloader v1.1 ═══{RESET}")
        print(f"{Style.DIM}Download media in various formats to /home/Downloads/{RESET}")
        print(f"\n{YELLOW}Usage:{RESET}")
        print(f"  pydownloader youtube [format] <url>")
        print(f"\n{YELLOW}Available Video Formats:{RESET}")
        print(f"  {', '.join(VIDEO_FORMATS)}")
        print(f"\n{YELLOW}Available Audio Formats:{RESET}")
        print(f"  {', '.join(AUDIO_FORMATS)}")
        print(f"\n{YELLOW}Example:{RESET}")
        print(f"  pydownloader youtube mp4 https://youtube.com/example")
        print(f"  pydownloader youtube wav https://youtube.com/example\n")

    if not args or args[0] in ["help", "-h"] or len(args) < 3:
        print_help()
        return

    # Check for yt-dlp dependency
    try:
        import yt_dlp
    except ImportError:
        print(f"{RED}Error: 'yt-dlp' library not found.{RESET}")
        print(f"Try running: {YELLOW}pip install yt-dlp{RESET}")
        return

    provider = args[0].lower()
    requested_format = args[1].lower()
    url = args[2]

    if provider != "youtube":
        print(f"{RED}Error: Only 'youtube' provider is supported currently.{RESET}")
        return

    # Ensure the Downloads directory exists
    download_path = os.path.join("home", "Downloads")
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Base configuration
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': True,
    }

    # Format Logic
    if requested_format in AUDIO_FORMATS:
        print(f"{CYAN}Initializing Audio Extraction ({requested_format.upper()})...{RESET}")
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': requested_format,
                'preferredquality': '192',
            }],
        })
    elif requested_format in VIDEO_FORMATS:
        print(f"{CYAN}Initializing Video Download ({requested_format.upper()})...{RESET}")
        # merge-output-format ensures the final container is what the user asked for
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': requested_format,
        })
    else:
        print(f"{RED}Unsupported format: {requested_format}{RESET}")
        print(f"Use: {', '.join(VIDEO_FORMATS + AUDIO_FORMATS)}")
        return

    # Execution
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"{YELLOW}Downloading: {url}{RESET}")
            ydl.download([url])
        print(f"\n{GREEN}✔ Download complete! Check /home/Downloads/{RESET}")
    except Exception as e:
        print(f"\n{RED}Download Failed: {e}{RESET}")

if __name__ == "__main__":
    # For testing outside PYlux environment
    if len(sys.argv) > 3:
        run(sys.argv[1:], ".", "testuser", 0)
    else:
        print("Usage: python pydownloader.py youtube mp4 <url>")
