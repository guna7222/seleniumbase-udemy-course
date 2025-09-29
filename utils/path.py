import os

import os

def get_project_path(*path_parts: str) -> str:
    """
    Return absolute path for a file/folder inside the project.
    Example:
        get_project_path("data", "some_image.png")
        get_project_path("tests", "fixtures", "test_data.json")
    """
    # Find project root (folder where this utils file lives, then go up if needed)
    project_root = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(project_root, ".git")) \
          and project_root != os.path.dirname(project_root):
        # keep going up until project root (detected via .git or stop at top)
        project_root = os.path.dirname(project_root)

    # Join all given parts relative to root
    return os.path.abspath(os.path.join(project_root, *path_parts))

