import subprocess


def run_command(command, capture_output=False):
    """Helper function to run a shell command and optionally capture the output"""
    result = subprocess.run(
        command, shell=True, text=True, capture_output=capture_output
    )
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
    return result


def main():
    print("")


if __name__ == "__main__":
    main()
