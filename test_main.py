import json
import os
from main import run_command, are_updates_available, upgrade_packages


def test_run_command_real():
    """Test run_command with a real command"""
    result = run_command(
        "echo 'Hello, World!'", capture_output=True, suppress_output=False
    )

    assert result.returncode == 0
    assert result.stdout.strip() == "Hello, World!"


def test_run_command_real_failure():
    """Test run_command with a failing command"""
    result = run_command("invalid-command", capture_output=True, suppress_output=False)

    assert result.returncode != 0
    assert (
        "command not found" in result.stderr.lower()
        or "is not recognized" in result.stderr.lower()
    )


def test_are_updates_available(tmp_path):
    """Test are_updates_available"""
    package_json_path = tmp_path / "package.json"
    package_json_content = {
        "name": "test-package",
        "version": "1.0.0",
        "dependencies": {"@martendebruijn/types": "1.0.0"},
    }
    with open(package_json_path, "w") as f:
        json.dump(package_json_content, f, indent=4)

    current_dir = os.getcwd()
    os.chdir(tmp_path)
    try:
        updates_available = are_updates_available()
    finally:
        os.chdir(current_dir)

    assert updates_available is True


# Todo:
# are_updates_available:
# Test when there are no dependencies
# Test when all dependencies are already up to date
# Test when ncu is not installed


# upgrade_packages:
# Test if patch versions will be updated
def test_upgrade_packages_patch(tmp_path):
    """Test upgrade_packages with patch versions"""
    package_json_path = tmp_path / "package.json"
    package_json_content = {
        "name": "test-package",
        "version": "1.0.0",
        "dependencies": {"@martendebruijn/types": "2.0.1"},
    }
    with open(package_json_path, "w") as f:
        json.dump(package_json_content, f, indent=4)

    current_dir = os.getcwd()
    os.chdir(tmp_path)
    try:
        upgrade_successful = upgrade_packages("minor")
    finally:
        os.chdir(current_dir)

    assert upgrade_successful is True

    with open(package_json_path) as f:
        updated_package_json_content = json.load(f)

    assert (
        updated_package_json_content["dependencies"]["@martendebruijn/types"] != "2.0.1"
    )
    assert (
        updated_package_json_content["dependencies"]["@martendebruijn/types"] == "2.0.2"
    )


# Test if minor versions will be updatedd
def test_upgrade_packages_minor(tmp_path):
    """Test upgrade_packages with minor versions"""
    package_json_path = tmp_path / "package.json"
    package_json_content = {
        "name": "test-package",
        "version": "1.0.0",
        "dependencies": {"@martendebruijn/types": "1.0.0"},
    }
    with open(package_json_path, "w") as f:
        json.dump(package_json_content, f, indent=4)

    current_dir = os.getcwd()
    os.chdir(tmp_path)
    try:
        upgrade_successful = upgrade_packages("minor")
    finally:
        os.chdir(current_dir)

    assert upgrade_successful is True

    with open(package_json_path) as f:
        updated_package_json_content = json.load(f)

    assert (
        updated_package_json_content["dependencies"]["@martendebruijn/types"] != "1.0.0"
    )
    assert (
        updated_package_json_content["dependencies"]["@martendebruijn/types"] == "1.4.0"
    )


# Test if major versions will not be updated
# Test if package.json is untracked
