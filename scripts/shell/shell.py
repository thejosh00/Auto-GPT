import subprocess
import os

def execute_bash_command(command, file_path):
    # Check if the specified file path exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Path '{file_path}' does not exist.")

    # Change to the specified directory
    os.chdir(file_path)

    # Execute the command using bash
    try:
        result = subprocess.run(["bash", "-c", command], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("An error occurred while executing the command.")
        return e.stderr
