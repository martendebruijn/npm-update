import subprocess
import re

branch_name = "feat-npm-updates"


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
    """Check if there are any updates available"""
    result = run_command("ncu", capture_output=True, suppress_output=False)
    return (
        "No depencies." not in result.stdout
        and "All dependencies match the latest package versions" not in result.stdout
    )


def does_branch_exists(branch):
    """Check if the branch already exists"""
    result = run_command(
        f"git branch --list {branch}", capture_output=True, suppress_output=False
    )
    return branch_name in result.stdout


def does_remote_branch_exists(branch):
    """Check if the branch already exists on a remote"""
    result = run_command(
        "git branch --list --remotes", capture_output=True, suppress_output=False
    )
    remote_branches = result.stdout.strip().split("\n")
    pattern = re.compile(rf".*\b{branch}\b$")
    for remote_branch in remote_branches:
        if pattern.search(remote_branch.strip()):
            return True

    return False


def is_changed():
    """Check if something has changed"""
    result = run_command(
        "git status --short", capture_output=True, suppress_output=False
    )
    return result.stdout != ""


def upgrade_packages(type):
    """Upgrade dependencies according to the target"""
    print(f"🆙 Upgrade {type} versions")
    run_command(f"ncu --target {type} --upgrade")
    if is_changed():
        run_command("git add package*")
        run_command(f"git commit -m '(npm): update {type} versions'")


def create_merge_request(title, description):
    """Create a merge request on GitLab"""
    run_command(f'glab mr create --draft --title "{title}" --description "{description}"')

def check_remote():
    """Check the current remote"""
    result = run_command("git remote -v", capture_output=True, suppress_output=False)
    if "draft.beerntea.com" in result.stdout:
        return "beerntea"
    else:
        return False
    
def create_merge_request(title, description):
        print(f"Create merge request: {title}")
        run_command(f'glab mr create --draft --title "{title}" --description "{description}"')

def create_description():
    result = run_command("ncu --target minor", capture_output=True, suppress_output=False)
    lines = result.stdout.splitlines()
    filtered_lines = lines[1:-1]
    return "\n\n".join(filtered_lines)


def main():
    print("🕵️‍♂️ Checking for updates")
    if are_updates_available():
        run_command("git fetch --prune")
        if does_branch_exists(branch_name):
            print(f"❗️ The branch {branch_name} already exists")
            return
        if does_remote_branch_exists(branch_name):
            print(f"❗️ The branch {branch_name} already exists on a remote")
            return

        print(f'👾 Create branch "{branch_name}"')
        run_command(f"git switch --create {branch_name}")
        description = create_description()
        upgrade_packages("minor")
        print("👾 Push changes")
        run_command("git push")
        remote = check_remote()
        if remote == 'beerntea':
            print("👾 Create pull request")
            create_merge_request('NPM dependencies update', description)
        # List remaining (major) updateable packages
        print("👨‍💻 Check manually:")
        run_command("ncu", capture_output=False, suppress_output=False)
    else:
        print("✅ All dependencies are up to date")


if __name__ == "__main__":
    main()
