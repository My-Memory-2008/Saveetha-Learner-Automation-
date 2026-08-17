import subprocess
import sys
import time
import os

# Workflow file to trigger
# If your file is actually named "reatsrt.yml", change this to "reatsrt.yml"
WORKFLOW_FILE = "restart.yml"

# Branch to trigger the workflow on
TARGET_BRANCH = os.getenv("TARGET_BRANCH", "main")

# Pause for 2 minutes
WAIT_SECONDS = 2 * 60


def main():
    print(f"Waiting {WAIT_SECONDS} seconds before triggering {WORKFLOW_FILE}...", flush=True)
    time.sleep(WAIT_SECONDS)

    print(f"Triggering workflow: {WORKFLOW_FILE}", flush=True)

    try:
        subprocess.run(
            [
                "gh",
                "workflow",
                "run",
                WORKFLOW_FILE,
                "--ref",
                TARGET_BRANCH,
            ],
            check=True,
            text=True,
            capture_output=True,
        )

        print("Workflow triggered successfully. Terminating scheduler.py.", flush=True)
        sys.exit(0)

    except subprocess.CalledProcessError as e:
        print("Failed to trigger workflow.", flush=True)
        print(f"Error: {e.stderr}", flush=True)
        sys.exit(1)

    except FileNotFoundError:
        print("GitHub CLI 'gh' is not installed or not available.", flush=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
