# hooks/rules.py

from pathlib import Path

def rule_no_myorg_tech(file_path, content):
    if "myorg.tech" in content:
        return f"Error: The file {file_path} contains 'myorg.tech'"
    
rules = [
    {
        "description": "No myorg.tech in files",
        "check": rule_no_myorg_tech,
        "file_filter": lambda file_path: file_path.suffix == ".yaml" and not file_path.name == ".pre-commit-config.yaml"
    }
]