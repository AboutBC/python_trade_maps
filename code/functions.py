import subprocess
import sys
import importlib.util
import os
from pathlib import Path

def install_packages(packages):
    for package in packages:
        print(package)
        spec = importlib.util.find_spec(package)
        if spec is None:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

  
def path_to_project_root(project_name):
        path = os.getcwd()
        while not str(path).endswith(project_name):
            path = Path(path).parent

        print(path)
        return path