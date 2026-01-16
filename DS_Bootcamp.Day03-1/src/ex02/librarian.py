#!/usr/bin/env python3
import sys
import subprocess
import os
import shutil

def check_env():
    if sys.prefix == sys.base_prefix:
        raise EnvironmentError("Not running inside a virtual environment!")
    
def install_lib():
    with open("requirements.txt", "w") as f:
        f.write("beautifulsoup4\npytest\n")

    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def display_lib():
    installed = subprocess.check_output([sys.executable, "-m", "pip", "freeze"]).decode()
    print(installed.strip())
    with open("requirements.txt", "w") as f:
        f.write(installed)

def archive_env():
    venv_path = sys.prefix
    archive_name = "duckfiev_archive"

    shutil.make_archive(archive_name, 'zip', venv_path)
    print(f"Virtual environment archived as {archive_name}.zip")

if __name__ == "__main__":
    check_env()
    install_lib()
    display_lib()
    archive_env()
