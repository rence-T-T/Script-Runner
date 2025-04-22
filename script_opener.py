import subprocess
import os

def run_script(script_path, directory):
    """Run a Python script in the specified directory using Pythonw and close the window after."""
    # Convert to absolute path if needed
    script_path = os.path.abspath(script_path)
    directory = os.path.abspath(directory)
    
    # Check if the script and directory exist
    if not os.path.exists(script_path):
        print(f"Error: Script does not exist: {script_path}")
        return False
    
    if not os.path.exists(directory):
        print(f"Error: Directory does not exist: {directory}")
        return False
    
    # Create the command to execute
    cmd_command = f'cd /d "{directory}" && pythonw "{script_path}" && exit'
    
    try:
        # Run the command in a new cmd window that will close when finished
        subprocess.run(["cmd.exe", "/c", cmd_command], check=True)
        print(f"Successfully launched {script_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error executing script {script_path}: {e}")
        return False

def main():
    # Define your scripts and their corresponding directories
    scripts_to_run = [
        {
            "script": "battery_monitor.py",
            "directory": "D:\\PROGRAMMING\\PYTHON\\&my_scripts\\Battery Notification"
        },
        {
            "script": "phone_status.py",
            "directory": "D:\\PROGRAMMING\\PYTHON\\&my_scripts\\Phone Monitor"
        },
        # Add more scripts as needed
    ]
    
    # Run each script in sequence
    for script_info in scripts_to_run:
        success = run_script(script_info["script"], script_info["directory"])
        if not success:
            print(f"Failed to run {script_info['script']}")
    
    print("All scripts have been launched!")

if __name__ == "__main__":
    main()