import subprocess


def run_command(command, capture_output=False, suppress_output=True):
    """Helper function to run a shell command and optionally capture the output"""
    if suppress_output:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            capture_output=capture_output,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    else:
        result = subprocess.run(
            command, shell=True, text=True, capture_output=capture_output
        )

    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
    return result


def are_updates_available():
    result = run_command("ncu", capture_output=True, suppress_output=False)
    return (
        "No depencies." not in result.stdout
        and "All dependencies match the latest package versions" not in result.stdout
    )


def does_branch_exists(branch):
    result = run_command(
        f"git branch --list {branch}", capture_output=True, suppress_output=False
    )
    return result.stdout != ""


def is_changed():
    result = run_command(
        "git status --short", capture_output=True, suppress_output=False
    )
    return result.stdout != ""


def upgrade_packages(type):
    print(f"🆙 Upgrade {type} versions")
    run_command(f"ncu --target {type} --upgrade")
    if is_changed():
        run_command("git add package*")
        run_command(f"git commit -m '(npm): update {type} versions'")


def main():
    print("🕵️‍♂️ Checking for updates")
    if are_updates_available():
        if not does_branch_exists("feat-npm-update"):
            print('👾 Create branch "feat-npm-updates"')
            run_command("git switch --create feat-npm-updates")
            upgrade_packages("patch")
            upgrade_packages("minor")
            print("👾 Push changes")
            run_command("git push")
        else:
            print('❗️ The branch "feat-npm-updates" already exists')
    else:
        print("✅ All dependencies are up to date")


if __name__ == "__main__":
    main()
