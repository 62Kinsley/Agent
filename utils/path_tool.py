#provide absolute path for the given relative path

import os

def get_project_root() -> str: 

    """
    Get the root directory of the project.

    Returns:
        str: The absolute path to the project root directory.
    """
    # Get the current absolute path of this file
    current_file_abspath = os.path.abspath(__file__)
    
    # current working directory
    current_dir = os.path.dirname(current_file_abspath)
    
    # current working root
    project_root = os.path.dirname(current_dir)
    
    return project_root


def get_abs_path(relative_path: str) -> str:
    """
    Get the absolute path for the given relative path.

    Args:
        relative_path (str): The relative path to convert.

    Returns:
        str: The absolute path.
    """
    project_root = get_project_root()
    return os.path.join(project_root, relative_path)


if __name__ == "__main__":
    # Example usage
    relative_path = "data/选购指南.txt"
    absolute_path = get_abs_path(relative_path)
    print(f"Absolute path: {absolute_path}")