# model.py

from automation_functions import (
    open_chrome, open_calculator, get_cpu_usage, get_current_time, execute_command,
    get_ram_usage, get_ip_address, get_disk_space, take_screenshot,
    shutdown_system, restart_system, open_notepad, open_file_explorer
)

# Mapping function names to actual function objects
FUNCTIONS = {
    "open_chrome": open_chrome,
    "open_calculator": open_calculator,
    "get_cpu_usage": get_cpu_usage,
    "get_current_time": get_current_time,
    "execute_command": execute_command,
    "get_ram_usage": get_ram_usage,
    "get_ip_address": get_ip_address,
    "get_disk_space": get_disk_space,
    "take_screenshot": take_screenshot,
    "shutdown_system": shutdown_system,
    "restart_system": restart_system,
    "open_notepad": open_notepad,
    "open_file_explorer": open_file_explorer
}

def list_available_functions():
    """Returns a list of available functions with their descriptions."""
    return {"available_functions": list(FUNCTIONS.keys())}

def execute_function(function_name: str, **kwargs):
    """Executes the requested function dynamically."""
    if function_name in FUNCTIONS:
        return FUNCTIONS[function_name](**kwargs)
    else:
        raise ValueError(f"Function '{function_name}' not found.")

