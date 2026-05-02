import subprocess
import sys

packages = [
    "colorama",
    "pillow",
    "tkvideo",
    "pyperclip"
]

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

for pkg in packages:
    try:
        install(pkg)
        print(f"{pkg} installed successfully")
    except Exception as e:
        print(f"Failed to install {pkg}: {e}")