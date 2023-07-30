import os
import winreg

def create_folders():
    num_folders = int(input("Enter the number of folders to create: "))

    if num_folders <= 0:
        print("Number of folders should be greater than 0.")
        return

    for i in range(num_folders):
        folder_name = input(f"Enter the name for folder {i + 1}: ")
        os.makedirs(folder_name, exist_ok=True)
        print(f"Folder '{folder_name}' created.")

if __name__ == "__main__":
    create_folders()

# Update the following two paths to match your Python installation and script location.
python_exe_path = r"C:\\path\\to\\python.exe"
script_path = r"C:\\path\\to\\your\\script.py"


command = f'"{python_exe_path}" "{script_path}"'

# Create a registry key for the context menu integration.Feel free to change the name.
key = winreg.CreateKey(
    winreg.HKEY_CLASSES_ROOT,
    r"Directory\\Background\\shell\\Create Multiple Folders\\command",
)

# Set the command value for the registry key.
winreg.SetValue(key, "", winreg.REG_SZ, command)
