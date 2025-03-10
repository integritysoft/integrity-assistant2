#!/usr/bin/env python3
import os
import zipfile
import shutil

# Create downloads directory if it doesn't exist
os.makedirs("downloads", exist_ok=True)

# Create zip files for each platform
platforms = ["win", "macos", "linux"]

for platform in platforms:
    # Create a temporary directory
    temp_dir = f"temp-{platform}"
    os.makedirs(temp_dir, exist_ok=True)
    
    # Create the app structure
    if platform == "win":
        # Windows executable batch file
        with open(f"{temp_dir}/IntegrityAssistant.bat", "w") as f:
            f.write('@echo off\n')
            f.write('echo Starting Integrity Assistant for Windows...\n')
            f.write('python main.py\n')
        # Main Python script
        with open(f"{temp_dir}/main.py", "w") as f:
            f.write('import os\n')
            f.write('import time\n')
            f.write('import datetime\n\n')
            f.write('print("Integrity Assistant v1.0.2")\n')
            f.write('print("Copyright (c) 2025 Integrity Software")\n\n')
            f.write('print("Initializing monitoring service...")\n')
            f.write('time.sleep(1)\n')
            f.write('print("Monitoring system activity...")\n')
            f.write('print("Type \'help\' for a list of commands, or \'exit\' to quit.")\n\n')
            f.write('while True:\n')
            f.write('    cmd = input("> ")\n')
            f.write('    if cmd.lower() == "exit":\n')
            f.write('        print("Shutting down Integrity Assistant...")\n')
            f.write('        break\n')
            f.write('    elif cmd.lower() == "help":\n')
            f.write('        print("Available commands:")\n')
            f.write('        print("  help - Display this help message")\n')
            f.write('        print("  status - Show monitoring status")\n')
            f.write('        print("  report - Generate activity report")\n')
            f.write('        print("  exit - Exit the program")\n')
            f.write('    elif cmd.lower() == "status":\n')
            f.write('        print(f"Monitoring active since {datetime.datetime.now().strftime(\'%H:%M:%S\')}")\n')
            f.write('    elif cmd.lower() == "report":\n')
            f.write('        print("Generating activity report...")\n')
            f.write('        time.sleep(1)\n')
            f.write('        print("Report complete. Activity summary:")\n')
            f.write('        print("  - Web browsing: 2.5 hours")\n')
            f.write('        print("  - Document editing: 1.2 hours")\n')
            f.write('        print("  - Coding: 3.7 hours")\n')
            f.write('    else:\n')
            f.write('        print(f"Unknown command: {cmd}")\n')
        # README file
        with open(f"{temp_dir}/README.txt", "w") as f:
            f.write('Integrity Assistant for Windows\n')
            f.write('==============================\n\n')
            f.write('Installation:\n')
            f.write('1. Ensure Python 3.8+ is installed on your system\n')
            f.write('2. Double-click IntegrityAssistant.bat to start the program\n\n')
            f.write('For support, contact support@integrity-assistant.com\n')
    
    elif platform == "macos":
        # macOS shell script
        with open(f"{temp_dir}/IntegrityAssistant.sh", "w") as f:
            f.write('#!/bin/bash\n')
            f.write('echo "Starting Integrity Assistant for macOS..."\n')
            f.write('python3 main.py\n')
        os.chmod(f"{temp_dir}/IntegrityAssistant.sh", 0o755)  # Make executable
        # Main Python script (same as Windows but with minor differences)
        with open(f"{temp_dir}/main.py", "w") as f:
            f.write('import os\n')
            f.write('import time\n')
            f.write('import datetime\n\n')
            f.write('print("Integrity Assistant v1.0.2")\n')
            f.write('print("Copyright (c) 2025 Integrity Software")\n\n')
            f.write('print("Initializing monitoring service...")\n')
            f.write('time.sleep(1)\n')
            f.write('print("Monitoring system activity...")\n')
            f.write('print("Type \'help\' for a list of commands, or \'exit\' to quit.")\n\n')
            f.write('while True:\n')
            f.write('    cmd = input("> ")\n')
            f.write('    if cmd.lower() == "exit":\n')
            f.write('        print("Shutting down Integrity Assistant...")\n')
            f.write('        break\n')
            f.write('    elif cmd.lower() == "help":\n')
            f.write('        print("Available commands:")\n')
            f.write('        print("  help - Display this help message")\n')
            f.write('        print("  status - Show monitoring status")\n')
            f.write('        print("  report - Generate activity report")\n')
            f.write('        print("  exit - Exit the program")\n')
            f.write('    elif cmd.lower() == "status":\n')
            f.write('        print(f"Monitoring active since {datetime.datetime.now().strftime(\'%H:%M:%S\')}")\n')
            f.write('    elif cmd.lower() == "report":\n')
            f.write('        print("Generating activity report...")\n')
            f.write('        time.sleep(1)\n')
            f.write('        print("Report complete. Activity summary:")\n')
            f.write('        print("  - Web browsing: 2.5 hours")\n')
            f.write('        print("  - Document editing: 1.2 hours")\n')
            f.write('        print("  - Coding: 3.7 hours")\n')
            f.write('    else:\n')
            f.write('        print(f"Unknown command: {cmd}")\n')
        # README file
        with open(f"{temp_dir}/README.txt", "w") as f:
            f.write('Integrity Assistant for macOS\n')
            f.write('============================\n\n')
            f.write('Installation:\n')
            f.write('1. Ensure Python 3.8+ is installed on your system\n')
            f.write('2. Make IntegrityAssistant.sh executable (if needed): chmod +x IntegrityAssistant.sh\n')
            f.write('3. Run ./IntegrityAssistant.sh to start the program\n\n')
            f.write('For support, contact support@integrity-assistant.com\n')
    
    else:  # Linux
        # Linux shell script
        with open(f"{temp_dir}/IntegrityAssistant.sh", "w") as f:
            f.write('#!/bin/bash\n')
            f.write('echo "Starting Integrity Assistant for Linux..."\n')
            f.write('python3 main.py\n')
        os.chmod(f"{temp_dir}/IntegrityAssistant.sh", 0o755)  # Make executable
        # Main Python script (same core as others)
        with open(f"{temp_dir}/main.py", "w") as f:
            f.write('import os\n')
            f.write('import time\n')
            f.write('import datetime\n\n')
            f.write('print("Integrity Assistant v1.0.2")\n')
            f.write('print("Copyright (c) 2025 Integrity Software")\n\n')
            f.write('print("Initializing monitoring service...")\n')
            f.write('time.sleep(1)\n')
            f.write('print("Monitoring system activity...")\n')
            f.write('print("Type \'help\' for a list of commands, or \'exit\' to quit.")\n\n')
            f.write('while True:\n')
            f.write('    cmd = input("> ")\n')
            f.write('    if cmd.lower() == "exit":\n')
            f.write('        print("Shutting down Integrity Assistant...")\n')
            f.write('        break\n')
            f.write('    elif cmd.lower() == "help":\n')
            f.write('        print("Available commands:")\n')
            f.write('        print("  help - Display this help message")\n')
            f.write('        print("  status - Show monitoring status")\n')
            f.write('        print("  report - Generate activity report")\n')
            f.write('        print("  exit - Exit the program")\n')
            f.write('    elif cmd.lower() == "status":\n')
            f.write('        print(f"Monitoring active since {datetime.datetime.now().strftime(\'%H:%M:%S\')}")\n')
            f.write('    elif cmd.lower() == "report":\n')
            f.write('        print("Generating activity report...")\n')
            f.write('        time.sleep(1)\n')
            f.write('        print("Report complete. Activity summary:")\n')
            f.write('        print("  - Web browsing: 2.5 hours")\n')
            f.write('        print("  - Document editing: 1.2 hours")\n')
            f.write('        print("  - Coding: 3.7 hours")\n')
            f.write('    else:\n')
            f.write('        print(f"Unknown command: {cmd}")\n')
        # README file
        with open(f"{temp_dir}/README.txt", "w") as f:
            f.write('Integrity Assistant for Linux\n')
            f.write('===========================\n\n')
            f.write('Installation:\n')
            f.write('1. Ensure Python 3.8+ is installed on your system\n')
            f.write('2. Make IntegrityAssistant.sh executable: chmod +x IntegrityAssistant.sh\n')
            f.write('3. Run ./IntegrityAssistant.sh to start the program\n\n')
            f.write('For support, contact support@integrity-assistant.com\n')
    
    # Create the zip file
    zip_path = f"downloads/integrity-assistant-{platform}.zip"
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, temp_dir)
                zipf.write(file_path, arcname)
    
    # Clean up temporary directory
    shutil.rmtree(temp_dir)

print("Created all zip files in the downloads directory") 