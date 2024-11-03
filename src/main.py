import os
import json
import subprocess
from packaging import version

cwd = os.getcwd()


# Load dependencies from package.json
def load_dependencies():
    # Read package.json file
    with open(f"{cwd}/package.json", "r") as f:
        package_data = json.load(f)
    # Extract dependencies from package.json
    dependencies = package_data.get("dependencies", {})
    # Extract devDependencies
    dev_dependencies = package_data.get("devDependencies", {})
    # Extract peerDependencies
    peer_dependencies = package_data.get("peerDependencies", {})
    # Extract optionalDependencies
    optional_dependencies = package_data.get("optionalDependencies", {})

    # Combine all dependencies
    return {
        **dependencies,
        **dev_dependencies,
        **peer_dependencies,
        **optional_dependencies,
    }


# Fetch the latest version of a package from npm
def get_latest_version(package_name):
    # Use 'npm show' to fetch the latest version
    try:
        result = subprocess.run(
            ["npm", "show", package_name, "version"],
            capture_output=True,
            text=True,
            check=True,
        )
        # Return the latest version
        return result.stdout.strip()
    # Handle errors for invalid package names
    except subprocess.CalledProcessError:
        print(f"Could not fetch the version of {package_name}.")
        return None


# Parse the version string and return a version object
def parse_version(version_string):
    """Skip versions with 'file:' prefix."""
    try:
        # Remove caret (^) or tilde (~) for correct comparison
        version_string_cleaned = version_string.lstrip("^~")
        # Use packaging.version.parse, but handle errors for invalid versions
        return version.parse(version_string_cleaned)
    # Handle errors for invalid versions
    except version.InvalidVersion:
        print(f"Warning: Invalid version '{version_string}', skipping.")
        return None


# Check if the current version is outdated
def is_outdated(current_version, latest_version):
    # Skip dependencies with 'file:' prefix
    if current_version.startswith("file:"):
        return False

    # Parse both versions, skip if the current version is invalid
    current_semver = parse_version(current_version)
    # Skip if the latest version is invalid
    latest_semver = parse_version(latest_version)
    # Skip if either version is invalid
    if current_semver is None or latest_semver is None:
        # Skip on invalid version parsing
        return False

    # Check if the latest version is greater than the current version
    return latest_semver > current_semver


# Check for updates for all dependencies
def check_for_updates(dependencies):
    # Dictionary to store updates
    updates = {}
    # Iterate over all dependencies
    for package, current_version in dependencies.items():
        # Fetch the latest version of the package
        latest_version = get_latest_version(package)
        # Check if the current version is outdated
        if latest_version and is_outdated(current_version, latest_version):
            # Store the update in the dictionary
            updates[package] = {
                # Store the current and latest version
                "current_version": current_version,
                # Store the latest version
                "latest_version": latest_version,
            }

    # Return the dictionary with updates
    return updates


# Main function to check for updates
def main():
    # Load dependencies from package.json
    dependencies = load_dependencies()
    # Check for updates
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
