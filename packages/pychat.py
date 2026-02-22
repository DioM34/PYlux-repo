import socket
import threading
import sys
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    CYAN, GREEN, RED, YELLOW, RESET = Fore.CYAN, Fore.GREEN, Fore.RED, Fore.YELLOW, Style.RESET_ALL

    if not args or args[0] != "join":
        print(f"\n{CYAN}═══ PYlux Live Chat ═══{RESET}")
        print(f"Usage: pchat join <ip>")
        return

    # 1. Ask for a specific Chat Display Name
    chat_user = input(f"{YELLOW}Enter Chat Username (Default: {username}): {RESET}").strip()
    if not chat_user:
        chat_user = username

    host = args[1]
    port = 5555
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((host, port))
    except:
        print(f"{RED}Error: Server at {host} is offline.{RESET}")
        return

    def receive():
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message == 'USER_REQ':
                    client.send(chat_user.encode('utf-8'))
                else:
                    # Fix 2 & 3: Clear the current line and move to the start
                    # \033[K is the ANSI escape code to clear from cursor to end of line
                    sys.stdout.write(f"\r\033[K{message}\n")
                    sys.stdout.write(f"{GREEN}{chat_user} > {RESET}")
                    sys.stdout.flush()
            except:
                client.close()
                break

    receive_thread = threading.Thread(target=receive)
    receive_thread.daemon = True
    receive_thread.start()

    print(f"{GREEN}✔ Joined! Type 'exit' to leave.{RESET}")

    while True:
        try:
            msg = input(f"{GREEN}{chat_user} > {RESET}").strip()
            if not msg: continue
            if msg.lower() == 'exit':
                client.close()
                break
            
            # We don't print the message locally anymore. 
            # We wait for the server to send it back to us.
            # This ensures we only see it once and only if it actually sent.
            full_msg = f"{Fore.CYAN}{chat_user}{RESET}: {msg}"
            client.send(full_msg.encode('utf-8'))
            
            # Move cursor up one line and clear it to remove what you just typed
            # so the server's broadcast replaces it cleanly.
            sys.stdout.write("\033[A\033[K")
            sys.stdout.flush()
        except:
            break
