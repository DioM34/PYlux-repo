import socket
import threading
import sys
import os
from colorama import Fore, Style

def run(args, current_dir, username, start_time, is_sudo=False):
    """
    PChat Live - Ephemeral Community Chat
    Usage: pchat join <server_ip>
    """
    CYAN = Fore.CYAN
    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL

    if not args or args[0] != "join":
        print(f"\n{CYAN}═══ PYlux Live Chat (Temporary) ═══{RESET}")
        print(f"{Style.DIM}Privacy: No logs are saved to disk.{RESET}")
        print(f"\n{YELLOW}Usage:{RESET}")
        print(f"  pchat join <ip_address>")
        print(f"\n{YELLOW}Example:{RESET}")
        print(f"  pchat join 127.0.0.1  {Style.DIM}(For local testing){RESET}")
        return

    # Server details
    host = args[1]
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Attempt to connect to the server
        client.connect((host, port))
    except Exception as e:
        print(f"{RED}Error: Could not connect to chat server at {host}.{RESET}")
        print(f"{Style.DIM}Make sure chat_server.py is running!{RESET}")
        return

    def receive():
        """Handles incoming messages from the server."""
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message == 'USER_REQ':
                    # Send the PYlux username automatically
                    client.send(username.encode('utf-8'))
                else:
                    # Clear current line and print the received message
                    sys.stdout.write(f"\r{message}\n")
                    # Re-print the prompt for the user
                    sys.stdout.write(f"{GREEN}{username} > {RESET}")
                    sys.stdout.flush()
            except:
                print(f"\n{RED}[!] Connection lost.{RESET}")
                client.close()
                break

    # Start the background thread for receiving messages
    receive_thread = threading.Thread(target=receive)
    receive_thread.daemon = True 
    receive_thread.start()

    print(f"{GREEN}✔ Connected to PYlux Chat!{RESET}")
    print(f"{Style.DIM}Type 'exit' to leave the room.{RESET}\n")

    # Main loop for sending messages
    while True:
        try:
            msg = input(f"{GREEN}{username} > {RESET}").strip()
            
            if not msg:
                continue

            if msg.lower() == 'exit':
                client.close()
                print(f"{YELLOW}Logged out of chat.{RESET}")
                break

            # Format the message: [Username]: Message
            full_msg = f"{Fore.CYAN}{username}{RESET}: {msg}"
            client.send(full_msg.encode('utf-8'))
        except EOFError:
            break
        except Exception as e:
            print(f"{RED}Send Error: {e}{RESET}")
            break
