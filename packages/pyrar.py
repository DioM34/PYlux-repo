import os
import zipfile
import tarfile
import lzma
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PyRAR 1.0 - PYlux Compression Utility
    Usage: pyrar [mode] [archive_name] [file/dir]
    """
    CYAN = Fore.CYAN
    GREEN = Fore.GREEN
    RED = Fore.RED
    RESET = Style.RESET_ALL

    def print_help():
        print(f"\n{CYAN}PyRAR v1.0 Help Menu{RESET}")
        print(f"{'-'*30}")
        print(f"Usage: pyrar [action] [archive] [target]")
        print(f"\n{Fore.YELLOW}Actions:{RESET}")
        print(f"  zip      - Create a standard .zip archive")
        print(f"  unzip    - Extract a .zip archive")
        print(f"  xz       - Create a high-compression .xz file (single file)")
        print(f"  unxz     - Extract a .xz file")
        print(f"  help     - Show this menu")
        print(f"\n{Fore.YELLOW}Examples:{RESET}")
        print(f"  pyrar zip backup.zip notes.txt")
        print(f"  pyrar unzip backup.zip .")
        print(f"  pyrar xz data.xz bigfile.txt\n")

    if not args or args[0] in ["help", "-h", "--help"]:
        print_help()
        return

    action = args[0].lower()

    # Ensure we have enough arguments for processing
    if len(args) < 3:
        print(f"{RED}Error: Missing arguments. Use 'pyrar help' for syntax.{RESET}")
        return

    archive_name = args[1]
    target = args[2]
    target_path = os.path.join(current_dir, target)
    archive_path = os.path.join(current_dir, archive_name)

    try:
        # Standard ZIP Compression
        if action == "zip":
            print(f"{CYAN}Creating ZIP archive: {archive_name}...{RESET}")
            with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                if os.path.isdir(target_path):
                    for root, dirs, files in os.walk(target_path):
                        for file in files:
                            zipf.write(os.path.join(root, file), 
                                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(target_path, '..')))
                else:
                    zipf.write(target_path, os.path.basename(target_path))
            print(f"{GREEN}Successfully created {archive_name}{RESET}")

        # Standard ZIP Extraction
        elif action == "unzip":
            print(f"{CYAN}Extracting ZIP: {archive_name}...{RESET}")
            with zipfile.ZipFile(archive_path, 'r') as zipf:
                zipf.extractall(target_path)
            print(f"{GREEN}Extraction complete to {target}{RESET}")

        # XZ High Compression (Single File)
        elif action == "xz":
            print(f"{CYAN}Compressing to XZ (LZMA)...{RESET}")
            with open(target_path, 'rb') as f_in:
                with lzma.open(archive_path, 'wb') as f_out:
                    f_out.write(f_in.read())
            print(f"{GREEN}Successfully created {archive_name}{RESET}")

        # XZ Extraction
        elif action == "unxz":
            print(f"{CYAN}Decompressing XZ file...{RESET}")
            with lzma.open(archive_path, 'rb') as f_in:
                with open(target_path, 'wb') as f_out:
                    f_out.write(f_in.read())
            print(f"{GREEN}Decompressed to {target}{RESET}")

        else:
            print(f"{RED}Unknown action: {action}{RESET}")

    except Exception as e:
        print(f"{RED}PyRAR Error: {e}{RESET}")
