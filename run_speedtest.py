#!/usr/bin/env python3
import subprocess
import sys

def run_speedtest():
    """Runs the speedtest command and prints the JSON output."""
    try:
        # The --accept-license flag is required to run the speedtest cli
        command = ["speedtest", "--accept-license", "--accept-gdpr", "--format=json"]
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )
        print(result.stdout)
    except FileNotFoundError:
        print("Error: 'speedtest' command not found. Please make sure it's installed and in your PATH.", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error running speedtest: {e}", file=sys.stderr)
        print(f"Stderr: {e.stderr}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run_speedtest()
