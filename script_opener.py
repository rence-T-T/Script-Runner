import os
import subprocess
import tempfile

def run_script(script_name, directory):
    """Run a Python script in the specified directory using a VBScript wrapper."""
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
        # Create a temporary VBS file that will run our Python script
        fd, vbs_path = tempfile.mkstemp(suffix=".vbs")
        with os.fdopen(fd, 'w') as f:
            f.write(f'''
Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "{directory.replace('\\', '\\\\')}"
WshShell.Run "pythonw {script_name}", 0, False
''')
        
        # Run the VBS file (which will run the Python script in the correct directory)
        subprocess.run(["wscript.exe", vbs_path], check=True)
        
        # Clean up the temporary file
        os.unlink(vbs_path)
        
        print(f"Successfully launched {script_name}")
        return True
    except Exception as e:
        print(f"Error executing script {script_name}: {e}")
        return False

def main():
    # Define your scripts and their corresponding directories
    scripts_to_run = [
        {
            "script": "battery_monitor.py",  # Just the script name
            "directory": r"D:\PROGRAMMING\PYTHON\&my_scripts\Battery Notification"  # The full directory path
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