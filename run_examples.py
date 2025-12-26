"""Run every `example.py` found in the repository using the current Python interpreter."""

import os
import subprocess
import sys


def main():
    root = os.path.dirname(__file__)
    for dirpath, _, filenames in os.walk(root):
        if "example.py" in filenames:
            path = os.path.join(dirpath, "example.py")
            print("--- Running:", path)
            subprocess.run([sys.executable, path])


if __name__ == "__main__":
    main()
