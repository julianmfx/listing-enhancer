from pathlib import Path

def get_root_dir() -> Path:
    """
    Walk up the directory tree to ind the project root,
    identified by the presence of a .git folder.

    Returns:
        Path: The root directory of the project.
    
    Raises:
        FileNotFOundError: If no .git folder is found.
    """
    current = Path(__file__).resolve().parent

    while current != current.parent:
        if (current / ".git").exists():
            return current
        current = current.parent
    
    raise (FileNotFoundError("Could not find a .git directory. Are you inside a git repository?"))