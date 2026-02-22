import os
import socket
import subprocess
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PYlux PyMap - Network Mapper
    Usage: pymap <target_ip>
    """
    CYAN = Fore.CYAN
    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    RESET = Style.RESET_ALL

    if not args:
        print(f"{RED}Usage: pymap <target_ip>{RESET}")
        print(f"{Style.DIM}Example: pymap 127.0.0.1{RESET}")
        return

    target = args[0]

    print(f"\n{CYAN}═══ PYlux PyMap (Network Mapper) ═══{RESET}")
    print(f"Target: {target}")
    print(f"{'-'*35}")
    print(f"1. Use Original Nmap (Recommended - Requires Nmap installed)")
    print(f"2. Use PyMap Python Mapper (Self-made)")
    
    choice = input(f"\n{YELLOW}Select Mode (1/2): {RESET}").strip()

    if choice == "1":
        print(f"{CYAN}Calling system nmap binary...{RESET}\n")
        try:
            # We still call the 'nmap' binary on the host machine
            result = subprocess.run(['nmap', '-F', target], capture_output=True, text=True)
            if result.returncode == 0:
                print(result.stdout)
            else:
                print(f"{RED}Nmap Error: {result.stderr}{RESET}")
        except FileNotFoundError:
            print(f"{RED}Error: Nmap binary not found on host system.{RESET}")
            print(f"{YELLOW}Falling back to PyMap Python version...{RESET}")
            choice = "2" 

    if choice == "2":
        print(f"{CYAN}Starting PyMap Scan (Common Ports)...{RESET}")
        # Scanning key ports similar to your help and search logic
        common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]
        
        found_ports = 0
        for port in common_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5) 
            result = s.connect_ex((target, port))
            
            if result == 0:
                try:
                    service = socket.getservbyname(port, 'tcp')
                except:
                    service = "unknown"
                print(f"{GREEN}[OPEN]{RESET} Port {port:<5} | Service: {service}")
                found_ports += 1
            s.close()

        if found_ports == 0:
            print(f"{YELLOW}No common ports found open on {target}.{RESET}")
        else:
            print(f"\n{GREEN}Scan complete. Found {found_ports} open ports.{RESET}")

    print(f"{CYAN}════════════════════════════════════{RESET}\n")
