# import subprocess
# import sys
# import time
# import os

# # Workflow file to trigger
# # If your file is actually named "reatsrt.yml", change this to "reatsrt.yml"
# WORKFLOW_FILE = "restart.yml"

# # Branch to trigger the workflow on
# TARGET_BRANCH = os.getenv("TARGET_BRANCH", "main")

# # Pause for 2 minutes
# WAIT_SECONDS = 2 * 60


# def main():
#     print(f"Waiting {WAIT_SECONDS} seconds before triggering {WORKFLOW_FILE}...", flush=True)
#     time.sleep(WAIT_SECONDS)

#     print(f"Triggering workflow: {WORKFLOW_FILE}", flush=True)

#     try:
#         subprocess.run(
#             [
#                 "gh",
#                 "workflow",
#                 "run",
#                 WORKFLOW_FILE,
#                 "--ref",
#                 TARGET_BRANCH,
#             ],
#             check=True,
#             text=True,
#             capture_output=True,
#         )

#         print("Workflow triggered successfully. Terminating scheduler.py.", flush=True)
#         sys.exit(0)

#     except subprocess.CalledProcessError as e:
#         print("Failed to trigger workflow.", flush=True)
#         print(f"Error: {e.stderr}", flush=True)
#         sys.exit(1)

#     except FileNotFoundError:
#         print("GitHub CLI 'gh' is not installed or not available.", flush=True)
#         sys.exit(1)


# if __name__ == "__main__":
#     main()






import subprocess
import sys
import time
import os

# Workflow file to trigger (must exactly match the filename in .github/workflows/)
WORKFLOW_FILE = "restart.yml"

# Branch to trigger the workflow on (defaults to 'main' if not set in GitHub Actions)
TARGET_BRANCH = os.getenv("TARGET_BRANCH", "main")

# Pause for 2 minutes before triggering
WAIT_SECONDS = 2 * 60

# Retry settings to handle transient GitHub API errors (like HTTP 503)
MAX_RETRIES = 10
RETRY_DELAY_SECONDS = 15


def main():
    print(f"⏳ Waiting {WAIT_SECONDS} seconds before triggering {WORKFLOW_FILE}...", flush=True)
    time.sleep(WAIT_SECONDS)

    print(f"🚀 Attempting to trigger workflow: {WORKFLOW_FILE}", flush=True)

    for attempt in range(1, MAX_RETRIES + 1):
        print(f"🔄 Attempt {attempt} of {MAX_RETRIES}...", flush=True)
        try:
            # Note: We removed 'check=True' to handle the return code manually for retries
            result = subprocess.run(
                [
                    "gh",
                    "workflow",
                    "run",
                    WORKFLOW_FILE,
                    "--ref",
                    TARGET_BRANCH,
                ],
                text=True,
                capture_output=True,
            )

            if result.returncode == 0:
                print("✅ Workflow triggered successfully. Terminating scheduler.py.", flush=True)
                sys.exit(0)
            else:
                error_msg = result.stderr.strip()
                print(f"⚠️ Attempt {attempt} failed.", flush=True)
                print(f"Error output: {error_msg}", flush=True)
                
                # Check if it's a transient GitHub server error (500, 502, 503, 504)
                if "503" in error_msg or "500" in error_msg or "502" in error_msg or "504" in error_msg:
                    if attempt < MAX_RETRIES:
                        print(f"⏳ Transient server error detected. Retrying in {RETRY_DELAY_SECONDS} seconds...", flush=True)
                        time.sleep(RETRY_DELAY_SECONDS)
                        continue
                    else:
                        print("❌ Max retries reached due to persistent GitHub server errors.", flush=True)
                else:
                    # For non-transient errors (e.g., 404 Not Found, 403 Forbidden, typo in workflow name), fail immediately
                    print("❌ Non-transient error detected (e.g., workflow not found or permissions issue). Aborting retries.", flush=True)
                
                sys.exit(1)

        except FileNotFoundError:
            print("❌ GitHub CLI 'gh' is not installed or not available in the system PATH.", flush=True)
            sys.exit(1)
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}", flush=True)
            sys.exit(1)

    print("❌ Failed to trigger workflow after all retries.", flush=True)
    sys.exit(1)


if __name__ == "__main__":
    main()
