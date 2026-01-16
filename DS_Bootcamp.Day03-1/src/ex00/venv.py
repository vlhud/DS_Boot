#!/usr/bin/env python3
import os

def get_virtual_env_path():
    # Get the path of the current virtual environment (or None if not in one)
    return os.environ.get('VIRTUAL_ENV', None)

if __name__ == "__main__":
    env_path = get_virtual_env_path()
    if env_path:
        print(f"Your current virtual env is {env_path}\n")
    else:
        print("No virtual environment is active.\n")