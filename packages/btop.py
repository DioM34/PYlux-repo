import os
import time
import psutil
from colorama import Fore, Style

# Initialize history lists for graphs
cpu_history = [0] * 50
ram_history = [0] * 50
net_in_history = [0] * 50
net_out_history = [0] * 50

def run(args, current_dir, username, start_time, is_sudo=False):
    global cpu_history, ram_history, net_in_history, net_out_history

    HIDE_CURSOR = "\033[?25l"
    SHOW_CURSOR = "\033[?25h"
    GOTO_HOME = "\033[H"
    CLEAR_SCREEN = "\033[2J"

    def draw_graph(data, height=4, color=Fore.GREEN):
        """Generates a block graph."""
        graph_lines = []
        for h in range(height, 0, -1):
            line = ""
            threshold = (h / height) * 100
            for value in data[-40:]: # Reduced width to make room for stats
                if value >= threshold: line += "█"
                elif value >= threshold - (100/height/2): line += "▄"
                else: line += " "
            graph_lines.append(f"{color}{line}{Style.RESET_ALL}")
        return graph_lines

    print(CLEAR_SCREEN + HIDE_CURSOR, end="")
    net_old = psutil.net_io_counters()

    try:
        while True:
            print(GOTO_HOME, end="")

            # --- DATA COLLECTION ---
            cpu = psutil.cpu_percent()
            mem = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            net_new = psutil.net_io_counters()

            # Speed calculation
            din = (net_new.bytes_recv - net_old.bytes_recv) / 1024
            dout = (net_new.bytes_sent - net_old.bytes_sent) / 1024
            net_old = net_new

            # Update histories
            cpu_history.append(cpu); ram_history.append(mem.percent)
            net_in_history.append(min(din / 10, 100)); net_out_history.append(min(dout / 10, 100))

            # Keep lists at 50
            cpu_history = cpu_history[-50:]; ram_history = ram_history[-50:]
            net_in_history = net_in_history[-50:]; net_out_history = net_out_history[-50:]

            # --- RENDER CPU BOX ---
            print(f"{Fore.MAGENTA}╔════ CPU TREND ══════════════ STATS ══════════════════════╗")
            graph = draw_graph(cpu_history, height=4, color=Fore.GREEN)
            print(f"║ {graph[0]} ║ Total Usage: {cpu:>5}%       ║")
            print(f"║ {graph[1]} ║ Load Avg:    {os.getloadavg()[0] if hasattr(os, 'getloadavg') else 'N/A'}         ║")
            print(f"║ {graph[2]} ║ Cores:       {psutil.cpu_count()}          ║")
            print(f"║ {graph[3]} ║ Threads:     {len(psutil.pids())}        ║")
            print(f"╚══════════════════════════════════════════════════════════╝")

            # --- RENDER RAM & DISK BOX ---
            print(f"{Fore.MAGENTA}╔════ RAM TREND ══════════════ STORAGE ════════════════════╗")
            graph = draw_graph(ram_history, height=4, color=Fore.CYAN)
            print(f"║ {graph[0]} ║ Used: {mem.used // (1024**2):>6} MB      ║")
            print(f"║ {graph[1]} ║ Free: {mem.available // (1024**2):>6} MB      ║")
            print(f"║ {graph[2]} ║ Disk: {disk.percent:>6}%         ║")
            print(f"║ {graph[3]} ║ {disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB used      ║")
            print(f"╚══════════════════════════════════════════════════════════╝")

            # --- RENDER NETWORK BOX ---
            print(f"{Fore.MAGENTA}╔════ NETWORK (UP/DOWN) ══════ SPEED ══════════════════════╗")
            g_in = draw_graph(net_in_history, height=2, color=Fore.YELLOW)
            g_out = draw_graph(net_out_history, height=2, color=Fore.RED)
            print(f"║ {g_in[0]} ║ Download: {din:>8.1f} KB/s ║")
            print(f"║ {g_in[1]} ║                           ║")
            print(f"║ {g_out[0]} ║ Upload:   {dout:>8.1f} KB/s ║")
            print(f"║ {g_out[1]} ║                           ║")
            print(f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════════╝")

            print(f"\n {Style.DIM}PYlux btop v1.3 | Ctrl+C to Exit{Style.RESET_ALL}")
            time.sleep(0.5)

    except KeyboardInterrupt:
        print(SHOW_CURSOR + CLEAR_SCREEN)
