import os
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PYlux File Explorer 1.0
    Usage: explorer [path]
    """
    # Use current directory if no path is provided
    target_dir = args[0] if args else current_dir
    
    # Visual Constants
    FOLDER_ICON = Fore.CYAN + "📁 "
    FILE_ICON = Fore.WHITE + "📄 "
    HEADER = Fore.MAGENTA + Style.BRIGHT
    RESET = Style.RESET_ALL

    print(f"\n{HEADER}--- PYlux Explorer: {target_dir} ---{RESET}")

    try:
        if not os.path.exists(target_dir):
            print(f"{Fore.RED}Error: Path '{target_dir}' does not exist.{RESET}")
            return

        # Get and sort items: Folders first, then files
        items = os.listdir(target_dir)
        folders = sorted([f for f in items if os.path.isdir(os.path.join(target_dir, f))])
        files = sorted([f for f in items if os.path.isfile(os.path.join(target_dir, f))])

        print(f"{'Type':<6} {'Name':<20} {'Size':<10}")
        print("-" * 40)

        # List Folders
        for folder in folders:
            print(f"{FOLDER_ICON:<5} {Fore.CYAN}{folder:<20}{RESET} {'DIR':<10}")

        # List Files
        for file in files:
            file_path = os.path.join(target_dir, file)
            size_bytes = os.path.getsize(file_path)
            
            # Format size (Bytes/KB)
            if size_bytes < 1024:
                size_str = f"{size_bytes} B"
            else:
                size_str = f"{size_bytes / 1024:.1f} KB"
                
            print(f"{FILE_ICON:<5} {Fore.WHITE}{file:<20}{RESET} {size_str:<10}")

        print(f"{HEADER}--------------------------------------{RESET}\n")

    except PermissionError:
        print(f"{Fore.RED}Error: Permission Denied.{RESET}")
    except Exception as e:
        print(f"{Fore.RED}Explorer Error: {e}{RESET}")
