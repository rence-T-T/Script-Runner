import os
import subprocess
import tempfile

def run_script(script_name, directory, show_window=True):
    """
    Run a Python script in the specified directory using a VBScript wrapper.
    
    Args:
        script_name: Name of the Python script to run
        directory: Directory containing the script
        show_window: Whether to show the window (True for GUI apps, False for background scripts)
    """
    # Convert to absolute paths
    directory = os.path.abspath(directory)
    script_path = os.path.join(directory, script_name)
    
    # Check if the directory and script exist
    if not os.path.exists(directory):
        print(f"Error: Directory does not exist: {directory}")
        return False
    
    if not os.path.exists(script_path):
        print(f"Error: Script does not exist: {script_path}")
        return False
    
    try:
        # Set window visibility (1 = normal window, 0 = hidden)
        window_style = 1 if show_window else 0
        
        # Create a temporary VBS file that will run our Python script
        fd, vbs_path = tempfile.mkstemp(suffix=".vbs")
        with os.fdopen(fd, 'w') as f:
            f.write(f'''
Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "{directory.replace('\\', '\\\\')}"
WshShell.Run "pythonw {script_name}", {window_style}, False
''')
        
        # Run the VBS file (which will run the Python script in the correct directory)
        subprocess.run(["wscript.exe", vbs_path], check=True)
        
        # Clean up the temporary file
        os.unlink(vbs_path)
        
        print(f"Successfully launched {script_name} in {directory}")
        return True
    except Exception as e:
        print(f"Error executing script {script_name}: {e}")
        return False

def main():
    # Define your scripts and their corresponding directories
    scripts_to_run = [
        {
            "script": "battery_monitor.py",  # Your GUI app
            "directory": r"D:\PROGRAMMING\PYTHON\&my_scripts\Battery Notification",  # Directory path
            "is_gui": True  # This is a GUI app, so show the window
        },
        {
            "script": "phone_status.py.py",  # Your GUI app
            "directory": r"D:\PROGRAMMING\PYTHON\&my_scripts\Phone Monitor",  # Directory path
            "is_gui": True  # This is a GUI app, so show the window
        },
        # Add more scripts as needed, e.g.:
        # {
        #     "script": "another_script.py",
        #     "directory": r"D:\PROGRAMMING\PYTHON\&my_scripts\Another Directory",
        #     "is_gui": False  # Background script, hide the window
        # }
    ]
    
    # Run each script in sequence
    for script_info in scripts_to_run:
        success = run_script(
            script_info["script"], 
            script_info["directory"],
            show_window=script_info.get("is_gui", False)  # Default to hidden if not specified
        )
        if not success:
            print(f"Failed to run {script_info['script']}")
    
    print("All scripts have been launched!")

if __name__ == "__main__":
    main()