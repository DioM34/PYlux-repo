import os
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    Displays the entire virtual OS structure in a tree format.
    Usage: tree [directory]
    """
    # Default to root (current project folder) if no path is given
    target = args[0] if args else "."

    # Security: Prevent escaping the sandbox
    target_path = os.path.normpath(os.path.join(current_dir, target))
    if target_path.startswith(".."):
        print(f"{Fore.RED}Error: Access Denied.")
        return

    if not os.path.exists(target_path):
        print(f"{Fore.RED}tree: {target}: No such directory")
        return

    print(f"{Fore.CYAN}{Style.BRIGHT}{target_path}")
    render_tree(target_path, "")

def render_tree(path, prefix):
    """Recursively draws the tree branches."""
    try:
        # UPDATED FILTER: Hides hidden files AND __pycache__ folders
        items = [
            i for i in os.listdir(path)
            if not i.startswith('.') and i != "__pycache__"
        ]
        items.sort()
    except PermissionError:
        print(f"{prefix}└── {Fore.RED}[Permission Denied]")
        return

    for index, item in enumerate(items):
        item_path = os.path.join(path, item)
        is_last = (index == len(items) - 1)

        # Select the correct branch character
        connector = "└── " if is_last else "├── "

        if os.path.isdir(item_path):
            # Print directory in Cyan
            print(f"{Fore.WHITE}{prefix}{connector}{Fore.CYAN}{Style.BRIGHT}{item}/")
            # Calculate the prefix for the next depth level
            extension = "    " if is_last else "│   "
            render_tree(item_path, prefix + extension)
        else:
            # Print file in White
            print(f"{Fore.WHITE}{prefix}{connector}{item}")
