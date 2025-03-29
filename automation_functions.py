# automation_functions.py

import os
import webbrowser
import psutil
import datetime
import platform
import socket
import shutil
import pyautogui

# 🚀 Existing Functions

def open_chrome():
    """Opens Google Chrome browser."""
    webbrowser.open("https://www.google.com")

def open_calculator():
    """Opens the calculator application."""
    if platform.system() == "Windows":
        os.system("calc")
    elif platform.system() == "Linux":
        os.system("gnome-calculator")

def get_cpu_usage():
    """Returns the current CPU usage percentage."""
    return f"CPU Usage: {psutil.cpu_percent(interval=1)}%"

def get_current_time():
    """Returns the current system date and time."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def execute_command(command):
    """Executes a shell command and returns the output."""
    return os.popen(command).read()


# 🔥 New Functions to Enhance Automation

def get_ram_usage():
    """Returns the system's RAM usage percentage."""
    return f"RAM Usage: {psutil.virtual_memory().percent}%"

def get_ip_address():
    """Returns the local IP address of the system."""
    return socket.gethostbyname(socket.gethostname())

def get_disk_space():
    """Returns available disk space in GB."""
    total, used, free = shutil.disk_usage("/")
    return f"Disk Space - Total: {total // (2**30)}GB, Used: {used // (2**30)}GB, Free: {free // (2**30)}GB"

def take_screenshot():
    """Takes a screenshot and saves it as 'screenshot.png'."""
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    return "Screenshot saved as 'screenshot.png'"

def shutdown_system():
    """Shuts down the system after a short delay."""
    if platform.system() == "Windows":
        os.system("shutdown /s /t 10")  # Shutdown in 10 seconds
    elif platform.system() == "Linux":
        os.system("shutdown -h 10")
    return "System will shut down in 10 seconds."

def restart_system():
    """Restarts the system after a short delay."""
    if platform.system() == "Windows":
        os.system("shutdown /r /t 10")  # Restart in 10 seconds
    elif platform.system() == "Linux":
        os.system("shutdown -r 10")
    return "System will restart in 10 seconds."

def open_notepad():
    """Opens Notepad application (Windows only)."""
    if platform.system() == "Windows":
        os.system("notepad")
    return "Opened Notepad."

def open_file_explorer():
    """Opens File Explorer (Windows only)."""
    if platform.system() == "Windows":
        os.system("explorer")
    return "Opened File Explorer."
