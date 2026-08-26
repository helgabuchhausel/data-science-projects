import subprocess
import sys

def install_dependencies():
    packages = [
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "kagglehub",
        "pillow",
        "torch",
        "torchvision",
        "squarify",
        "jupyter"
    ]
    
    print("Installing dependencies...")
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}: {e}")
            sys.exit(1)
            
    print("All dependencies installed successfully.")

if __name__ == "__main__":
    install_dependencies()
