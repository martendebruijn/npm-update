import os
import json
import subprocess
from packaging import version

pwd = os.getcwd()


def load_dependencies():
    with open(f"{pwd}/package.json", "r") as f:
        package_data = json.load(f)
    dependencies = package_data.get("dependencies", {})
    dev_dependencies = package_data.get("devDependencies", {})
    peer_dependencies = package_data.get("peerDependencies", {})
    optional_dependencies = package_data.get("optionalDependencies", {})
    return {
        **dependencies,
        **dev_dependencies,
        **peer_dependencies,
        **optional_dependencies,
    }


def get_latest_version(package_name):
    try:
        # Use 'npm show' to fetch the latest version
        result = subprocess.run(
            ["npm", "show", package_name, "version"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        print(f"Could not fetch the version of {package_name}.")
        return None


def parse_version(version_string):
    """Skip versions with 'file:' prefix."""
    try:
        # Remove caret (^) or tilde (~) for correct comparison
        version_string_cleaned = version_string.lstrip("^~")
        # Use packaging.version.parse, but handle errors for invalid versions
        return version.parse(version_string_cleaned)
    except version.InvalidVersion:
        print(f"Warning: Invalid version '{version_string}', skipping.")
        return None


def is_outdated(current_version, latest_version):
    # Skip dependencies with 'file:' prefix
    if current_version.startswith("file:"):
        return False

    # Parse both versions, skip if the current version is invalid
    current_semver = parse_version(current_version)
    latest_semver = parse_version(latest_version)
    if current_semver is None or latest_semver is None:
        return False  # Skip on invalid version parsing

    # Check if the latest version is greater than the current version
    return latest_semver > current_semver


def check_for_updates(dependencies):
    updates = {}
    for package, current_version in dependencies.items():
        latest_version = get_latest_version(package)
        if latest_version and is_outdated(current_version, latest_version):
            updates[package] = {
                "current_version": current_version,
                "latest_version": latest_version,
            }
    return updates


def main():
    dependencies = load_dependencies()
    updates = check_for_updates(dependencies)
    if updates:
        print("Updates available for the following dependencies:")
        for package, versions in updates.items():
            print(
                f"{package}: {versions['current_version']} -> {versions['latest_version']}"
            )
    else:
        print("All dependencies are up-to-date.")


if __name__ == "__main__":
    main()
