import subprocess
import sys


def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])


if __name__ == "__main__":
    install("pyglet")
    install("numpy")
