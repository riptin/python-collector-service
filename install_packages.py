import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_packages():
    try:
        with open("requirements.txt", "r") as f:
            for line in f:
                pkg = line.strip()
                if not pkg or pkg.startswith("#"):
                    continue
                try:
                    __import__(pkg.split("==")[0])
                except ImportError:
                    print(f"Package '{pkg}' not found. Installing...")
                    install_package(pkg)
    except FileNotFoundError:
        print("requirements.txt not found.")