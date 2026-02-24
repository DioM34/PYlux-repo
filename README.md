# 🐧 PYlux

**PYlux** is a Python-based sandbox environment that simulates a Linux-like experience. It is 100% open-source, lightweight, and free for everyone.

<img src="https://via.placeholder.com/800x400.png?text=PYlux+Terminal+Preview" alt="PYlux Terminal Preview" width="100%">

> [!IMPORTANT]
> **DISCLAIMER:** This project was developed through "vibecoding" using AI tools like Gemini and ChatGPT. If you encounter bugs, please contribute by opening an issue or a pull request!

---

## ✨ Features

* **📦 The `py` Package Manager** – Easily manage packages found in the `/packages` folder of this repository.
* **📂 Real Directory Logic** – Experience a system structured like Linux with `/bin`, `/core`, and `/packages`.
* **🎨 Customizable MOTD** – Personalize your startup experience by editing `motd.txt`.
* **🛡️ Sandbox Mode** – Stay within your PYlux environment without accidentally exiting to your host system.
* **🚀 Active Package Support** – The library of available packages is constantly expanding.
* **🍃 Resource Efficient** – Significantly lighter on hardware than running a full Virtual Machine (VM).
* **🤝 Community Driven** – Built on community requests and ideas.

---

## 📂 System Structure

PYlux mimics a standard Unix-like hierarchy to keep system files and user scripts organized:

* **`/bin`**: Contains all core system commands and binaries.
* **`/core`**: The "heart" of the system. Contains boot files, login logic, and user creation scripts.
* **`/packages`**: The landing zone for all external tools installed via the `py` manager.
* **`motd.txt`**: Edit this file to change the ASCII logo and welcome message shown at boot.

---

## ⌨️ Core Commands

Once inside the PYlux terminal, you can use these built-in commands located in `/bin`:

| Command       Description 
| :--- |        :--- |
| `help`             | Displays the help menu and available commands. |
| `ls`               | Lists files and folders in your current directory. |
| `cd <dir>`         | Change your current working directory. |
| `mkdir <name>`     | Create a new directory within the sandbox. |
| `py install <pkg>` | Download and install a package to the `/packages` folder. |
| `whoami`           | Show the currently logged-in user. |
| `clear`            | Clears the terminal screen for a fresh start. |

---

## 🛠️ Dependencies

To run PYlux, ensure you meet the following requirements:

* **Python:** `3.13+`
* **OS:** Windows 10/11 or Linux
* **Optional:** `pip` (for extended package support)

---

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/DioM34/PYlux.git](https://github.com/DioM34/PYlux.git)

2. **Navigate to the folder:**
   ```bash
   cd PYlux

3. **Run the simulation:**
   ```bash
   python main.py

> [!TIP]
> On your fist boot, the system will trigger the **User Creation Skript** located in the `/core` directory. Follow the promts to set up your credentials!

---

## 💡 Customization

**Changing the welcome Screen**
Open `motd.txt` in any editor. You can add your own **ASCII Art** or custom instructions. This will be displayed every time the `main.py` is executed, right before the command promt appears.

## ❤️ Support & Contributing

If you enjoy using PYlux, please consider giving this project a ⭐ Star. It motivates me to keep updating and improving the code!

Suggestions: Open a Pull Request with your ideas.

Bugs: Report issues via the GitHub Issues tab.

Feedback: I actively listen to community requests!

Made with ❤️ and AI.
