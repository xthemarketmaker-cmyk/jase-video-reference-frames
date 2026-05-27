#!/usr/bin/env python3
"""
Jase Video Reference Frame Updater
Usage: python update_last_frame.py "C:\path\to\last-scene-frame.jpg"

This script copies the provided image to last-frame.jpg in the repo,
commits it, and pushes. The raw GitHub URL always serves the latest version.

This is the core of the automated last-frame chaining system.
"""

import sys
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

REPO_DIR = Path(__file__).parent.resolve()
TARGET_IMAGE = REPO_DIR / "last-frame.jpg"

def run(cmd: list[str]) -> None:
    """Run a shell command and raise on failure."""
    result = subprocess.run(cmd, cwd=REPO_DIR, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Command failed: {' '.join(cmd)}")
        print(result.stdout)
        print(result.stderr)
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python update_last_frame.py \"C:\\path\\to\\last-frame.jpg\"")
        print("Example: python update_last_frame.py \"C:\\Users\\Hardcore\\Videos\\scene1_last.jpg\"")
        sys.exit(1)

    source_path = Path(sys.argv[1]).expanduser().resolve()

    if not source_path.exists():
        print(f"ERROR: Source image not found: {source_path}")
        sys.exit(1)

    if not source_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]:
        print(f"WARNING: Unusual extension {source_path.suffix}. Proceeding anyway.")

    print(f"Updating last-frame from: {source_path}")

    # Copy (overwrite) the target
    shutil.copy2(source_path, TARGET_IMAGE)
    print(f"Copied to: {TARGET_IMAGE}")

    # Git operations
    run(["git", "add", "last-frame.jpg"])
    run(["git", "commit", "-m", f"Update last-frame.jpg — {datetime.now().isoformat()}"])
    run(["git", "push"])

    print("\n✅ Success!")
    print("Stable public URL (use this in video tools):")
    print("https://raw.githubusercontent.com/xthemarketmaker-cmyk/jase-video-reference-frames/main/last-frame.jpg")

if __name__ == "__main__":
    main()